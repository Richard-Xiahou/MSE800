from Employee import Employee
from LoginManager import LoginManager
from decorators import login_required


class EmployeeSystem:

    def __init__(self):

        self.login_manager = LoginManager()

        self.employee = Employee(
            1001,
            "Richard",
            "Software Engineering",
            6500
        )

    @login_required
    def view_salary(self):

        self.employee.view_salary()

    @login_required
    def view_personal_details(self):

        self.employee.view_personal_details()

    @login_required
    def download_report(self):

        self.employee.download_report()

    def menu(self):

        while True:

            print()
            print("==============================")
            print(" Employee Access System")
            print("==============================")
            print("1. Login")
            #username: admin, password: 1234
            print("2. View Salary")
            print("3. View Personal Details")
            print("4. Download Report")
            print("5. Logout")
            print("0. Exit")
            print()

            choice = input("Choose: ")

            if choice == "1":

                self.login_manager.login()

            elif choice == "2":

                self.view_salary()

            elif choice == "3":

                self.view_personal_details()

            elif choice == "4":

                self.download_report()

            elif choice == "5":

                self.login_manager.logout()

            elif choice == "0":

                print("Goodbye!")

                break

            else:

                print("Invalid choice.")


def main():

    system = EmployeeSystem()

    system.menu()


if __name__ == "__main__":

    main()