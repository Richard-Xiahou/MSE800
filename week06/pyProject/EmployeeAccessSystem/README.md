# Employee Access Management System

## Overview

This project demonstrates the use of Python Function Decorators together with Object-Oriented Programming (OOP).

The system simulates a simple employee management system. Only logged-in employees are allowed to access protected functions.

The project was developed for the Week 6 Decorator activity.

---

# Project Structure

```
EmployeeAccessSystem/

├── Employee.py
├── LoginManager.py
├── decorators.py
├── main.py
└── README.md
```

---

# Features

The system provides the following functions:

- Login
- Logout
- View Salary
- View Personal Details
- Download Employee Report

All protected functions use the same decorator.

---

# Decorator

The project uses one function decorator.

```python
@login_required
```

The decorator checks whether the employee has logged in before executing the function.

If the employee is not logged in, the system displays:

```
Access Denied!
Please login first.
```

The original function will not be executed.

---

# OOP Design

The project contains three main classes.

### Employee

Stores employee information.

Attributes:

- employee_id
- name
- department
- salary

Methods:

- view_salary()
- view_personal_details()
- download_report()

---

### LoginManager

Manages login status.

Methods:

- login()
- logout()

---

### EmployeeSystem

Provides the menu and connects all classes together.

---

# Why Use a Decorator?

Without a decorator, every function would need to check whether the user is logged in.

Example:

```python
if logged_in:
    ...
```

This would create duplicated code.

Using a decorator makes the program cleaner and easier to maintain.

---

# Program Flow

```
Start

↓

Login

↓

Decorator

↓

Check Login

↓

Yes

↓

Execute Function

↓

No

↓

Access Denied
```

---

# Learning Outcomes

After completing this project, I learned:

- Object-Oriented Programming
- Function Decorators
- Wrapper Functions
- Access Control
- Python Modules
- Code Reusability

---

# Author

Richard Xiahou

Master of Software Engineering

Yoobee Colleges