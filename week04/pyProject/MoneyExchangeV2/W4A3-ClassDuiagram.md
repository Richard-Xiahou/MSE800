# Money Exchange System

## Week 4 - Activity 3
## Class Diagram for Money Exchange System

### Overview

This project contains one class diagram.
The class diagram shows the software structure of the Money Exchange System.
It explains the classes, their attributes, methods and relationships.

## Class Diagram

![Class Diagram](https://github.com/Richard-Xiahou/MSE800/blob/main/week04/images/W4A3-class_diagram.jpg)

---

## Classes

### Customer

The Customer class stores customer information.

Attributes:

- customer_id
- first_name
- last_name
- phone

Methods:

- get_full_name()
- display()

---

### Currency

The Currency class stores currency information.

Attributes:

- currency_id
- currency_code
- currency_name
- country

Methods:

- get_currency()
- display()

---

### ExchangeRate

The ExchangeRate class stores exchange rate information.

Attributes:

- rate_id
- from_currency
- to_currency
- exchange_rate

Methods:

- get_rate()
- display()

---

### Transaction

The Transaction class stores exchange transaction information.

Attributes:

- transaction_id
- customer_id
- from_currency
- to_currency
- amount
- exchange_rate
- received_amount

Methods:

- calculate_received_amount()
- display()

---

### ExchangeManager

The ExchangeManager class controls the business logic.

It connects to SQLite database.

Functions include:

- insert customer
- insert currency
- insert exchange rate
- exchange currency
- show customers
- show currencies
- show transactions

---

### Database

The database module creates the SQLite database and tables.

---

## Relationships

ExchangeManager communicates with all entity classes.

Customer, Currency, ExchangeRate and Transaction are independent entity classes.

The database module is responsible for creating the database connection.

---

## Conclusion

This class diagram follows Object-Oriented Programming concepts.

Each class has its own responsibility, making the system easier to maintain and extend.

Miro link:

https://miro.com/app/board/uXjVHu6ZOXE=/?share_link_id=294097719198