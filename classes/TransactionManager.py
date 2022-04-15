from config import EQUAL_EXPENSE_TYPE_NAME, EXACT_EXPENSE_TYPE_NAME, EXPENSE_TYPES
from typing import List
from classes.User import User


class TransactionManager:
    def __init__(self) -> None:
        self.balance_sheet = {}

    def show_balance_for_user(self, user_id):
        if self.balance_sheet.get(user_id) is None:
            print('\nNo Balances')
            return
        else:
            balance = self.balance_sheet.get(user_id)
            for balance_user, amount in balance.items():
                if amount < 0:
                    print(f'\n{user_id} owes {balance_user}: {abs(amount)}')
                else:
                    print(f'\n{balance_user} owes {user_id}: {amount}')

        return

    def show_all_balances(self):
        if len(self.balance_sheet.keys()) == 0:
            print("\nNo Balances")
        for user_id in self.balance_sheet.keys():
            self.show_balance_for_user(user_id)

    def create_expense(self, paid_by: User, amount, expense_type, users: List[User], users_expenses=[]):
        paid_by_user_id = paid_by.get_user_id()
        if expense_type not in EXPENSE_TYPES:
            print('\nError, expense type dne')
            return None

        if expense_type == EQUAL_EXPENSE_TYPE_NAME:
            individual_amount = amount / len(users)

            for user in users:
                user_id = user.get_user_id()
                if paid_by_user_id == user_id:
                    continue

                if self.balance_sheet[paid_by_user_id].get(user_id) is None:
                    self.balance_sheet[paid_by_user_id][user_id] = individual_amount
                else:
                    self.balance_sheet[paid_by_user_id][user_id] += individual_amount

                if self.balance_sheet[user_id].get(paid_by_user_id) is None:
                    self.balance_sheet[user_id][paid_by_user_id] = (
                        -1)*individual_amount
                else:
                    self.balance_sheet[user_id][paid_by_user_id] -= individual_amount

        if expense_type == EXACT_EXPENSE_TYPE_NAME:
            for i in range(0, len(users)):
                user_id = users[i].get_user_id()
                individual_amount = users_expenses[i]
                if paid_by_user_id == user_id:
                    continue
                if self.balance_sheet[paid_by_user_id].get(user_id) is None:
                    self.balance_sheet[paid_by_user_id][user_id] = individual_amount
                else:
                    self.balance_sheet[paid_by_user_id][user_id] += individual_amount

                if self.balance_sheet[user_id].get(paid_by_user_id) is None:
                    self.balance_sheet[user_id][paid_by_user_id] = (
                        -1)*individual_amount
                else:
                    self.balance_sheet[user_id][paid_by_user_id] -= individual_amount

        return None

    def add_user(self, user: User):
        user_id = user.get_user_id()
        if self.balance_sheet.get(user_id) is not None:
            print('\nUser already exists in sheet')
        else:
            self.balance_sheet[user_id] = {}
