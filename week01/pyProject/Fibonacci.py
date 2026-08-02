# -*- coding: utf-8 -*-

def print_fibonacci_up_to(n):
    """Function 1: Print all Fibonacci numbers less than or equal to N."""
    print "Fibonacci series up to {}:".format(n)
    a, b = 0, 1
    # 只要当前的斐波那契数不超过 n，就继续打印
    while a <= n:
        print a,
        a, b = b, a + b
    print ""  # 打印完毕后换行


def calculate_factorial(n):
    """Function 2: Calculates and returns the factorial of N. (Factorial)"""
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def main():
    # convert to integers
    user_input = raw_input("Please enter a number (N): ")
    n = int(user_input)
    
    print "-" * 30
    
    # 1. print fibonacci series
    print_fibonacci_up_to(n)
    
    # 2. Call the function to calculate the factorial, and print the result.
    factorial_res = calculate_factorial(n)
    print "Factorial of {} is: {}".format(n, factorial_res)
    
    print "-" * 30


if __name__ == "__main__":
    main()