text = "abc"
value = 10;

value = int(text)  # This will raise a ValueError because "abc" cannot be converted to an integer

try:
  value = int(text)
  result = 100 / value
# to handle multiple exceptions in a single except block, you can use a tuple of exception types. 
# tuple 元组
except *(ValueError, ZeroDivisionError) as e:
  print(f"An error occurred: {e}")