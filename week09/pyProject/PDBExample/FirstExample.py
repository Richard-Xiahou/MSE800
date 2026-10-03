# This is a simple example to demonstrate the use of the Python Debugger (pdb) module.
# using PDB commands to set breakpoints, step through the code, and inspect variables.
# Essential PDB Commands:
# 1. bp or b (breakpoint): Set a breakpoint at the current line.
# 2. c or continue: Continue execution until the next breakpoint or the end of the program.
# 3. n or next: Execute the next line of code, skipping over any function calls.
# 4. p or print: Print the value of a variable.
# 5. s or step: Execute the next line of code, but stop at the first line of any function calls.

def calculate_total(price, quantity):
    total = price * quantity
    discount = 10
    final_price = total - discount
    return final_price

price = 25
quantity = 3

breakpoint() #input "continue" to continue the program execution

result = calculate_total(price, quantity)
print(result)