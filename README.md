# MSE800 - Week 8 Python Exercises

This folder contains my Python exercises for **MSE800 - Week 8**.

The main focus of this week is **Design Patterns**, with examples implemented in Python.

The exercises are based on the Design Patterns covered in class and are intended to help me understand how different classes and objects can be organised to solve common software design problems.

---

## 1. What I learned in Week 8

The main topics covered this week include:

- Version Control System (Git)
- GitHub repository management
- Object-Oriented Programming (OOP)
- Inheritance
- Design Patterns
- Creational Design Patterns
- Structural Design Patterns
- Behavioral Design Patterns

The main focus of my Python exercises in this folder is **Design Patterns**.

---

## 2. What is a Design Pattern?

A Design Pattern is a general model for solving a common software design problem.

A Design Pattern is **not ready-to-use code**.

Instead, it provides a general structure that can be adapted to different software projects.

A Design Pattern normally describes:

1. **Name** - the name of the pattern
2. **Problem** - the problem that the pattern solves
3. **Solution** - how classes and objects can be organised
4. **Consequences** - the results of using the pattern

Design Patterns should only be used when they are necessary. A simple solution is sometimes better than using a Design Pattern.

---

## 3. Three Main Categories

The Design Patterns covered in this week's exercises can be grouped into three main categories.

```text
                    Design Patterns
                          |
          +---------------+---------------+
          |               |               |
     Creational       Structural      Behavioral
      创建型             结构型            行为型
          |               |               |
   Object creation   Object structure   Object communication
```

### Creational Patterns

These patterns focus on **how objects are created**.

Examples:

- Factory
- Factory Method
- Abstract Factory
- Singleton
- Builder

### Structural Patterns

These patterns focus on **how classes and objects are combined**.

Examples:

- Adapter
- Decorator

### Behavioral Patterns

These patterns focus on **how objects communicate and responsibilities are distributed**.

Example:

- Observer

---

# 4. Creational Patterns

## 4.1 Simple Factory

A Simple Factory provides one place for creating different types of objects.

The client provides a choice, and the factory decides which object to create.

```text
Client
   |
   v
Factory
   |
   +---- Product A
   |
   +---- Product B
```

### Exercises

```text
Creation Patterns/
└── factoryPattern/
    ├── simplefactory.py
    ├── basicFactory.py
    ├── AnimalFactory.py
    └── foodOrderSystem.py
```

These examples help demonstrate how object creation can be separated from the client code.

---

## 4.2 Factory Method

The Factory Method pattern uses inheritance.

Instead of one factory deciding every type of object, different subclasses can decide which object they create.

```text
Creator
   |
   +---- Creator A ----> Product A
   |
   +---- Creator B ----> Product B
```

### Important idea

```text
Simple Factory
    Factory decides which object to create

Factory Method
    Subclass decides which object to create
```

### Exercises

```text
Creation Patterns/
└── factoryMethodDesign/
    ├── FactoryMethoddesign.py
    ├── OnlineNotificationSystem.py
    └── SystemUIFactory.py
```

---

## 4.3 Abstract Factory

The Abstract Factory pattern is used when we need to create a **family of related objects**.

For example, a user interface may have different components for different operating systems.

```text
Windows
    ├── Windows Button
    └── Windows Checkbox

Mac
    ├── Mac Button
    └── Mac Checkbox
```

The client works with the factory without needing to know the concrete classes.

```text
             Abstract Factory
                    |
          +---------+---------+
          |                   |
   Windows Factory       Mac Factory
          |                   |
     Windows UI             Mac UI
```

### Exercises

```text
Creation Patterns/
└── AbstractFactory/
    ├── FurnitureFactory.py
    └── SystemUIFactory.py
```

---

# 5. Singleton

The Singleton pattern is used when a class should have **only one instance**.

The general idea is:

```text
        Class
          |
          v
     One Instance
       /       \
      /         \
 Object A      Object B
      \         /
       \       /
        Same Object
```

For example, a system may need only one configuration manager.

### Exercises

```text
Creation Patterns/
└── Singleton/
    ├── basicSingleton.py
    ├── gameSetting.py
    └── UniversityConfigurationManager.py
```

### Important idea

```python
object1 is object2
```

should be:

```text
True
```

when both variables refer to the same Singleton instance.

---

# 6. Builder Pattern

The Builder Pattern is useful when an object is complex and has many parts or options.

Instead of creating the whole object in one large constructor, the object can be built step by step.

```text
Builder
   |
   +---- set CPU
   |
   +---- set RAM
   |
   +---- set Storage
   |
   +---- set Graphics Card
   |
   v
 Build
   |
   v
Complex Object
```

### Exercises

```text
Creation Patterns/
└── BuilderPattern/
    ├── BuildingAComputer.py
    └── PizzaBuilder.py
```

### Important idea

```text
Builder
    |
    | step by step
    v
Complex Object
```

This can make the construction process easier to understand and allows different versions of the same type of object to be created.

---

# 7. Structural Patterns

Structural Design Patterns focus on how classes and objects are combined to form larger structures.

The two patterns practised in this project are:

- Adapter
- Decorator

---

# 8. Adapter Pattern

The Adapter Pattern allows two incompatible classes to work together.

For example:

