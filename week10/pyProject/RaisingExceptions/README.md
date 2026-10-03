Raise Error 引发/抛出异常

## 3.1 raise
Your own code should raise an exception when it receives something it cannot accept. This is called failing early: the caller learns about the problem immediately instead of getting a wrong result later.

### The syntax of this is 
raise <Exception/Error type to raise>()

···
  def function_bang():
    print('function_bang in')
  raise ValueError('Bang!')
    print('function_bang')
···

In the above function the second statement in the function body will create a new instance of the ValueError class and then raise it so that it is thrown allowing it to be caught by any exception handlers that have been defined. We can handle this exception by writing a try block with an except clause for the ValueError class. 
For example:

···
  try:
    function_bang()
  except ValueError as ve:
    print(ve)

  age = -5
  if age < 0:
    raise ValueError("Age cannot be negative")
···

···
  def set_daily_rate(rate):
    if rate <= 0:
        raise ValueError("Daily rate must be greater than zero")
    return rate

  daily_rate = set_daily_rate(-50)
  print(daily_rate)
···

···
  def calculate_discount(price):
    if price < 0:
        raise ValueError("Price cannot be negative")

    if price == 0:
        raise ValueError("Price cannot be zero")

    discount = price * 0.10
    return discount


  try:
    price = float(input("Enter the price: "))

    discount = calculate_discount(price)

    print("Discount:", discount)
    print("Final price:", price - discount)

  except ValueError as e:
    print("Error type:", type(e).__name__)
    print("Error message:", e)
···

## 3.2 Re-raising and chaining
Sometimes you want to handle an exception partly (for example log it) and let it continue upwards: use a bare raise. To translate a low-level error into a domain error without losing the original cause, use raise ... from:
Re-raising means: “I caught the error here, but I want the calling function to deal with it.”

···
  def function_a():
    function_b()


  def function_b():
    try:
      x = 10 / 0
    except ZeroDivisionError:
      print("Error found in function_b")
      raise
  function_a()
···

Chaining: "I got a ValueError, but I'll turn it into a BookingError. However, remember that the BookingError was caused by the original ValueError."

···
  class BookingError(Exception):
    """Base class for all booking problems."""
 
  def load_rate(text):
    try:
      return float(text)
    except ValueError as e:
      raise BookingError(f"Invalid daily rate: {text!r}") from e #from connects the new error to the original error.
··
The original ValueError is kept in the __cause__ attribute and shown in the traceback, which makes debugging much easier.