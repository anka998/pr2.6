class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
users = [
    User("user1", "password1"),
    User("user2", "password2"),
    User("user3", "password3"),
    User("user4", "password4"),
    User("user5", "password5")
]
search_login = "user2"
search_password = "password2"

found_user = None
for user in users:
    if user.login == search_login and user.password == search_password:
        found_user = user
        break
if found_user:
    print(found_user.login)
    print(found_user.password)
else:
    print("Not found")