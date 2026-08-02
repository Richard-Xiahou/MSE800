#include <iostream>
#include <iomanip>

int main() {
    double hours_worked, hourly_pay_rate, gross_pay;

    // 1. Input (输入)
    std::cout << "Please input (Hours worked): ";
    std::cin >> hours_worked;
    std::cout << "Please input (Hourly pay rate): ";
    std::cin >> hourly_pay_rate;

    // 2. Process (处理)
    gross_pay = hours_worked * hourly_pay_rate;

    // 3. Output (输出)
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "Gross pay is: $" << gross_pay << std::endl;

    return 0;
}