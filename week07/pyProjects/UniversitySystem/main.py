# =====================================
# Department Class
# =====================================

class Department:

    def __init__(self, department_name, head):

        self.department_name = department_name
        self.head = head

    def show_department(self):

        print("Department Name :", self.department_name)
        print("Head of Department :", self.head)


# =====================================
# University Class
# =====================================

class University:

    def __init__(self, university_name, department_name, head):

        self.university_name = university_name

        # Composition
        self.department = Department(department_name, head)

    def show_university(self):

        print()
        print("==============================")
        print("University Information")
        print("==============================")

        print("University :", self.university_name)

        self.department.show_department()


# =====================================
# CLI Menu
# =====================================

def menu():

    print()
    print("==============================")
    print(" University System")
    print("==============================")
    print("1. Create University")
    print("2. Display Information")
    print("0. Exit")
    print()


# =====================================
# Main Function
# =====================================

def main():

    university = None

    while True:

        menu()

        choice = input("Choose: ")

        if choice == "1":

            university_name = input("University Name: ")
            department_name = input("Department Name: ")
            head = input("Head of Department: ")

            university = University(
                university_name,
                department_name,
                head
            )

            print("University created successfully.")

        elif choice == "2":

            if university is None:

                print("Please create a university first.")

            else:

                university.show_university()

        elif choice == "0":

            print("Goodbye!")
            break

        else:

            print("Invalid choice.")


if __name__ == "__main__":
    main()