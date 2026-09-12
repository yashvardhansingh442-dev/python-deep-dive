# Dictionaries

## What Is a Dictionary?

A dictionary is an **unordered (insertion-ordered since Python 3.7+), mutable** collection of **key-value pairs**. Keys must be unique and hashable (strings, numbers, tuples); values can be anything.

```python
student = {
    "name": "Yash",
    "age": 21,
    "gpa": 8.5
}
```

---

## Accessing Values

```python
student = {"name": "Yash", "age": 21}

print(student["name"])        # "Yash"
print(student.get("age"))     # 21
print(student.get("city"))    # None  (no KeyError)
print(student.get("city", "Unknown"))  # "Unknown"  (default fallback)
```

**Key difference:** `d["key"]` raises `KeyError` if missing; `d.get("key")` returns `None` (or a default) instead — safer for uncertain keys.

```python
print(student["city"])   # ❌ KeyError: 'city'
```

---

## Adding and Updating Values

```python
student = {"name": "Yash", "age": 21}

student["gpa"] = 8.5          # add new key
student["age"] = 22           # update existing key

print(student)
# {'name': 'Yash', 'age': 22, 'gpa': 8.5}
```

---

## Removing Values

| Method | Behavior |
|---|---|
| `del d[key]` | Removes key; raises `KeyError` if missing |
| `.pop(key)` | Removes and returns value; can supply a default |
| `.popitem()` | Removes and returns the last inserted key-value pair |
| `.clear()` | Removes all items |

```python
student = {"name": "Yash", "age": 21, "gpa": 8.5}

del student["gpa"]
print(student)              # {'name': 'Yash', 'age': 21}

age = student.pop("age")
print(age, student)         # 21  {'name': 'Yash'}
```

---

## Common Dictionary Methods

| Method | Purpose | Example |
|---|---|---|
| `.keys()` | All keys | `d.keys()` |
| `.values()` | All values | `d.values()` |
| `.items()` | Key-value pairs | `d.items()` |
| `.update(other)` | Merge another dict in | `d.update({"city": "Delhi"})` |
| `.get(key, default)` | Safe access | `d.get("x", 0)` |
| `.setdefault(key, default)` | Get value, or set it if missing | `d.setdefault("count", 0)` |

```python
student = {"name": "Yash", "age": 21}

for key in student.keys():
    print(key)
# name
# age

for value in student.values():
    print(value)
# Yash
# 21

for key, value in student.items():
    print(f"{key}: {value}")
# name: Yash
# age: 21
```

---

## Checking Membership

Membership checks (`in`) test **keys**, not values, by default.

```python
student = {"name": "Yash", "age": 21}

print("name" in student)     # True  -> checks keys
print("Yash" in student)     # False -> "Yash" is a value, not a key
print("Yash" in student.values())  # True
```

---

## Nested Dictionaries

```python
students = {
    "s1": {"name": "Yash", "age": 21},
    "s2": {"name": "Raj", "age": 22}
}

print(students["s1"]["name"])   # Yash

for sid, info in students.items():
    print(sid, "->", info["name"])
# s1 -> Yash
# s2 -> Raj
```

---

## Dictionary Comprehension

```python
squares = {x: x**2 for x in range(5)}
print(squares)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

filtered = {k: v for k, v in squares.items() if v > 5}
print(filtered)
# {3: 9, 4: 16}
```

---

## Merging Dictionaries

```python
a = {"x": 1, "y": 2}
b = {"y": 99, "z": 3}

merged = {**a, **b}
print(merged)
# {'x': 1, 'y': 99, 'z': 3}   <- b's value for 'y' wins (later dict overrides)

# Python 3.9+ shortcut:
merged2 = a | b
print(merged2)
# {'x': 1, 'y': 99, 'z': 3}
```

---

## Quick Reference

| Concept | Key takeaway |
|---|---|
| `d[key]` vs `.get(key)` | `[]` raises `KeyError`, `.get()` returns `None`/default |
| Keys must be hashable | Strings, numbers, tuples — not lists |
| `.items()` | The go-to way to loop over key + value together |
| `in` checks keys | Use `.values()` explicitly to check values |
| Dict comprehension | `{key_expr: val_expr for item in iterable}` |
| Merging | `{**a, **b}` or `a \| b` (3.9+) — later dict wins on conflicts |

---

## Practice Task

```python
# dicts_check.py
inventory = {"apples": 10, "bananas": 5, "cherries": 20}

# Add a new item
inventory["mangoes"] = 15

# Update existing item
inventory["apples"] += 5

# Total items in stock
print(sum(inventory.values()))     # 55

# Items with more than 10 in stock
high_stock = {k: v for k, v in inventory.items() if v > 10}
print(high_stock)                  # {'apples': 15, 'cherries': 20, 'mangoes': 15}

# Safe lookup for a missing item
print(inventory.get("grapes", "Out of stock"))  # "Out of stock"
```

Predict each output before running — especially the totals after the update.
