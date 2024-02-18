package expense

import (
	"machine-coding-splitwise/internal/model"
	"machine-coding-splitwise/internal/model/split"
)

type Expense struct {
	Amount float64
	PaidBy *model.User
	Splits []*split.Split
}
