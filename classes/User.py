class User:
    def __init__(self, id, name, email, mobile) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.mobile = mobile

    def get_user_id(self):
        return self.id

    def get_user_name(self):
        return self.name

    def set_user_id(self, id):
        self.id = id

    def set_user_name(self, name):
        self.name = name
