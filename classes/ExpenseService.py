from typing import List
from classes.Split import Split
from classes.PercentSplit import PercentSplit
from classes.ExactExpense import ExactExpense
from classes.EqualExpense import EqualExpense
from classes.PercentExpense import PercentExpense
from .config import EXACT_EXPENSE_TYPE, EQUAL_EXPENSE_TYPE, PERCENT_EXPENSE_TYPE


class ExpenseService:
    def __init__(self) -> None:
        pass

    @classmethod
    def create_expense(cls, expense_type, amount, paid_by, splits: List[Split], expense_metadata):
        if expense_type == EXACT_EXPENSE_TYPE:
            return ExactExpense(amount, paid_by, splits, expense_metadata)
        elif expense_type == EQUAL_EXPENSE_TYPE:
            total_splits = len(splits)
            split_amount = round(amount*100/total_splits)/100.0
            for split in splits:
                split.set_amount(split_amount)
            splits[0].set_amount(
                split_amount + (amount - split_amount*total_splits))
            return EqualExpense(amount, paid_by, splits, expense_metadata)
        elif expense_type == PERCENT_EXPENSE_TYPE:
            for split in splits:
                percent_split: PercentSplit = split
                split.set_amount((amount*percent_split.get_percent())/100.0)
            return PercentExpense(amount, paid_by, splits, expense_metadata)

        return None
