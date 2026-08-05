#include <iostream>

int main() {
    long long a = 0;
    long long b = 1;

    std::cout << "Fibonacci sequence (10 iterations):" << std::endl;

    // 迭代 10 次
    for (int i = 0; i < 10; ++i) {
        std::cout << a << " ";
        long long next = a + b;
        a = b;
        b = next;
    }

    std::cout << std::endl;
    return 0;
}