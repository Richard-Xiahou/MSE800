# Money Exchange System

## Class Diagram

![Class Diagram](https://github.com/Richard-Xiahou/MSE800/blob/main/week03/images/W4A3-class_diagram.jpg)

This class diagram shows the main classes used in the Money Exchange System.

The system contains four classes:

- Customer
- Currency
- ExchangeRate
- Transaction

The **Customer** class stores customer information.

The **Currency** class stores supported currencies.

The **ExchangeRate** class stores the exchange rate between two currencies.

The **Transaction** class records each money exchange transaction.

The relationships between the classes show how the system works. One customer can make many transactions. Each transaction uses two currencies (from currency and to currency). The exchange rate is used to calculate the exchanged amount.

Miro link:

https://miro.com/app/board/uXjVHu6ZOXE=/?share_link_id=294097719198