# Conditionals

## What Are Conditionals?

Conditionals let a program make decisions — run different code depending on whether a condition is `True` or `False`.

---

## Basic `if` Statement

```python
age = 20

if age >= 18:
    print("You are an adult")
```

Indentation (4 spaces) defines the block — Python doesn't use `{}` like other languages.

---

## `if` / `else`

```python
age = 15

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

---

## `if` / `elif` / `else`

Use `elif` to check multiple conditions in sequence. Python checks them top to bottom and stops at the first `True`.

```python
marks = 72

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

# Output: Grade: C
```

---

## Nested Conditionals

An `if` inside another `if` — used when a decision depends on another decision.

```python
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("Get a license first")
else:
    print("Too young to drive")
```

---

## Truthy and Falsy Values

Python treats many values as `True`/`False` even outside explicit booleans.

| Falsy values | Truthy values |
|---|---|
| `0`, `0.0` | any nonzero number |
| `""` (empty string) | non-empty string |
| `[]`, `{}`, `()`, `set()` (empty collections) | non-empty collections |
| `None` | most other objects |
| `False` | `True` |

```python
name = ""

if name:
    print(f"Hello, {name}")
else:
    print("No name provided")
# Output: No name provided
```

---

## Combining Conditions

Use `and`, `or`, `not` (from the Operators notes) to build compound conditions.

```python
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("Entry allowed")
else:
    print("Entry denied")
```

---

## Ternary (Conditional) Expression

A compact one-line `if`/`else` for simple cases.

```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)   # adult
```

Use this only for short, readable conditions — nesting ternaries hurts readability fast.

---

## Common Trap: `=` vs `==`

```python
x = 5

if x = 5:      # ❌ SyntaxError — = is assignment, not comparison
    print("five")

if x == 5:     # ✅ correct — == compares values
    print("five")
```

---

## Quick Reference

| Concept | Key takeaway |
|---|---|
| `if` / `elif` / `else` | Checked top to bottom, stops at first `True` |
| Indentation | Defines blocks — no `{}` |
| Truthy/Falsy | Empty/zero/`None` values act as `False` in conditions |
| Ternary | `value_if_true if condition else value_if_false` |
| `=` vs `==` | Assignment vs comparison — a classic bug source |

---

## Practice Task

```python
# conditionals_check.py
num = 17

if num < 0:
    print("Negative")
elif num == 0:
    print("Zero")
elif num % 2 == 0:
    print("Positive and even")
else:
    print("Positive and odd")
```

Predict the output before running — then try it with `num = -4`, `num = 0`, and `num = 8`.
