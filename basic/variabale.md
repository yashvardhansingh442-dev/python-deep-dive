# Variables

## What is a Variable?

A variable is a **name that points to a value stored in memory**.
In Python, you don't declare types — just assign and go.

```python
name   = "Yash"     # str
age    = 21         # int
gpa    = 8.5         # float
active = True        # bool
```

Python is **dynamically typed** — the type is attached to the *value*, not the variable name. The same name can point to a string today and an integer tomorrow.

```python
x = "hello"
x = 42          # perfectly valid — x now points to an int
```

---

## Naming Rules

| Rule | Example |
|---|---|
| Must start with a letter or underscore, not a digit | `_count`, `age` ✅ &nbsp;&nbsp; `2age` ❌ |
| Case-sensitive | `age` and `Age` are different variables |
| Can't use reserved words | `for`, `class`, `if`, `return`, etc. are off-limits |
| Convention: `snake_case` for variables/functions | `student_name` |
| Convention: `PascalCase` for classes | `StudentRecord` |

---

## Multiple Assignment

```python
x = y = z = 0
# all three -> 0
```

### Unpacking

```python
a, b, c = 1, 2, 3
# a=1, b=2, c=3
```

### Star unpacking

```python
first, *rest = [10, 20, 30, 40]
# first = 10
# rest  = [20, 30, 40]
```

### Swap without a temp variable

```python
a, b = 5, 10
a, b = b, a
# a=10, b=5  ✓
```

This is Python's classic one-liner swap — no temp variable needed. Under the hood, Python builds the tuple `(b, a)` on the right side *before* assigning, so both values swap simultaneously.

---

## Identity vs. Mutability

Reassignment (`=`) **rebinds** a name to a new object.
Mutation (`.append()`, `[i] = ...`, etc.) **changes the object in place** — and every name pointing to that same object sees the change.

```python
x = 10
y = x
y = 20          # rebinds y to a new object; x is untouched
# x = 10, y = 20

lst1 = [1, 2, 3]
lst2 = lst1
lst2.append(4)  # mutates the same list object
# lst1 is now [1, 2, 3, 4] too — because lst1 and lst2 point to the same object
```

Check this with `id()`:

```python
print(id(lst1) == id(lst2))   # True — same object in memory
```

---

## Quick Reference

| Concept | Key takeaway |
|---|---|
| Dynamic typing | Type belongs to the value, not the name |
| Multiple assignment | `x = y = z = 0` binds all names to the same object |
| Unpacking | `a, b, c = 1, 2, 3` — count must match |
| Star unpacking | `first, *rest = [...]` — grabs the "leftover" into a list |
| Swap trick | `a, b = b, a` — no temp variable |
| Mutation vs reassignment | Mutation affects all references; reassignment only affects one name |
