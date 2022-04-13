from classes.Split import Split


class ExactSplit(Split):
    def __init__(self, user, amount) -> None:
        super().__init__(user)
        self.amount = amount
