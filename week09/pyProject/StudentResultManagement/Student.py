class Student:
    def __init__(self, student_id, name, mark):
        self.student_id = student_id
        self.name = name
        self.mark = mark

    def calculate_pass_status(self):
        return self.mark >= 50

    def display_result(self):
        print(f"ID: {self.student_id}", f"Name: {self.name}", f"Mark: {self.mark}", f"ispass: {self.mark >= 50}")