```text
Client
  |
  v
Adapter
  |
  v
Old / Incompatible Class
```

The Adapter converts one interface into another interface expected by the client.

## Adapter using Composition

One approach is to store the old object inside the Adapter.

```python
self.adaptee = adaptee
```

This represents a:

```text
has-a
```

relationship.

```text
Adapter
   |
   +---- has-a ----> Adaptee
```

### Exercises

```text
Structural Patterns/
└── Adapter/
    ├── Combination.py
    ├── MultipleInheritance.py
    └── SimpleAdapter.py
```

---

# 9. Adapter using Multiple Inheritance

Another approach is to use multiple inheritance.

```python
class Adapter(Target, Adaptee):
    ...
```

This gives the Adapter access to both interfaces.

The exercises compare the two approaches:

```text
Composition

Adapter
   |
   +---- has-a ----> Adaptee
```

and:

```text
Multiple Inheritance

Adapter
   |
   +---- is-a ----> Target
   |
   +---- is-a ----> Adaptee
```

This connects the Adapter Pattern with the OOP concepts of **composition and inheritance**.

---

# 10. Decorator Pattern

The Decorator Pattern allows additional functionality to be added to an existing object without changing its original class.

For example:

```text
Coffee
   |
   v
Milk Decorator
   |
   v
Sugar Decorator
   |
   v
Coffee + Milk + Sugar
```

Each decorator can add something extra.

### Exercises

```text
Structural Patterns/
└── Decorator/
    ├── CarCustomer.py
    └── CoffeeDecorator.py
```

The main idea is:

```text
Original Object
      +
Additional Responsibility
      =
Extended Object
```

---

# 11. Behavioral Pattern

Behavioral Design Patterns focus on how objects communicate with each other.

The main behavioral pattern practised this week is:

- Observer

---

# 12. Observer Pattern

The Observer Pattern is useful when one object changes and other objects need to be notified.

For example:

```text
             Channel
                |
          upload video
                |
        +-------+-------+
        |       |       |
        v       v       v
      User    User    User
```

The main object keeps a list of observers.

When something changes, it notifies the observers.

A simplified structure is:

```python
self.subscribers = []

self.subscribers.append(user)

for user in self.subscribers:
    user.notify(video)
```

### Exercises

```text
Behavioral Patterns/
└── Observer/
    ├── SimpleObserver.py
    ├── StockPriceMonitor.py
    └── YouTubeChannel.py
```

These examples demonstrate how one object can communicate changes to multiple other objects.

---

# 13. Important Pattern Comparisons

## Simple Factory vs Factory Method vs Abstract Factory

| Pattern | Main Idea | Who decides? |
|---|---|---|
| Simple Factory | One factory creates objects | Factory |
| Factory Method | Subclasses create objects | Subclass |
| Abstract Factory | Creates a family of related objects | Concrete Factory |

A simple way to remember:

```text
Simple Factory
    ↓
One factory

Factory Method
    ↓
Different subclasses

Abstract Factory
    ↓
A family of related objects
```

---

# 14. Creational Patterns Summary

| Pattern | Main Question |
|---|---|
| Factory | Which object should I create? |
| Factory Method | Which subclass should create the object? |
| Abstract Factory | How can I create a related family of objects? |
| Singleton | How can I make sure there is only one instance? |
| Builder | How can I build a complex object step by step? |

---

# 15. Structural Patterns Summary

| Pattern | Main Question |
|---|---|
| Adapter | How can incompatible classes work together? |
| Decorator | How can I add functionality without changing the original class? |

---

# 16. Behavioral Patterns Summary

| Pattern | Main Question |
|---|---|
| Observer | How can other objects be notified when something changes? |

---

# 17. Week 8 Learning Summary

Before Week 8, I mainly focused on writing Python programs and understanding Object-Oriented Programming.

For example:

```text
Class
   ↓
Object
   ↓
Attributes
   ↓
Methods
   ↓
Inheritance
   ↓
Composition
```

In Week 8, I started to think more about **software design**.

Instead of only asking:

> "How do I write this code?"

I also need to ask:

> "How should these classes and objects be organised?"

Design Patterns provide common models for solving recurring design problems.

The main concepts I practised are:

```text
Object Creation
    ↓
Factory
Factory Method
Abstract Factory
Singleton
Builder

Object Structure
    ↓
Adapter
Decorator

Object Communication
    ↓
Observer
```

---

# 18. Key Things I Should Remember

### Factory

Separate object creation from the client.

### Factory Method

Subclasses decide which product to create.

### Abstract Factory

Create a family of related objects.

### Singleton

Only one instance of a class should exist.

### Builder

Build a complex object step by step.

### Adapter

Make incompatible interfaces work together.

### Decorator

Add functionality to an object without changing its original class.

### Observer

Notify other objects when an object changes.

---

# 19. Final Reflection

The main lesson from Week 8 is that a Design Pattern is not something that should be added just because it is available.

A Design Pattern should be used when it helps solve a particular design problem.

The goal is not to use as many patterns as possible.

The goal is to understand:

```text
Problem
   ↓
Possible Design
   ↓
Suitable Pattern
   ↓
Classes and Objects
   ↓
Implementation
```

These exercises are my practice examples for understanding how OOP concepts can be combined into larger software designs.