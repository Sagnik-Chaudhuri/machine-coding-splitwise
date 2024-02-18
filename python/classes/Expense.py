from typing import List
from classes.Split import Split


class Expense:
    def __init__(self, amount, paid_by, splits: List[Split]) -> None:
        self.amount = amount
        self.paid_by = paid_by
        self.splits = splits

    # Validate Expenses for both types
