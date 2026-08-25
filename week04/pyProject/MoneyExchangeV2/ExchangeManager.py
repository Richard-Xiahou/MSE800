from database import create_connection
from Customer import Customer
from Currency import Currency

class ExchangeManager:

    def __init__(self):
        # 自动连接数据库
        self.connection = create_connection()
        self.cursor = self.connection.cursor()

        print("Database connected.")


    # 保存数据库， 关闭数据库
    def close(self):
        if self.connection:
            self.connection.commit()
            self.connection.close()
            print("Database closed.")
    
    # 检查记录是否存在
    def record_exists(self, table, id_name, id_value):
        sql = f"""
        SELECT *
        FROM {table}
        WHERE {id_name}=?
        """
        self.cursor.execute(sql, (id_value,))
        return self.cursor.fetchone() is not None
    # 创建 Customer 对象
    def insert_customer(self, customer):
        if self.record_exists(
            "Customer",
            "customer_id",
            customer.customer_id
            ):
            print("Customer already exists.")
            return
    
        sql = """
        INSERT INTO Customer
        (customer_id, first_name, last_name, phone)
        VALUES (?, ?, ?, ?)
        """

        self.cursor.execute(
            sql,
            (
                customer.customer_id,
                customer.first_name,
                customer.last_name,
                customer.phone
            )
        )

        self.connection.commit()

        print("Customer added successfully.")
    # 打印 Customer 对象
    def show_customers(self):

        sql = """
        SELECT *
        FROM Customer
        """

        self.cursor.execute(sql)

        customers = self.cursor.fetchall()

        print()
        print("Customer List")
        print("------------------------------")

        for row in customers:

            customer = Customer(
                row[0],
                row[1],
                row[2],
                row[3]
            )

            customer.display()

    # 设置一个新货币
    def insert_currency(self, currency):
        if self.record_exists(
            "Currency",
            "currency_id",
            currency.currency_id
        ):
            print("Currency already exists.")
            return
        
        # 执行插入操作
        sql = """
        INSERT INTO Currency
        (currency_id, currency_code, currency_name, country)
        VALUES (?, ?, ?, ?)
        """
        self.cursor.execute(
            sql,
            (
                currency.currency_id,
                currency.currency_code,
                currency.currency_name,
                currency.country
            )
        )
        self.connection.commit()
        print ("Currency added successfully.")

    # 显示所有货币
    def show_currencies(self):

        sql = """
        SELECT *
        FROM Currency
        """

        self.cursor.execute(sql)
        currencies = self.cursor.fetchall()

        print()
        print("Currency List")
        print("------------------------------")

        for row in currencies:
            currency = Currency(
                row[0],
                row[1],
                row[2],
                row[3]
            )
            currency.display()
   # 插入一个新汇率(如 usd_to_cny)
    def insert_exchange_rate(self, rate):
        if self.record_exists(
            "ExchangeRate",
            "rate_id",
            rate.rate_id
        ):
            print("Exchange Rate already exists.")
            return

        # 执行插入操作
        sql = """
        INSERT INTO ExchangeRate
        (
            rate_id,
            from_currency,
            to_currency,
            exchange_rate
        )
        VALUES (?, ?, ?, ?)
        """

        self.cursor.execute(
            sql,
            (
                rate.rate_id,
                rate.from_currency,
                rate.to_currency,
                rate.exchange_rate
            )
        )

        self.connection.commit()

        print("Exchange rate added successfully.")

    # 汇率转换
    def exchange_currency(
            self,
            transaction_id,
            customer_id,
            from_currency,
            to_currency,
            amount):
        
        # 检查金额是否合法 
        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        # 检查记录是否存在
        if self.record_exists(
            "TransactionHistory",
            "transaction_id",
            transaction_id
        ):
            print("Transaction already exists.")
            return
        # 

        # 查询汇率 Find exchange rate
        sql = """
        SELECT exchange_rate
        FROM ExchangeRate
        WHERE from_currency = ?
        AND to_currency = ?
        """

        self.cursor.execute(
            sql,
            (
                from_currency,
                to_currency
            )
        )

        result = self.cursor.fetchone()

        if result is None:
            print("Exchange rate not found.")
            return

        exchange_rate = result[0]
        #  计算接收金额 Calculate received amount
        received_amount = amount * exchange_rate

        # 插入交易记录
        sql = """
        INSERT INTO TransactionHistory
        (
            transaction_id,
            customer_id,
            from_currency,
            to_currency,
            amount,
            exchange_rate,
            received_amount
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """

        self.cursor.execute(
            sql,
            (
                transaction_id,
                customer_id,
                from_currency,
                to_currency,
                amount,
                exchange_rate,
                received_amount
            )
        )

        self.connection.commit()
        print("Currency exchanged successfully.")

    # 显示所有汇率
    def show_transactions(self):

        sql = """
        SELECT *
        FROM TransactionHistory
        """

        self.cursor.execute(sql)

        transactions = self.cursor.fetchall()

        print()
        print("Transaction History")
        print("-----------------------------------")

        for transaction in transactions:

            print("Transaction ID :", transaction[0])
            print("Customer ID    :", transaction[1])
            print("From Currency  :", transaction[2])
            print("To Currency    :", transaction[3])
            print("Amount         :", transaction[4])
            print("Rate           :", transaction[5])
            print("Received       :", transaction[6])

            print("-----------------------------------")