package main

import (
	"log"
	"machine-coding-splitwise/internal/handler"
	"machine-coding-splitwise/internal/model"
	"machine-coding-splitwise/internal/model/expense"
	"machine-coding-splitwise/internal/model/split"
	"machine-coding-splitwise/pkg"
)

func main() {

	// please note that this was what I could come up with given the time limit
	// however, please try to explain scope of improvements during the interview
	log.Println("inside main")
	user1 := &model.User{
		Id:     "user_1",
		Name:   "user_1",
		Email:  "user_1",
		Mobile: "user_1",
	}
	user2 := &model.User{
		Id:     "user_2",
		Name:   "user_2",
		Email:  "user_2",
		Mobile: "user_2",
	}
	user3 := &model.User{
		Id:     "user_3",
		Name:   "user_3",
		Email:  "user_3",
		Mobile: "user_3",
	}
	user4 := &model.User{
		Id:     "user_4",
		Name:   "user_4",
		Email:  "user_4",
		Mobile: "user_4",
	}
	tHandler := handler.GetTransactionHandler()
	tHandler.AddUser(user1)
	tHandler.AddUser(user2)
	tHandler.AddUser(user3)
	tHandler.AddUser(user4)
	tHandler.CreateExpense(pkg.EXPENSE_TYPE_EQUAL, expense.Expense{
		Amount: 1000,
		PaidBy: user1,
		Splits: []*split.Split{
			{
				UserId: "user_1",
			},
			{
				UserId: "user_2",
			},
			{
				UserId: "user_3",
			},
			{
				UserId: "user_4",
			},
		},
	})

	tHandler.CreateExpense(pkg.EXPENSE_TYPE_EXACT, expense.Expense{
		Amount: 1250,
		PaidBy: user1,
		Splits: []*split.Split{
			{
				UserId: "user_2",
				Amount: 370,
			},
			{
				UserId: "user_3",
				Amount: 880,
			},
		},
	})
	//
	tHandler.CreateExpense(pkg.EXPENSE_TYPE_EXACT, expense.Expense{
		Amount: 1000,
		PaidBy: user3,
		Splits: []*split.Split{
			{
				UserId: "user_2",
				Amount: 300,
			},
			{
				UserId: "user_1",
				Amount: 700,
			},
		},
	})
	tHandler.ShowBalance()
}
