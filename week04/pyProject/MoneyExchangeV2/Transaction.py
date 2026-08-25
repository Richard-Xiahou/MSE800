class Transaction:

    def __init__(self,
                 transaction_id,
                 customer_id,
                 from_currency,
                 to_currency,
                 amount,
                 exchange_rate,
                 received_amount):

        self.transaction_id = transaction_id
        self.customer_id = customer_id
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.amount = amount
        self.exchange_rate = exchange_rate
        self.received_amount = received_amount


    def calculate_received_amount(self):

        self.received_amount = self.amount * self.exchange_rate

        return self.received_amount


    def display(self):

        print("------------------------------")
        print("Transaction ID :", self.transaction_id)
        print("Customer ID    :", self.customer_id)
        print("From Currency  :", self.from_currency)
        print("To Currency    :", self.to_currency)
        print("Amount         :", self.amount)
        print("Exchange Rate  :", self.exchange_rate)
        print("Receive Amount :", self.received_amount)
        print("------------------------------")