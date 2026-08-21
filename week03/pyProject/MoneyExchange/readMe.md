# Money Exchange System

## Project Introduction

This project is a simple Money Exchange System developed by using Python and SQLite3.

The system can store customer information, currencies, exchange rates, and exchange transactions.

This project is developed based on the ER diagram and uses Object-Oriented Programming (OOP) style.

![Image](https://github.com/Richard-Xiahou/MSE800/blob/main/week03/images/Week3-Activity5-Money_Exchange_Project_with_Database_ERD.png?raw=true)

---

## Database Tables

This project contains **4 tables**.

### 1. Customer

The Customer table stores customer information.

It includes:

- Customer ID
- First Name
- Last Name
- Phone Number

This table is necessary because every exchange transaction belongs to one customer.

---

### 2. Currency

The Currency table stores different currencies.

It includes:

- Currency ID
- Currency Code
- Currency Name

This table is necessary because customers can exchange different currencies.

For example:

- NZD
- USD
- CNY

---

### 3. ExchangeRate

The ExchangeRate table stores exchange rates.

It includes:

- Rate ID
- From Currency
- To Currency
- Exchange Rate

This table is necessary because different currencies have different exchange rates.

---

### 4. TransactionHistory

The TransactionHistory table stores exchange transaction records.

It includes:

- Transaction ID
- Customer ID
- From Currency
- To Currency
- Amount
- Exchange Rate

This table is necessary because the business needs to record every exchange transaction.

---

## Python Files

This project contains three Python files.

### database.py

Creates the SQLite database and all tables.

### exchangeManager.py

Inserts sample data and runs SQL queries.

### main.py

Runs the menu and allows users to use the system.

---

## Technologies

- Python 3
- SQLite3
- SQL
- Object-Oriented Programming (OOP)

---

## How to Run

Run the following command:

```bash
python3 main.py
```

Then choose a menu option.

Example:

```

1 Show Total Transactions
2 Show Transaction History
0 Exit
```

---

## Author

Richard Xiahou

MSE800 Week 3 Activity 5
