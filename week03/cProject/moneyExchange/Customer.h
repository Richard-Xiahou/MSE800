#ifndef CUSTOMER_H
#define CUSTOMER_H

#include <string>

class Customer
{
public:

    int customerId;

    std::string firstName;

    std::string lastName;

    std::string phone;

    Customer()
    {
        customerId = 0;
    }

    Customer(
        int id,
        std::string first,
        std::string last,
        std::string phoneNumber
    )
    {
        customerId = id;
        firstName = first;
        lastName = last;
        phone = phoneNumber;
    }
};

#endif