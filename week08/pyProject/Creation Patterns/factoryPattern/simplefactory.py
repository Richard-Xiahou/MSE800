
# 1.1.Simple Factory Design Pattern
# Imagine you have an online payment system.
# A customer can pay using:
#  - Credit Card 
#  - PayPal 
#  - Bank Transfer 
# Without the Factory pattern, you might write:

# payment_type = "paypal"

# if payment_type == "credit_card":
#    payment = CreditCard()
# elif payment_type == "paypal":
#    payment = PayPal()
# elif payment_type == "bank":
#    payment = BankTransfer()

# payment.pay()

#-The problem is that the code that uses the payment also has to know how to create each payment object.
# The Factory pattern moves this object-creation logic into a separate place.
# Example I
# Step 1: Create the classes
# Step 2: Create the Factory
# Step 3: Use the Factory

# Step 1: Create the classes
# Each class has its own pay() method.

class CreditCard:
    def pay(self):
        print("Payment made using Credit Card")

class PayPal:
    def pay(self):
        print("Payment made using PayPal")

class BankTransfer:
    def pay(self):
        print("Payment made using Bank Transfer")

# Step 2: Create the Factory
# The Factory's job is to create the appropriate object.

class PaymentFactory:

    @staticmethod
    def create_payment(payment_type):
        if payment_type == "credit_card":
            return CreditCard()

        elif payment_type == "paypal":
            return PayPal()

        elif payment_type == "bank":
            return BankTransfer()

        else:
            raise ValueError("Invalid payment type")

#Step 3: Use the Factory
payment = PaymentFactory.create_payment("paypal")
payment.pay()
