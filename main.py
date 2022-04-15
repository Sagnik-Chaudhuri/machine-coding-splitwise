from config import EQUAL_EXPENSE_TYPE_NAME, EXACT_EXPENSE_TYPE_NAME
from classes.TransactionManager import TransactionManager
from classes.User import User


def main():

    user1 = User("user_1", 'User 1', 'a', '123')
    user2 = User("user_2", 'User 2', 'bcd', '123')
    user3 = User("user_3", 'User 3', 'cd', '123')
    user4 = User("user_4", 'User 4', 'd', '123')

    transaction_manager = TransactionManager()
    transaction_manager.add_user(user1)
    transaction_manager.add_user(user2)
    transaction_manager.add_user(user3)
    transaction_manager.add_user(user4)
    # transaction_manager.show_all_balances()
    transaction_manager.create_expense(user1, 1000, EQUAL_EXPENSE_TYPE_NAME, [
                                       user1, user2, user3, user4])
    # transaction_manager.show_all_balances()
    # transaction_manager.show_balance_for_user(user1)
    transaction_manager.create_expense(user1, 1250, EXACT_EXPENSE_TYPE_NAME, [
                                       user2, user3], [370, 880])
    transaction_manager.create_expense(user3, 1000, EXACT_EXPENSE_TYPE_NAME, [
                                       user2, user1], [300, 700])
    # transaction_manager.show_balance_for_user('user_3')
    transaction_manager.show_all_balances()

    return None


main()
