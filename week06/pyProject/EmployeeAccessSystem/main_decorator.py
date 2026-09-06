# ===============================
# Employee Access Management System
# Week 6 - Decorator Example
# 这个文件是练习 装饰器 的完整版本
# ===============================

# Login status
logged_in = False


# -------------------------------
# Decorator
# -------------------------------
def login_required(func):

    def wrapper():

        if logged_in:
            func()
        else:
            print("Access Denied! Please log in first.")

    return wrapper


# -------------------------------
# Employee Functions
# -------------------------------

@login_required
def view_salary():
    print("Salary: $6,500 per month")


@login_required
def view_personal_details():
    print("Name : Richard")
    print("Department : IT")
    print("Position : Software Developer")


@login_required
def download_report():
    print("Employee report downloaded successfully.")


# -------------------------------
# Login Function
# -------------------------------

def login():

    global logged_in

    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "1234":
        logged_in = True
        print("Login successful.")
    else:
        print("Invalid username or password.")


# -------------------------------
# Logout
# -------------------------------

def logout():

    global logged_in

    logged_in = False

    print("Logged out.")


# -------------------------------
# Menu
# -------------------------------

def menu():

    print()
    print("==============================")
    print(" Employee Access System ")
    print("==============================")
    print("1. Login")
    print("2. View Salary")
    print("3. View Personal Details")
    print("4. Download Report")
    print("5. Logout")
    print("0. Exit")
    print()


# -------------------------------
# Main
# -------------------------------

def main():

    while True:

        menu()

        choice = input("Choose: ")

        if choice == "1":

            login()

        elif choice == "2":

            view_salary()

        elif choice == "3":

            view_personal_details()

        elif choice == "4":

            download_report()

        elif choice == "5":

            logout()

        elif choice == "0":

            print("Goodbye!")
            break

        else:

            print("Invalid choice.")


if __name__ == "__main__":
    main()