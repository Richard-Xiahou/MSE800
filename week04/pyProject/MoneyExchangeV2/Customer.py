class Customer:

    def __init__(self,
                 customer_id,
                 first_name,
                 last_name,
                 phone):

        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone


    def get_full_name(self):

        return self.first_name + " " + self.last_name


    def display(self):

        print("------------------------------")
        print("Customer ID :", self.customer_id)
        print("First Name  :", self.first_name)
        print("Last Name   :", self.last_name)
        print("Phone       :", self.phone)
        print("------------------------------")