def login_required(func):

    def wrapper(self, *args, **kwargs):

        if self.login_manager.logged_in:

            return func(self, *args, **kwargs)

        else:

            print()
            print("Access Denied!")
            print("Please login first.")
            print()

    return wrapper