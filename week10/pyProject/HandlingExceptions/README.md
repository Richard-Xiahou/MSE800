# Catch Exceptions 捕捉异常
Exception handling

## 1. try and except
```
  try:
    10 * (1/0)
  except:
    print("The calculation failed")
```

```
  try:
    x = int(input("Enter a number: "))
    print(10 / x)
  except ValueError:
    print("An error occurred!")
```

## 2.Handling Specific Exceptions
```
  try:
    a = int("abc")
  except ValueError:
    print("Conversion failed!")
```

```
  try:
    days = int(input("Rental days: "))
    print("Total:", days * 60)
  except ValueError:
    print("Please enter a whole number.")
 
  print("Program continues...")
```

## Several except blocks / Multiple Exceptions
```
  try:
    value = int(text)
    result = 100 / value
  except ValueError:
    print("Not a number")
  except ZeroDivisionError:
    print("Cannot divide by zero")
```

  to handle serveral exceptions in the same way, group them in a tuple:
  
  ```
  try:
    age = int(input("Enter your age: "))
    result = 100 / age
  except (ValueError, TypeError):
    print("Invalid input")
```

## 2. Getting the exception object
try:
  ...
except KeyError as e:
  print("type", type(e).__nsme__)
  print("detail", e)

## else and final
  try -> starts
  except  -> the exceptions you given
  else ->  another exceptions you not given
  final -> both condition will excute this part

```
  try:
    my_function(6, 2)
  except ZeroDivisionError as e:
    print(e)
  else:
    print('Everything worked OK')
```

```
  try:
    print(10 / 2)
  except ZeroDivisionError:
    print("zero")
  else:
    print("ok")
  finally:
    print("done")
```

5.0
ok
done

## finally and the with statement
```
  def read_first_line(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.readline().strip()
    except FileNotFoundError:
        print(f"File not found: {path}")
    except PermissionError:
        print(f"No permission to read: {path}")
    return None
```
The file is closed automatically when the with block ends, even when an exception is raised inside it.