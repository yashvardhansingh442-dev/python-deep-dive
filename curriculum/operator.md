# Operators

Operators perform actions on values (**operands**) — math, comparisons, logic, and assignment.

---

## 1. Arithmetic Operators

Perform mathematical calculations.

| Operator | Meaning | Example (`a=10, b=3`) | Result |
|---|---|---|---|
| `+` | Addition | `a + b` | `13` |
| `-` | Subtraction | `a - b` | `7` |
| `*` | Multiplication | `a * b` | `30` |
| `/` | True division (always float) | `a / b` | `3.333...` |
| `//` | Floor division (drops remainder) | `a // b` | `3` |
| `%` | Modulus (remainder) | `a % b` | `1` |
| `**` | Exponentiation | `a ** b` | `1000` |

```python
a, b = 10, 3
print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.333...
print(a // b)   # 3
print(a % b)    # 1
print(a ** b)   # 1000
```

---

## 2. Comparison Operators

Always return a `bool` (`True`/`False`).

| Operator | Meaning | Example (`a=10, b=3`) | Result |
|---|---|---|---|
| `==` | Equal to | `a == b` | `False` |
| `!=` | Not equal to | `a != b` | `True` |
| `>` | Greater than | `a > b` | `True` |
| `<` | Less than | `a < b` | `False` |
| `>=` | Greater than or equal to | `a >= b` | `True` |
| `<=` | Less than or equal to | `a <= b` | `False` |

```python
a, b = 10, 3
print(a == b)   # False
print(a != b)   # True
print(a > b)    # True
print(a < b)    # False
print(a >= b)   # True
print(a <= b)   # False
```

---

## 3. Logical Operators

Combine boolean expressions.

| Operator | Meaning | Rule |
|---|---|---|
| `and` | True only if both sides are True | `x and y` |
| `or` | True if at least one side is True | `x or y` |
| `not` | Inverts the boolean value | `not x` |

```python
x, y = True, False
print(x and y)   # False — both must be True
print(x or y)    # True  — at least one True
print(not x)     # False — inverts x
```

---

## 4. Assignment Operators (Shorthand)

Combine an operation with assignment.

| Operator | Equivalent to | Example (`n=5`) | Result |
|---|---|---|---|
| `+=` | `n = n + 1` | `n += 1` | `6` |
| `-=` | `n = n - 1` | `n -= 1` | `5` |
| `*=` | `n = n * 2` | `n *= 2` | `10` |
| `//=` | `n = n // 3` | `n //= 3` | `3` |

```python
n = 5
n += 1    # 6
n -= 1    # 5
n *= 2    # 10
n //= 3   # 3
```

---

## 5. Identity vs Equality (Recap from Day 1)

- `==` compares **values**
- `is` compares **identity** (same object in memory)

```python
a = [1, 2]
b = [1, 2]

print(a == b)   # True  -> same values
print(a is b)   # False -> different objects in memory
```

---

## 6. Operator Precedence (Common Trap)

Python evaluates operators in a fixed order — `*` and `/` bind tighter than `+` and `-`.

```python
result = 2 + 3 * 4       # 14, not 20 -> * happens before +
result2 = (2 + 3) * 4    # 20 -> parentheses override precedence
```

**Rule of thumb:** when unsure, use parentheses — it costs nothing and removes ambiguity.

---

## Practice Task

```python
# operators_check.py
a, b = 17, 5

print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"Is {a} even? {a % 2 == 0}")
print(f"Is {a} > {b} and {b} > 0? {a > b and b > 0}")
```

Predict each output before running it — `//` and `%` trip people up the most.
