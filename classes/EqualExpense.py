from config import EQUAL_EXPENSE_TYPE_NAME
from classes.Expense import Expense


class EqualExpense(Expense):
    def __init__(self, amount, paid_by, splits) -> None:
        super().__init__(amount, paid_by, splits)
        self.type = EQUAL_EXPENSE_TYPE_NAME
