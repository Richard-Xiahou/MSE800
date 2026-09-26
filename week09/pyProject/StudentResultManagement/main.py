import StudentManager
import Student

def menu():
    manager = StudentManager.StudentManager()
    manager.add_student(Student.Student("1", "Alice", 85))
    manager.add_student(Student.Student("2", "Bob", 75))
    manager.add_student(Student.Student("3", "Charlie", 620))
    manager.add_student(Student.Student("4", "David", 46))
    manager.add_student(Student.Student("5", "Eve", 30))

    while True:
        print("\nStudent Result Management System")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Get Student")
        print("4. List Students")
        print("5. Show Results")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            mark = input("Enter student Mark: ")
            student = Student(student_id, name, mark)
            manager.add_student(student)
            print(f"Student {name} added successfully.")

        elif choice == '2':
            student_id = input("Enter student ID to remove: ")
            manager.remove_student(student_id)
            print(f"Student with ID {student_id} removed successfully.")

        elif choice == '3':
            student_id = input("Enter student ID to get details: ")
            student = manager.get_student(student_id)
            if student:
                print(f"Student ID: {student.student_id}, Name: {student.name}")
            else:
                print(f"No student found with ID {student_id}.")

        elif choice == '4':
            students = manager.list_students()
            if students:
                for s in students:
                    print(f"Student ID: {s.student_id}, Name: {s.name}")
            else:
                print("No students available.")
        elif choice == '5':
            manager.show_results()

        elif choice == '6':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()