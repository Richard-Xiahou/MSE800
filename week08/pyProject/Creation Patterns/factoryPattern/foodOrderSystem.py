# 1.1 Simple Factory Design Pattern

class Pizza:
  def __init__(self):
    print("preparing Pizza")

class Burger:
  def __init__(self):
    print("preparing Burger")

class Pasta:
  def __init__(self):
    print("preparing Pasta")


# Factory class
class FoodFactory:
  def order(self, choice):
    if (choice == "pizza"):
      return Pizza()
    if (choice == "burger"):
      return Burger();
    else:
      return Pasta();

# client

factory = FoodFactory();
food_a = factory.order("pizza")
food_b = factory.order("burger")
food_c = factory.order("pasta")