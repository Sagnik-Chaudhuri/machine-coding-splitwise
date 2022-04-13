from classes.User import User


class Split():
    def __init__(self, user: User) -> None:
        self.user: User = user

    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user = user

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount
