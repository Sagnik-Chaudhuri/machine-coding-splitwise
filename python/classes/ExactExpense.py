from config import EXACT_EXPENSE_TYPE_NAME
from classes.Expense import Expense


class ExactExpense(Expense):
    def __init__(self, amount, paid_by, splits) -> None:
        super().__init__(amount, paid_by, splits)
        self.type = EXACT_EXPENSE_TYPE_NAME
