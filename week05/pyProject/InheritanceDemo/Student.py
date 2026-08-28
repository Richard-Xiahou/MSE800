from Person import Person

class Student(Person):
  def __init__(self, student_id, student_name):
    self.Id = student_id
    self.name = student_name

  def display(self):
    print("Student ID: ", self.Id)
    print("Student Name: ", self.name)