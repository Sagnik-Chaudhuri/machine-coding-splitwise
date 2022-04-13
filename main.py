from classes.User import User


def main():
    id = "a"
    name = "b"
    user = User(id, name)
    print(user)
    user2 = User(user)
    print(user2)


main()
