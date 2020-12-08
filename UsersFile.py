class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


class Users:
    def __init__(self):
        self.Users = []

    def add_user(self, user):
        if type(user) == User:
            self.Users.append(user)
            print("USER HAS BEEN ADDED")
            return True
        else:
            print("[ERROR] Object is not type 'User'")
            return False


SignedUpUsers = Users()