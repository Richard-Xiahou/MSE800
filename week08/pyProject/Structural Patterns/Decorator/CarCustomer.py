# ==========================================
# 1. PRODUCT 
# ==========================================
class Car:
    def cost(self):
        return 25000

    def description(self):
        return "Car"

# ==========================================
# 2. BASE DECORATOR 
# ==========================================
class CarDecorator:
    def __init__ (self, car):
        self.car = car

    def cost(self):
        return self.car.cost()

# ==========================================
# 3. CONCRETE DECORATORS 
# ==========================================
class GPSDecorator(CarDecorator):

    def cost(self):
        return self.car.cost() + 500

class SunroofDecorator(CarDecorator):
    def cost(self):
        return self.car.cost() + 1000

class LeatherSeatsDecorator(CarDecorator):
    def cost(self):
        return self.car.cost() + 1500

class PremiumSoundDecorator(CarDecorator):
    def cost(self):
        return self.car.cost() + 800

# ==========================================
# 4. CLIENT - CREATE CAR 
# ==========================================

car = Car()
car = GPSDecorator(car)
car = SunroofDecorator(car)
car = LeatherSeatsDecorator(car)
car = PremiumSoundDecorator(car)

# OR 
car2  = PremiumSoundDecorator(LeatherSeatsDecorator(SunroofDecorator(GPSDecorator(Car()))))



print(car.cost())
print(car2.cost())