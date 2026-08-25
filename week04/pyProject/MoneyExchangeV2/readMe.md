# Money Exchange System

## Introduction

This is a simple Money Exchange System developed with Python and SQLite3.

The project is created for Week 3 Activity 5 and Week 4 UML activities.

The system allows users to:

- Manage customers
- Manage currencies
- Manage exchange rates
- Exchange currency
- Save transaction history

---

# Project Structure
MoneyExchange/
│
├── database.py
├── Customer.py
├── Currency.py
├── ExchangeRate.py
├── Transaction.py
├── ExchangeManager.py
├── main.py
├── README.md
├── W4A3-ClassDiagram.md
│
../../images/
      └── W4A3-class_diagram.jpg

    
# Classes

| File | Description |
|------|-------------|
| database.py | Create database and tables |
| Customer.py | Customer class |
| Currency.py | Currency class |
| ExchangeRate.py | Exchange rate class |
| Transaction.py | Transaction class |
| ExchangeManager.py | Business logic |
| main.py | Program entry |

# Database Tables
The project contains four tables.
## Customer
Stores customer information.
## Currency
Stores supported currencies.
## ExchangeRate
Stores exchange rates between currencies.
## TransactionHistory
Stores all exchange transactions.

# Features
- Add customer
- Show customer list
- Add currency
- Show currency list
- Add exchange rate
- Exchange currency
- Save transaction history
- Show transaction history

# Object-Oriented Design
The project uses Object-Oriented Programming.
Each entity has its own class.
Business logic is separated into ExchangeManager.
SQLite database operations are also separated.

# UML
The project includes one UML Class Diagram.
See:
w4A1-UserCase.md
W4A2-ActivityDiagram.md
W4A3-ClassDiagram.md

# Requirements
- Python 3
- SQLite3

# Run
```
python3 main.py
```