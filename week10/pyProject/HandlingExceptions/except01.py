text = "abc"
value = 10;

value = int(text)  # This will raise a ValueError because "abc" cannot be converted to an integer

try:
  value = int(text)
  result = 100 / value
except ValueError:
  print("ValueError: Cannot convert text to an integer.")
except ZeroDivisionError:
  print("ZeroDivisionError: Division by zero is not allowed.")