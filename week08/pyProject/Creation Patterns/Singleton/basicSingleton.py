# Singleton Pattern 
# The Singleton Design Pattern is used when you want to make sure that:
# Only one object (one instance) of a class exists throughout the program.


# 1.Without Singleton
# Normally, every time we use ClassName():
# class PrinterManager:
#    pass
#
# p1 = PrinterManager()
# p2 = PrinterManager()
# print(p1 is p2) # We have two different objects.
# Output: False

# Imagine an office has one central printer. You don't want every employee's program to create a completely new printer manager:

# 2.Singleton
# With Singleton, we want:
#
# p1 = PrinterManager()
# p2 = PrinterManager()
# print(p1 is p2)
# Output: True

# ========== Implementation =========
# One common Python approach is to override __new__():
# 使用__new__(cls)方法

class PrinterManager:
    _instance = None # This variable belongs to the class, not to an individual object. there is no object yet

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls) # create an object
        return cls._instance

p1 = PrinterManager()
p2 = PrinterManager()

print(p1 is p2)