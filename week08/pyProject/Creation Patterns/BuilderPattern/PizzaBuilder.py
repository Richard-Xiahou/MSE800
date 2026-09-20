class Pizza:
    def __init__(self, size, crust, cheese, toppings, sauce):
        self.size =size
        self.crust=crust
        self.cheese=cheese
        self.toppings=toppings
        self.sauce=sauce

    def show_pizza(self):
        print("Size: ", self.size)
        print("Crust: ", self.crust)
        print("Cheese: ", self.cheese)
        print("Toppings: ", self.toppings)
        print("Sauce: ", self.sauce)

class PizzaBuilder:
    def __init__(self):
        self.size = None
        self.crust= None
        self.cheese= None
        self.toppings= []
        self.sauce= None

    def set_size(self, size):
        self.size = size
        return self

    def set_crust(self, crust):
        self.crust = crust
        return self

    def add_cheese(self, cheese):
        self.cheese = cheese
        return self

    def add_toppings(self, toppings):
        self.toppings = toppings
        return self

    def set_sauce(self, sauce):
        self.sauce = sauce
        return self

    def build(self):
         return Pizza(
            self.size,
            self.crust,
            self.cheese,
            self.toppings,
            self.sauce
         )
pizza = (
    PizzaBuilder()
    .set_size("Large")
    .set_crust("Thin")
    .add_cheese("Smoked")
    .add_toppings("Mushroom")
    .set_sauce("BBQ")
    .build())

pizza.show_pizza()