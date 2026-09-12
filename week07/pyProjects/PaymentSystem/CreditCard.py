from Payment import Payment


class CreditCard(Payment):

    def __init__(self, customer_name, amount):
        super().__init__(customer_name, amount)

    def make_payment(self):
        print()
        print("========== Credit Card ==========")
        print("Customer :", self.customer_name)
        print("Amount   : $", self.amount)
        print("Payment Method : Credit Card")
        print("Credit Card payment successful.")