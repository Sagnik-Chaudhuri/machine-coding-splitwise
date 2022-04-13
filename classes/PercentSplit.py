from classes.Split import Split


class PercentSplit(Split):
    def __init__(self, user, percent) -> None:
        super().__init__(user)
        self.percent = percent

    def get_percent(self):
        return self.percent

    def set_percent(self, percent):
        self.percent = percent
