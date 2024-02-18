from config import EXACT_EXPENSE_TYPE_NAME
from classes.Split import Split


class ExactSplit(Split):
    def __init__(self, user_id, amount) -> None:
        super().__init__(user_id, amount)
        self.type = EXACT_EXPENSE_TYPE_NAME
