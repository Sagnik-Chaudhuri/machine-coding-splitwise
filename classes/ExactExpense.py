from classes.ExactSplit import ExactSplit
from classes.Expense import Expense


class ExactExpense(Expense):
    def __init__(self, amount, paid_by, splits, metadata) -> None:
        super().__init__(amount, paid_by, splits, metadata)

    def validate(self):
        for split in self.get_splits():
            if not isinstance(split, ExactSplit):
                return False

        total_amount = self.get_amount()
        sum_split_amount = 0
        for split in self.get_splits():
            exact_split: ExactSplit = split
            sum_split_amount += exact_split.get_amount()

        if total_amount != sum_split_amount:
            return False

        return True
