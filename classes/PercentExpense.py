from classes.PercentSplit import PercentSplit
from classes.Expense import Expense


class PercentExpense(Expense):
    def __init__(self, amount, paid_by, splits, metadata) -> None:
        super().__init__(amount, paid_by, splits, metadata)

    def validate(self):
        for split in self.get_splits():
            if not isinstance(split, PercentSplit):
                return False

        total_percent = 100
        sum_split_percent = 0
        for split in self.get_splits():
            percent_split: PercentSplit = split
            sum_split_percent += percent_split.get_percent()

        if total_percent != sum_split_percent:
            return False

        return True
