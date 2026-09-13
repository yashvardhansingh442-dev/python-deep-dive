# Exception Handling

## What Is an Exception?

An exception is an error that occurs during program execution and (if unhandled) crashes the program. Python lets you **catch** these errors and respond gracefully instead of crashing.

```python
print(10 / 0)   # ZeroDivisionError: division by zero
# program crashes here
```

---

## `try` / `except` — Basic Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero")

print("Program continues running")
```

---

## Catching Specific Exceptions

Always catch the **specific** exception type when you know it — catching everything blindly hides real bugs.

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("That wasn't a valid number")
except ZeroDivisionError:
    print("Can't divide by zero")
```

### Common built-in exceptions

| Exception | When it happens |
|---|---|
| `ValueError` | Right type, invalid value — `int("abc")` |
| `TypeError` | Wrong type for an operation — `"2" + 2` |
| `ZeroDivisionError` | Dividing by zero |
| `KeyError` | Missing dictionary key |
| `IndexError` | List index out of range |
| `FileNotFoundError` | File doesn't exist |
| `AttributeError` | Calling a method/attribute that doesn't exist |

```python
d = {"a": 1}
print(d["b"])        # KeyError: 'b'

lst = [1, 2, 3]
print(lst[10])        # IndexError: list index out of range
```

---

## Catching Multiple Exceptions Together

```python
try:
    value = int("abc")
except (ValueError, TypeError):
    print("Invalid input type or value")
```

---

## `else` — Runs Only If No Exception Occurred

```python
try:
    num = int("42")
except ValueError:
    print("Invalid number")
else:
    print(f"Success: {num}")   # only runs if no exception was raised
```

---

## `finally` — Always Runs

Runs whether an exception occurred or not — used for cleanup (closing files, releasing resources).

```python
try:
    f = open("data.txt")
    # process file
except FileNotFoundError:
    print("File not found")
finally:
    print("Cleanup done — this always runs")
```

---

## Accessing the Exception Object

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")
    # Error occurred: division by zero
```

---

## Raising Your Own Exceptions

Use `raise` to trigger an exception intentionally — useful for validating input in your own functions.

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

set_age(-5)   # raises ValueError: Age cannot be negative
```

```python
try:
    set_age(-5)
except ValueError as e:
    print(f"Invalid input: {e}")
```

---

## Custom Exceptions

Define your own exception classes by inheriting from `Exception` — useful for domain-specific errors in larger programs (relevant later for your Day 9 custom exception hierarchy).

```python
class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Not enough funds")
    return balance - amount

try:
    withdraw(100, 150)
except InsufficientBalanceError as e:
    print(f"Transaction failed: {e}")
```

---

## Quick Reference

| Concept | Key takeaway |
|---|---|
| `try` / `except` | Catch and handle errors instead of crashing |
| Specific exceptions | Catch the exact type — avoid bare `except:` |
| `else` | Runs only if no exception occurred |
| `finally` | Always runs — used for cleanup |
| `raise` | Manually trigger an exception |
| Custom exceptions | Subclass `Exception` for domain-specific errors |

---

## Practice Task

```python
# exceptions_check.py

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: division by zero"
    except TypeError:
        return "Error: both inputs must be numbers"
    else:
        return result
    finally:
        print("Division attempt finished")

print(safe_divide(10, 2))     # 5.0
print(safe_divide(10, 0))     # "Error: division by zero"
print(safe_divide(10, "2"))   # "Error: both inputs must be numbers"
```

Predict each output (and when "Division attempt finished" prints) before running.
