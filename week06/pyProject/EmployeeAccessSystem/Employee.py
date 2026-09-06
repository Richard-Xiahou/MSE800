class Employee:

    def __init__(self, employee_id, name, department, salary):

        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary

    def view_salary(self):

        print("---------------------------")
        print("Salary Information")
        print("---------------------------")
        print("Employee :", self.name)
        print("Salary   : $", self.salary)

    def view_personal_details(self):

        print("---------------------------")
        print("Personal Details")
        print("---------------------------")
        print("ID         :", self.employee_id)
        print("Name       :", self.name)
        print("Department :", self.department)

    def download_report(self):

        print("---------------------------")
        print("Employee report downloaded.")