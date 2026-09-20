
class ProductA:
  def __init__(self):
    print("this is productA")

class ProductB:
  def __init__(self):
    print("this is productB")


# Factory class
class Factory:
  def create(self, choice):
    if(choice == "A"):
      return ProductA();
    else:
      return ProductA();

# client

factory = Factory();
p_a = factory.create("A")
p_b = factory.create("B")