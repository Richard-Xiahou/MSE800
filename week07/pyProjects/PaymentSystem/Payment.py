class Payment:

    def __init__(self, customer_name, amount):
        self.customer_name = customer_name
        self.amount = amount

    def make_payment(self):
        print("Processing payment...")