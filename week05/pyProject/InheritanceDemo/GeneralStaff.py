from Staff import Staff

class GeneralStaff(Staff):
  def __init__(self, staff_id,rete_of_pay):
    self.Id = staff_id
    self.rete_of_pay = rete_of_pay

  def display(self):
    print("General staff name: ", self.name)
    print("General staff rete_of_pay: ", self.rete_of_pay)