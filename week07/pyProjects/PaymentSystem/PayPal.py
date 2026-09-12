from Payment import Payment


class PayPal(Payment):

    def __init__(self, customer_name, amount):
        super().__init__(customer_name, amount)

    def make_payment(self):
        print()
        print("========== PayPal ==========")
        print("Customer :", self.customer_name)
        print("Amount   : $", self.amount)
        print("Payment Method : PayPal")
        print("PayPal payment successful.")