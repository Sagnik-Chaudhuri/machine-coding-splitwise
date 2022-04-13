from unicodedata import name


class ExpenseMetadata:
    def __init__(self, name, notes) -> None:
        self.name = name
        self.notes = notes

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_notes(self):
        return self.notes

    def set_notes(self, notes):
        self.notes = notes
