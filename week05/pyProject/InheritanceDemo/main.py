from Person import Person
from Student import Student
from Staff import Staff
from AcademicStaff import AcademicStaff
from GeneralStaff import GeneralStaff

def main():
  person = Person(1,"Mike")

  student = Student(2,"Bill")

  staff = Staff(3,30)
  staff.name = "Lucia"

  academic_staff = AcademicStaff(4, "Cora")
  academic_staff.add_publication("Python for beginners")
  academic_staff.add_publication("Foundations of Python")

  general_staff = GeneralStaff(5, 100)
  general_staff.name = "Sunny"

  person.display()
  print("-----------------------------------")
  student.display()
  print("-----------------------------------")
  staff.display()
  print("-----------------------------------")
  academic_staff.display()
  print("-----------------------------------")
  general_staff.display()
  print("-----------------------------------")



if __name__ == "__main__":
  main()
