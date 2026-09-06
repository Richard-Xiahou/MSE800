class LoginManager:

    def __init__(self):

        self.logged_in = False

    def login(self):

        username = input("Username: ")
        password = input("Password: ")

        if username == "admin" and password == "1234":

            self.logged_in = True

            print("Login successful.")

        else:

            print("Invalid username or password.")

    def logout(self):

        self.logged_in = False

        print("Logged out.")