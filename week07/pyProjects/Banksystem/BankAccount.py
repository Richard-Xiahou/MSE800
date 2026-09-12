class BankAccount:

    def __init__(self, account_number, customer_name, balance):

        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    # Display account information
    def display_account(self):

        print()
        print("========== Account ==========")
        print("Account Number :", self.account_number)
        print("Customer Name  :", self.customer_name)
        print("Balance        : $", self.balance)

    # Deposit money
    def deposit(self, amount):

        if amount <= 0:
            print("Invalid amount.")
            return

        self.balance += amount

        print("Deposit successful.")
        print("Current Balance : $", self.balance)

    # Withdraw money
    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid amount.")
            return

        if amount > self.balance:

            print("Insufficient balance.")

        else:

            self.balance -= amount

            print("Withdraw successful.")
            print("Current Balance : $", self.balance)