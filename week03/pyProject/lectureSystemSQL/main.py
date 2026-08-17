from database import create_tables
from userManager import insert_sample_data
from userManager import show_student_count
from userManager import show_students_more_than_one_course


def menu():
    print("==============================")
    print(" Lecture System (SQLite3)")
    print("==============================")
    print()

def main():
    menu()
    # Create database tables
    create_tables()
    # Insert sample data
    insert_sample_data()
    # Question 1
    show_student_count()
    # Question 2
    show_students_more_than_one_course()


if __name__ == "__main__":
    main()