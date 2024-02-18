package handler

import (
	"errors"
	"log"
	"machine-coding-splitwise/internal/model"
	"machine-coding-splitwise/internal/model/expense"
	"machine-coding-splitwise/internal/service"
	"machine-coding-splitwise/pkg"
)

type TransactionHandler struct {
	service service.TransactionService
}

func GetTransactionHandler() *TransactionHandler {
	return &TransactionHandler{
		service: service.GetTransactionService(),
	}
}

func (h *TransactionHandler) AddUser(user *model.User) error {
	ok := h.service.AddUser(user)
	if !ok {
		log.Println("user cannot be added: ", *user)
		return errors.New("user cannot be added")
	}
	return nil
}

func (h *TransactionHandler) ShowBalance() {
	h.service.ShowBalance()
}

func (h *TransactionHandler) CreateExpense(expenseType pkg.ExpenseType, expense expense.Expense) {
	h.service.CreateExpense(expenseType, expense)
}
