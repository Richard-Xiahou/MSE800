# ==========================================
# 1. PRODUCT 
# ==========================================
class Coffee:
    def cost(self):
        return 5

    def description(self):
        return "Coffee"

# ==========================================
# 2. BASE DECORATOR 
# ==========================================
class CoffeeDecorator:
    def __init__ (self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost()

# ==========================================
# 3. CONCRETE DECORATORS 
# ==========================================
class MilkDecorator(CoffeeDecorator):

    def cost(self):
        return self.coffee.cost() + 1

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 0.5

class CreamDecorator(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 0.5

# ==========================================
# 4. CLIENT - CREATE COFFEE 
# ==========================================
'''
coffee = Coffee()
coffee = MilkDecorator(coffee)
coffee = SugarDecorator(coffee)
coffee = CreamDecorator(coffee)
'''

coffee = CreamDecorator(SugarDecorator(MilkDecorator(Coffee())))
print(coffee.cost())