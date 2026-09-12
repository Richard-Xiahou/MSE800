class Payment:
  def make_payment(self):
    print("Making payment")

class example:
  pass

class CreditCard(Payment):
  def make_payment(self):
    print("Making payment using credit card")


class Payple(Payment):
  def make_payment(self):
    print("Making payment using Payple")


class BankTransfer(Payment):
  def make_payment(self):
    print("Making payment using bank transfer")


def main():
  payment = Payment();
  CreditCard = CreditCard();
  payple = Payple();
  bankTransfer = BankTransfer();


if __name__ == "__main__":
  main()
