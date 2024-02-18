package pkg

type ExpenseType int

const (
	EXPENSE_TYPE_EQUAL   ExpenseType = iota
	EXPENSE_TYPE_EXACT   ExpenseType = iota
	EXPENSE_TYPE_PERCENT ExpenseType = iota
)
