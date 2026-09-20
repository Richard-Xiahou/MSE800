# Target
class Target:
    def request(self):
        pass
# Adaptee
class Adaptee:
    def specific_request(self):
        print("Adaptee: specific request")
# Adapter
class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        self.adaptee.specific_request()
# Client

# Composition-based Adapter
adaptee = Adaptee() 
adapter = Adapter(adaptee) # Adapter contains/has an Adaptee
adapter.request()

# composition of adapters
req = Adapter(Adapter(adaptee)).request()