# OOP Basics — Classes and Objects

## What Is OOP?

Object-Oriented Programming organizes code around **objects** — bundles of data (attributes) and behavior (methods) — instead of just functions acting on raw data.

A **class** is a blueprint. An **object** (or instance) is a specific thing built from that blueprint.

```python
class Dog:
    pass

d = Dog()   # d is an object/instance of the Dog class
```

---

## The `__init__` Method (Constructor)

Runs automatically when a new object is created — used to set up initial attributes.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name   # instance attribute
        self.age = age

d1 = Dog("Rex", 3)
d2 = Dog("Bella", 5)

print(d1.name, d1.age)   # Rex 3
print(d2.name, d2.age)   # Bella 5
```

`self` refers to the specific instance being created/used — it's how each object keeps its own separate data.

---

## Instance Methods

Functions defined inside a class that operate on an instance's data.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

    def birthday(self):
        self.age += 1

d = Dog("Rex", 3)
d.bark()        # Rex says Woof!
d.birthday()
print(d.age)    # 4
```

---

## Class Attributes vs Instance Attributes

- **Class attribute**: shared by *all* instances, defined directly in the class body.
- **Instance attribute**: unique to each object, usually set in `__init__`.

```python
class Dog:
    species = "Canis familiaris"   # class attribute — same for every Dog

    def __init__(self, name):
        self.name = name             # instance attribute — unique per object

d1 = Dog("Rex")
d2 = Dog("Bella")

print(d1.species, d2.species)   # Canis familiaris  Canis familiaris
print(d1.name, d2.name)         # Rex  Bella
```

---

## Dunder Methods (Recap Preview)

Special methods (double-underscore, "dunder") let your objects work with Python's built-in syntax (`print()`, `==`, `len()`, etc.). This is the focus of your roadmap's Day 6.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Dog({self.name}, {self.age} yrs)"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __len__(self):
        return self.age

d1 = Dog("Rex", 3)
d2 = Dog("Rex", 3)

print(d1)          # Dog(Rex, 3 yrs)   <- uses __str__
print(d1 == d2)     # True              <- uses __eq__
print(len(d1))      # 3                 <- uses __len__
```

---

## Inheritance

A class can inherit attributes/methods from another class — the "is-a" relationship.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):          # overrides the parent's method
        print(f"{self.name} says Woof!")

class Cat(Animal):
    pass   # inherits speak() unchanged

d = Dog("Rex")
c = Cat("Whiskers")

d.speak()   # Rex says Woof!
c.speak()   # Whiskers makes a sound
```

### `super()` — Calling the Parent's Method

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # runs Animal's __init__
        self.breed = breed

d = Dog("Rex", "Labrador")
print(d.name, d.breed)   # Rex Labrador
```

---

## Encapsulation (Convention-Based in Python)

Python doesn't have strict private variables — it uses naming conventions instead.

```python
class Account:
    def __init__(self, balance):
        self._balance = balance      # "protected" — convention: internal use
        self.__pin = "1234"          # "private" — name-mangled

    def get_balance(self):
        return self._balance

a = Account(1000)
print(a.get_balance())   # 1000
print(a._balance)         # 1000 — accessible, but convention says "don't touch this directly"
```

| Prefix | Convention meaning |
|---|---|
| `name` | Public — freely accessible |
| `_name` | Protected — internal use, but not enforced |
| `__name` | Private — name-mangled to `_ClassName__name`, harder (not impossible) to access from outside |

---

## Quick Reference

| Concept | Key takeaway |
|---|---|
| Class | Blueprint for creating objects |
| `__init__` | Runs on object creation, sets up attributes |
| `self` | Refers to the specific instance |
| Class attribute | Shared across all instances |
| Instance attribute | Unique per object |
| Inheritance | `class Child(Parent):` — reuse and override behavior |
| `super()` | Call the parent class's method |
| Dunder methods | Hook into Python's built-in behavior (`==`, `print()`, `len()`) |

---

## Practice Task

```python
# oop_check.py

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def __str__(self):
        return f"{self.owner}'s account: ${self.balance}"


acc = BankAccount("Yash", 100)
acc.deposit(50)
acc.withdraw(30)
print(acc)              # Yash's account: $120
acc.withdraw(1000)      # Insufficient funds
```

Predict the balance after each operation before running.
