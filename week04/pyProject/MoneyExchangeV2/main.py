from database import create_tables

from Customer import Customer
from Currency import Currency
from ExchangeRate import ExchangeRate

from ExchangeManager import ExchangeManager


def menu():

    print()
    print("========== Money Exchange System ==========")
    print("1. Add Customer")
    print("2. Show Customers")
    print("3. Add Currency")
    print("4. Show Currencies")
    print("5. Add Exchange Rate")
    print("6. Exchange Currency")
    print("7. Show Transactions")
    print("0. Exit")
    print("-----------------------------------")
    print()


def main():

    create_tables()

    manager = ExchangeManager()

    while True:

        menu()

        choice = input("Choose: ")

        # -----------------------------
        # Add Customer
        # -----------------------------
        if choice == "1":
            customer_id = int(input("Customer ID: "))
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            phone = input("Phone: ")

            customer = Customer(
                customer_id,
                first_name,
                last_name,
                phone
            )

            manager.insert_customer(customer)

        # -----------------------------
        # Show Customers
        # -----------------------------
        elif choice == "2":
            manager.show_customers()

        # -----------------------------
        # Add Currency
        # -----------------------------
        elif choice == "3":
            currency_id = int(input("Currency ID: "))
            currency_code = input("Currency Code: ")
            currency_name = input("Currency Name: ")
            country = input("Country: ")

            currency = Currency(
                currency_id,
                currency_code,
                currency_name,
                country
            )

            manager.insert_currency(currency)

        # -----------------------------
        # Show Currency
        # -----------------------------
        elif choice == "4":
            manager.show_currencies()

        # -----------------------------
        # Add Exchange Rate
        # -----------------------------
        elif choice == "5":
            rate_id = int(input("Rate ID: "))
            from_currency = int(input("From Currency ID: "))
            to_currency = int(input("To Currency ID: "))
            exchange_rate = float(input("Exchange Rate: "))

            rate = ExchangeRate(
                rate_id,
                from_currency,
                to_currency,
                exchange_rate
            )

            manager.insert_exchange_rate(rate)

        # -----------------------------
        # Exchange Currency
        # -----------------------------
        elif choice == "6":
            transaction_id = int(input("Transaction ID: "))
            customer_id = int(input("Customer ID: "))
            from_currency = int(input("From Currency ID: "))
            to_currency = int(input("To Currency ID: "))
            amount = float(input("Amount: "))

            manager.exchange_currency(
                transaction_id,
                customer_id,
                from_currency,
                to_currency,
                amount
            )

        # -----------------------------
        # Show Transactions
        # -----------------------------
        elif choice == "7":
            manager.show_transactions()

        # -----------------------------
        # Exit
        # -----------------------------
        elif choice == "0":
            manager.close()
            print("Thank you for using Money Exchange System.")
            print("Goodbye.")
            break

        else:

            print("Invalid choice.")


if __name__ == "__main__":
    main()