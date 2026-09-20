class Target:
    def request(self):
        pass

class Adaptee:
    def specific_request(self):
        print("Adaptee: specific request")

class Adapter(Target, Adaptee):

    def request(self):
        self.specific_request()

adapter = Adapter()
adapter.request() 