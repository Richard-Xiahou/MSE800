from SavingsAccount import SavingsAccount

def menu():

    print()
    print("==============================")
    print(" Bank Account System")
    print("==============================")
    print("1. Display Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Calculate Interest")
    print("5. Display Account Type")
    print("0. Exit")
    print()


def main():

    account = SavingsAccount(
        "SA1001",
        "John",
        5000,
        5
    )

    while True:

        menu()

        choice = input("Choose: ")

        if choice == "1":

            account.display_account()

        elif choice == "2":

            amount = float(input("Deposit Amount: "))
            account.deposit(amount)

        elif choice == "3":

            amount = float(input("Withdraw Amount: "))
            account.withdraw(amount)

        elif choice == "4":

            account.calculate_interest()

        elif choice == "5":

            account.display_account_type()

        elif choice == "0":

            print("Goodbye!")
            break

        else:

            print("Invalid choice.")


if __name__ == "__main__":
    main()