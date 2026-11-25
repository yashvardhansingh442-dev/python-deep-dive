# Functions

## What Are Functions?

A function is a reusable, named block of code that performs a task. Instead of repeating logic, you define it once and call it whenever needed.

---

## Defining and Calling a Function

```python
def greet():
    print("Hello!")

greet()   # Hello!
```

`def` declares the function, the indented block is its body, and calling it by name (with `()`) runs that block.

---

## Parameters and Arguments

**Parameters** are the names in the function definition. **Arguments** are the actual values you pass in when calling.

```python
def greet(name):     # name = parameter
    print(f"Hello, {name}!")

greet("Yash")         # "Yash" = argument
# Hello, Yash!
```

### Multiple parameters

```python
def add(a, b):
    print(a + b)

add(3, 5)   # 8
```

---

## `return` — Sending a Value Back

`print()` displays something; `return` gives a value back to the caller so it can be stored or reused.

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)   # 8
```

A function without an explicit `return` returns `None`:

```python
def greet(name):
    print(f"Hello, {name}!")

x = greet("Yash")
print(x)   # None
```

---

## Default Arguments

Give a parameter a fallback value, used when the caller doesn't provide one.

```python
def greet(name="friend"):
    print(f"Hello, {name}!")

greet()          # Hello, friend!
greet("Yash")    # Hello, Yash!
```

**Trap: mutable default arguments** — never use a mutable object (`list`, `dict`) as a default. It's created once and shared across all calls.

```python
# ❌ bug
def add_item(item, cart=[]):
    cart.append(item)
    return cart

print(add_item("apple"))    # ['apple']
print(add_item("banana"))   # ['apple', 'banana']  <- unexpected! same list reused
```

```python
# ✅ fix
def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart
```

---

## Keyword Arguments

Pass arguments by name instead of position — improves readability and lets you skip the order.

```python
def describe(name, age):
    print(f"{name} is {age} years old")

describe(age=21, name="Yash")   # order doesn't matter with keywords
```

---

## `*args` — Variable Number of Positional Arguments

Collects extra positional arguments into a tuple.

```python
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3))       # 6
print(total(1, 2, 3, 4, 5)) # 15
```

---

## `**kwargs` — Variable Number of Keyword Arguments

Collects extra keyword arguments into a dictionary.

```python
def show_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

show_info(name="Yash", age=21, active=True)
# name: Yash
# age: 21
# active: True
```

---

## Combining Argument Types

Order matters: regular params → `*args` → default params → `**kwargs`.

```python
def order_summary(customer, *items, discount=0, **extra):
    print(f"Customer: {customer}")
    print(f"Items: {items}")
    print(f"Discount: {discount}%")
    print(f"Extra info: {extra}")

order_summary("Yash", "book", "pen", discount=10, gift_wrap=True)
```

---

## Scope — Where a Variable Lives

A variable defined inside a function only exists inside that function (**local scope**), unless declared `global`.

```python
x = 10   # global scope

def show():
    x = 5   # local scope — different variable, doesn't affect global x
    print(x)

show()      # 5
print(x)    # 10
```

---

## Quick Reference

| Concept | Key takeaway |
|---|---|
| `def` | Declares a function |
| Parameters vs arguments | Parameters = names in definition; arguments = values passed in |
| `return` | Sends a value back; no `return` means `None` |
| Default arguments | Fallback value if none is passed — avoid mutable defaults |
| Keyword arguments | Pass by name, order-independent |
| `*args` | Extra positional args → tuple |
| `**kwargs` | Extra keyword args → dict |
| Scope | Local variables inside a function don't leak to the global scope |

---

## Practice Task

```python
# functions_check.py

def is_even(n):
    return n % 2 == 0

def average(*numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def build_profile(name, **details):
    profile = {"name": name}
    profile.update(details)
    return profile

print(is_even(7))                      # False
print(average(4, 8, 15, 16, 23, 42))   # 18.0
print(build_profile("Yash", age=21, gpa=8.5))
# {'name': 'Yash', 'age': 21, 'gpa': 8.5}
```

Predict each output before running — especially `average()` with no arguments, and what `build_profile` returns.
