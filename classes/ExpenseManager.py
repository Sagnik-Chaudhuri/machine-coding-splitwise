from classes.Split import Split
from classes.ExpenseService import ExpenseService
import string
from typing import Dict, List
from classes.Expense import Expense
from classes.User import User


class ExpenseManager():
    def __init__(self) -> None:
        self.expenses: List[Expense] = []
        self.user_map = {}
        self.balance_sheet = {}

    def add_user(self, user: User):
        self.user_map[user.get_id()] = user
        self.balance_sheet[user.get_id()] = {}

    def add_expense(self, expense_type, amount, paid_by, splits: List[Split], expense_metadata):
        expense = ExpenseService.create_expense(
            expense_type, amount, paid_by, splits, expense_metadata)
        self.expenses.append(expense)
        for split in splits:
            paid_to = split.get_user().get_id()
            balances = self.balance_sheet.get(paid_by)
            if balances is None:
                balances[paid_to] = 0
