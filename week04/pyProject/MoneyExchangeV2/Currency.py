class Currency:

    def __init__(self,
                 currency_id,
                 currency_code,
                 currency_name,
                 country):

        self.currency_id = currency_id
        self.currency_code = currency_code
        self.currency_name = currency_name
        self.country = country


    def get_currency(self):

        return self.currency_code + " - " + self.currency_name


    def display(self):

        print("------------------------------")
        print("Currency ID   :", self.currency_id)
        print("Currency Code :", self.currency_code)
        print("Currency Name :", self.currency_name)
        print("Country       :", self.country)
        print("------------------------------")