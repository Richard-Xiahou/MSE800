from CreditCard import CreditCard
from PayPal import PayPal
from BankTransfer import BankTransfer


def menu():

    print()
    print("================================")
    print(" Payment System")
    print("================================")
    print("1. Credit Card")
    print("2. PayPal")
    print("3. Bank Transfer")
    print("0. Exit")
    print()


def main():

    while True:

        menu()

        choice = input("Choose: ")

        if choice == "0":
            print("Goodbye!")
            break

        name = input("Customer Name: ")
        amount = float(input("Amount: "))

        if choice == "1":
            payment = CreditCard(name, amount)

        elif choice == "2":
            payment = PayPal(name, amount)

        elif choice == "3":
            payment = BankTransfer(name, amount)

        else:
            print("Invalid choice.")
            continue

        payment.make_payment()


if __name__ == "__main__":
    main()