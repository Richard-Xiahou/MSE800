# 3. Abstract Factory Pattern
# -Factory Method creates one type of product.
# -Abstract Factory creates a family of related products.

from abc import ABC, abstractmethod
#abstract products
class Chair(ABC):
    @abstractmethod
    def sit(self):
        pass

class Sofa(ABC):
    @abstractmethod
    def relax(self):
        pass

#Concrete Products — Modern family
class ModernChair(Chair):
    def sit(self):
        print( "Sitting on Modern Chair ")
class ModernSofa(Sofa):
    def relax(self):
        print( "Relaxing on Modern Sofa ")
#Concrete Products — Victorian family
class VictorianChair(Chair):
    def sit(self):
        print( "Sitting on Victorian Chair ")
class VictorianSofa(Sofa):
    def relax(self):
        print( "Relaxing on Victorian Sofa ")
# Abstract Factory
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass
    @abstractmethod
    def create_sofa(self):
        pass

#Concrete Factories
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()
    def create_sofa(self):
        return ModernSofa()
class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return VictorianChair()
    def create_sofa(self):
        return VictorianSofa()

#Client
factory = ModernFurnitureFactory()
chair = factory.create_chair()
sofa = factory.create_sofa()

chair.sit()
sofa.relax()

#  =========================== relationship =================================
#
#                 FurnitureFactory (Abstract Factory)
#                                  │
#               ┌──────────────────┴─────────────────┐
#               ↓                                    ↓
#         ModernFurnitureFactory                VictorianFurnitureFactory
#           (Concrete Factory)                 (Concrete Factory)
#               │                                    │
#               ├── ModernChair (Product)            ├── VictorianChair (Product)
#               │                                    │
#               └── ModernSofa (Product)             └── VictorianSofa (Product)