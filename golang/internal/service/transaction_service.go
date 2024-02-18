package service

import (
	"log"
	"machine-coding-splitwise/internal/model"
	"machine-coding-splitwise/internal/model/expense"
	"machine-coding-splitwise/pkg"
	"math"
	"sync"
)

type TransactionService interface {
	AddUser(user *model.User) bool
	ShowBalance()
	CreateExpense(expenseType pkg.ExpenseType, expense expense.Expense)
}

type TransactionServiceInMemoryImpl struct {
	BalanceSheet map[string]map[string]float64 // map of user_id to balance_user and amount
}

var transactionServiceInstance TransactionService
var transactionServiceOnce sync.Once

func GetTransactionService() TransactionService {
	log.Println("init TransactionService")
	transactionServiceOnce.Do(func() {
		transactionServiceInstance = &TransactionServiceInMemoryImpl{
			BalanceSheet: map[string]map[string]float64{},
		}
	})
	return transactionServiceInstance
}

func (t *TransactionServiceInMemoryImpl) AddUser(user *model.User) bool {
	//userId := user.Id
	//_, ok := t.BalanceSheet[userId]
	//if ok {
	//	// idempotent call since user already added.
	//	log.Println("user : is already added", user.Name)
	//	return false
	//	//} else {
	//	//	t.BalanceSheet[userId] = map[string]float64{}
	//	//}
	//}
	return true
}

func (t *TransactionServiceInMemoryImpl) ShowBalance() {
	if len(t.BalanceSheet) == 0 {
		log.Println("no balances")
	} else {
		for user := range t.BalanceSheet {
			t.showBalancePerUser(user)
		}
	}
}

func (t *TransactionServiceInMemoryImpl) showBalancePerUser(userId string) {

	for balanceUser, balanceAmount := range t.BalanceSheet[userId] {
		if balanceAmount < 0 {
			log.Printf("%s is owed by %s: %.2f\n", balanceUser, userId, math.Abs(balanceAmount))
		} else {
			log.Printf("%s owes %s: %.2f\n", balanceUser, userId, balanceAmount)
		}
	}
}

func (t *TransactionServiceInMemoryImpl) CreateExpense(expenseType pkg.ExpenseType, expense expense.Expense) {
	paidByUserId := expense.PaidBy.Id
	//t.BalanceSheet[paidByUserId] = map[string]float64{}
	if expenseType == pkg.EXPENSE_TYPE_EQUAL {
		totalSplits := len(expense.Splits)
		splitAmount := math.Round(expense.Amount*100/float64(totalSplits)) / 100.0
		for _, split := range expense.Splits {
			// ensuring that split.Amount has equal amount for all users in splits slice.
			// ideally, should be validated during split creation.
			split.Amount = splitAmount
		}
	}

	for _, split := range expense.Splits {
		if paidByUserId != split.UserId {
			// add +ve expense beared by paidByUserId for list of users, as provided in split
			if paidByUserBalance, ok := t.BalanceSheet[paidByUserId]; ok {
				if _, ok := paidByUserBalance[split.UserId]; ok {
					t.BalanceSheet[paidByUserId][split.UserId] += split.Amount
				} else {
					t.BalanceSheet[paidByUserId][split.UserId] = split.Amount
				}
			} else {
				t.BalanceSheet[paidByUserId] = map[string]float64{
					split.UserId: split.Amount,
				}
			}
			// remove from balance sheet if ultimately amount = 0
			if val, ok := t.BalanceSheet[paidByUserId][split.UserId]; ok && val == 0 {
				delete(t.BalanceSheet[paidByUserId], split.UserId)
			}

			// add -ve expense owed by current user for all list of users as provided in split.
			// it is -ve expense, since current user owes it to paidByUser
			if paidByUserBalance, ok := t.BalanceSheet[split.UserId]; ok {
				if _, ok := paidByUserBalance[paidByUserId]; ok {
					t.BalanceSheet[split.UserId][paidByUserId] -= split.Amount
				} else {
					t.BalanceSheet[split.UserId][paidByUserId] = -split.Amount
				}
			} else {
				t.BalanceSheet[split.UserId] = map[string]float64{
					paidByUserId: -split.Amount,
				}
			}
			// remove from balance sheet if ultimately amount = 0
			if val, ok := t.BalanceSheet[split.UserId][paidByUserId]; ok && val == 0 {
				delete(t.BalanceSheet[split.UserId], paidByUserId)
			}

		}
	}
}
