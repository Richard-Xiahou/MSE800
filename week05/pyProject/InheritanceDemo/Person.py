class Person:
  def __init__(self,
               person_id,
               person_name):
    self.Id = person_id
    self.name = person_name

  def display(self):
    print("Person ID:", self.Id)
    print("Person Name:", self.name)