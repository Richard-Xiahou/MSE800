from Person import Person
from Student import Student
from Staff import Staff
from AcademicStaff import AcademicStaff
from GeneralStaff import GeneralStaff


def menu():

    print()
    print("===================================")
    print(" University Management System")
    print("===================================")
    print("1. Show Person")
    print("2. Show Students")
    print("3. Show Staff")
    print("4. Show Academic Staff")
    print("5. Show General Staff")
    print("6. Exit")
    print()


def main():

    # -----------------------------
    # Create Objects
    # -----------------------------

    person = Person(1, "Mike")

    student1 = Student(2, "Bill")
    student2 = Student(3, "Ye")
    student3 = Student(4, "Freya")

    staff = Staff(5, "600-607-590")
    staff.name = "Lucia"

    academic_staff = AcademicStaff(6, "Cora")
    academic_staff.add_publication("Python for Beginners")
    academic_staff.add_publication("Foundations of Python")

    general_staff = GeneralStaff(7, 100)
    general_staff.name = "Sunny"

    # -----------------------------
    # Menu
    # -----------------------------

    while True:

        menu()

        choice = input("Choose: ")

        print()

        if choice == "1":

            print("Person")
            print("---------------------------")
            person.display()

        elif choice == "2":

            print("Student List")
            print("---------------------------")

            student1.display()
            print()

            student2.display()
            print()

            student3.display()

        elif choice == "3":

            print("Staff")
            print("---------------------------")
            staff.display()

        elif choice == "4":

            print("Academic Staff")
            print("---------------------------")
            academic_staff.display()

            print()
            print("Number of Publications:",
                  len(academic_staff.publications))

        elif choice == "5":

            print("General Staff")
            print("---------------------------")
            general_staff.display()

        elif choice == "6":

            print()
            print("Thank you.")
            print("Program Finished.")
            break

        else:

            print("Invalid choice.")
            print("Please choose again.")


if __name__ == "__main__":
    main()