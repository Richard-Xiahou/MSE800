from BankAccount import BankAccount


class SavingsAccount(BankAccount):

    def __init__(self,
                 account_number,
                 customer_name,
                 balance,
                 interest_rate):

        super().__init__(
            account_number,
            customer_name,
            balance
        )

        self.interest_rate = interest_rate

    # Display account type
    def display_account_type(self):

        print("Account Type : Savings Account")

    # Calculate interest
    def calculate_interest(self):

        interest = self.balance * self.interest_rate / 100

        print()
        print("Interest Rate :", self.interest_rate, "%")
        print("Interest      : $", interest)

        return interest