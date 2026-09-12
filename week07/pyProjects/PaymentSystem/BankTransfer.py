from Payment import Payment


class BankTransfer(Payment):

    def __init__(self, customer_name, amount):
        super().__init__(customer_name, amount)

    def make_payment(self):
        print()
        print("========== Bank Transfer ==========")
        print("Customer :", self.customer_name)
        print("Amount   : $", self.amount)
        print("Payment Method : Bank Transfer")
        print("Bank transfer successful.")