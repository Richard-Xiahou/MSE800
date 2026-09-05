# Python Decorators - Study Notes

## Overview

This document summarizes the main concepts of Python Decorators learned in class.

Decorators are a Python feature that allows us to add new functionality to an existing function or class without changing its original code.

---

# What is a Decorator?

A decorator is a function that takes another function as an argument, adds extra behavior, and returns a new function.

The original function does not need to be modified.

Simple idea:

Original Function

↓

Decorator

↓

Enhanced Function

---

# How Decorators Work

A decorator usually contains three steps.

1. Receive the original function.
2. Define a wrapper function.
3. Return the wrapper function.

Example:

```python
def decorator(func):

    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper
```

---

# The @ Symbol

Python provides a simple syntax for decorators.

```python
@decorator
def hello():
    print("Hello")
```

This is equivalent to:

```python
def hello():
    print("Hello")

hello = decorator(hello)
```

The @ symbol is only a shortcut (syntactic sugar).

---

# Why Use Wrapper Functions?

The wrapper function allows us to execute code before and after the original function.

Example output:

```
Before
Hello
After
```

This lets us add extra features without changing the original function.

---

# *args and **kwargs

Some functions have different numbers of parameters.

To make decorators reusable, we usually write:

```python
def wrapper(*args, **kwargs):
    return func(*args, **kwargs)
```

This allows one decorator to work with many different functions.

---

# Multiple Decorators

More than one decorator can be applied.

Example:

```python
@timer
@logger
def calculate():
    pass
```

Python executes decorators from the bottom to the top.

Equivalent to:

```python
calculate = timer(logger(calculate))
```

---

# Class Decorators

Decorators can also be applied to classes.

Example:

```python
@decorator
class Student:
    pass
```

The decorator receives the class and returns a modified class.

---

# Common Uses of Decorators


Decorators are widely used in real software development.
实际开发中 Decorator 的使用场景

Examples include:

- Logging (日志)
- Authentication (认证)
- Permission checking (权限检查)
- Timing functions (计时函数)
- Input validation (输入验证)
- Error handling (错误处理)
- Caching (缓存)
- Performance monitoring (性能监控)

These features can be added without changing the original function.

---

# Advantages

- Reduce duplicated code
- Improve code readability
- Easier to maintain
- Reusable functionality
- Separate business logic from extra features

---

# Simple Example

```python
def welcome(func):

    def wrapper():
        print("Welcome to Python!")
        func()

    return wrapper


@welcome
def student():
    print("Richard")


student()
```

Output:

```
Welcome to Python!
Richard
```

---

# Key Concept

A decorator wraps a function.

```
Original Function
        ↓
Decorator
        ↓
Wrapper Function
        ↓
Enhanced Function
```

---

# Summary

Decorators are a powerful feature in Python.

They allow developers to add additional behavior such as logging, timing, validation, and authentication without modifying the original code.

Although decorators look difficult at first, they are simply functions that receive another function, wrap it, and return a new function.

Understanding functions as objects, nested functions, and returning functions makes decorators much easier to understand.