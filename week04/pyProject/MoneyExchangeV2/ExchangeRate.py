class ExchangeRate:

    def __init__(self,
                 rate_id,
                 from_currency,
                 to_currency,
                 exchange_rate):

        self.rate_id = rate_id
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.exchange_rate = exchange_rate


    def get_rate(self):
        return self.exchange_rate


    def display(self):

        print("------------------------------")
        print("Rate ID        :", self.rate_id)
        print("From Currency  :", self.from_currency)
        print("To Currency    :", self.to_currency)
        print("Exchange Rate  :", self.exchange_rate)
        print("------------------------------")