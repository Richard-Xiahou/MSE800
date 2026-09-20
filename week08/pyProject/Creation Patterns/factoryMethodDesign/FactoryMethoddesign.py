# 2.1 Factory Method Design Pattern

# Instead of one Factory deciding everything, we have different Factory subclasses:
#  - Define an interface for creating a factory, but let subclasses decide which class to instantiate.

from abc import ABC, abstractmethod
# ==========================================
# 1. ABSTRACT PRODUCT
#    Defines the common interface for the products
# ==========================================
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# ==========================================
# 2. CONCRETE PRODUCTS
#    The actual products (继承)
# ==========================================
class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

# ==========================================
# 3. ABSTRACT FACTORY / CREATOR
#    Defines the Factory Method
# ==========================================

class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

# ==========================================
# 4. CONCRETE FACTORIES
#    Concrete Factory / Concrete Creator
# ==========================================
# Concrete Factory
class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

# Concrete Factory
class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()

# ==========================================
# 5. CLIENT
# ==========================================
factory = DogFactory()
animal = factory.create_animal()
animal.speak()