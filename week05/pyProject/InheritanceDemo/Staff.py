from Person import Person

class Staff(Person):
  def __init__(self, staff_id,tax_num):
    self.Id = staff_id
    self.tax_num = tax_num

  def display(self):
    print("Staff ID: ", self.Id)
    print("Staff tax_num: ", self.tax_num)