from abc import ABC, abstractmethod


# ============================
# Abstract Class
# ============================

class ATM(ABC):

    @abstractmethod
    def insert_card(self):
        pass

    @abstractmethod
    def enter_pin(self):
        pass

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


# ============================
# Child Class
# ============================

class BankATM(ATM):

    def __init__(self):

        self.balance = 5000
        self.correct_pin = "1234"
        self.logged_in = False

    def insert_card(self):
        print("Card inserted successfully.")

    def enter_pin(self):

        pin = input("Enter PIN: ")

        if pin == self.correct_pin:

            self.logged_in = True
            print("PIN verified.")

        else:

            print("Incorrect PIN.")

    def check_balance(self):

        if self.logged_in:

            print("Current Balance : $", self.balance)

        else:

            print("Please enter your PIN first.")

    def withdraw(self, amount):

        if not self.logged_in:

            print("Please enter your PIN first.")
            return

        if amount > self.balance:

            print("Insufficient balance.")

        else:

            self.balance -= amount
            print("$", amount, "withdrawn successfully.")
            print("Remaining Balance :", self.balance)


# ============================
# CLI Menu
# ============================

def menu():

    print()
    print("==============================")
    print(" ATM System")
    print("==============================")
    print("1. Insert Card")
    print("2. Enter PIN")
    print("3. Check Balance")
    print("4. Withdraw Money")
    print("0. Exit")
    print()


# ============================
# Main Function
# ============================

def main():

    atm = BankATM()

    while True:

        menu()

        choice = input("Choose: ")

        if choice == "1":

            atm.insert_card()

        elif choice == "2":

            atm.enter_pin()

        elif choice == "3":

            atm.check_balance()

        elif choice == "4":

            amount = float(input("Withdraw Amount: "))
            atm.withdraw(amount)

        elif choice == "0":

            print("Thank you for using our ATM.")
            break

        else:

            print("Invalid choice.")


if __name__ == "__main__":
    main()