from classes.EqualSplit import EqualSplit
from classes.Expense import Expense


class EqualExpense(Expense):
    def __init__(self, amount, paid_by, splits, metadata) -> None:
        super().__init__(amount, paid_by, splits, metadata)

    def validate(self):
        for split in self.get_splits():
            if not isinstance(split, EqualSplit):
                return False

        return True
