class Observer:
    def update(self, temperature):
        pass
# Concrete Observer
class Person(Observer):
    def __init__(self, name):
        self.name = name
    def update(self, temperature):
        print(self.name, "knows temperature is", temperature)
# Subject
class WeatherStation:
    def __init__(self):
        self.observers = []
    def add_observer(self, observer):
        self.observers.append(observer)

    def notify(self, temperature):
        for observer in self.observers:
            observer.update(temperature)
# Create observers
person1 = Person("Ali")
person2 = Person("Sara")
# Create subject
weather = WeatherStation()
# Subscribe people
weather.add_observer(person1)
weather.add_observer(person2)

# Temperature changes
weather.notify(25)
