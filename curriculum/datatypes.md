# Data Types

## What Are Data Types?

A data type tells Python what kind of value a variable holds, and what operations are valid on it.

---

## Basic Built-in Types

| Type | Example | Meaning |
|---|---|---|
| `str` | `name = "Yash"` | Text |
| `int` | `age = 21` | Whole numbers |
| `float` | `gpa = 8.5` | Decimal numbers |
| `bool` | `active = True` | `True` / `False` |
| `NoneType` | `nothing = None` | Absence of a value |

```python
name    = "Yash"     # str
age     = 21         # int
gpa     = 8.5        # float
active  = True        # bool
nothing = None         # NoneType
```

---

## Checking Type

Use the built-in `type()` function:

```python
print(type(name))    # <class 'str'>
print(type(age))     # <class 'int'>
```

---

## Type Casting (Converting Between Types)

```python
x = "10"
y = int(x)          # "10" -> 10

z = str(25)          # 25 -> "25"

f = float("3.14")    # "3.14" -> 3.14
```

| Function | Converts to |
|---|---|
| `int(x)` | integer |
| `float(x)` | float |
| `str(x)` | string |
| `bool(x)` | boolean |

---

## Mutable vs Immutable Types

| Immutable (can't change in place) | Mutable (can change in place) |
|---|---|
| `int` | `list` |
| `float` | `dict` |
| `str` | `set` |
| `bool` | |
| `tuple` | |

```python
s = "hello"
s[0] = "H"     # ❌ TypeError — strings are immutable
```

```python
lst = [1, 2, 3]
lst[0] = 99    # ✅ works — lists are mutable
# lst -> [99, 2, 3]
```

---

## Why This Matters

- **Immutable objects** are safe to share and pass around — nothing else can silently change them under you.
- **Mutable objects** can be changed by *any* reference to them, which is a common source of bugs (see the linked-list append example from Day 1's identity/mutability notes).

```python
a = [1, 2, 3]
b = a
b.append(4)
# a is now [1, 2, 3, 4] too — a and b point to the same mutable object
```

---

## Quick Reference

| Concept | Key takeaway |
|---|---|
| `type()` | Reveals the type of any value |
| Type casting | Convert between types with `int()`, `float()`, `str()`, `bool()` |
| Immutable types | `int`, `float`, `str`, `bool`, `tuple` |
| Mutable types | `list`, `dict`, `set` |
| Shared references | Mutating a mutable object affects every name pointing to it |
