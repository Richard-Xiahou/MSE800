from Staff import Staff

class AcademicStaff(Staff):
  def __init__(self, staff_id,staff_name):
    self.Id = staff_id
    self.name = staff_name
    self.publications = []

  def add_publication(self, publication):
    self.publications.append(publication)

  def display(self):
    print("Staff ID:", self.Id)
    print("Staff Name:", self.name)
    print("Publications:",self.publications)