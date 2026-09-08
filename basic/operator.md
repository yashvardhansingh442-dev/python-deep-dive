**What are operators?**
Operators perform actions on values (operands) — math, comparisons, logic, etc.

**Arithmetic operators**
a, b = 10, 3
print(a + b)   # 13   addition
print(a - b)   # 7    subtraction
print(a * b)   # 30   multiplication
print(a / b)   # 3.333...  true division (always float)
print(a // b)  # 3    floor division (drops remainder)
print(a % b)   # 1    modulus (remainder)
print(a ** b)  # 1000 exponentiation

**Comparison operators** (return bool)
print(a == b)   # False — equal to
print(a != b)   # True  — not equal to
print(a > b)    # True
print(a < b)    # False
print(a >= b)   # True
print(a <= b)   # False

**Logical operators**
x, y = True, False
print(x and y)   # False — both must be True
print(x or y)    # True  — at least one True
print(not x)     # False — inverts

**Assignment operators (shorthand)**
n = 5
n += 1   # n = n + 1 -> 6
n -= 1   # n = n - 1 -> 5
n *= 2   # n = n * 2 -> 10
n //= 3  # n = n // 3 -> 3

**Identity vs equality (recap from Day 1)**
a = [1, 2]
b = [1, 2]
print(a == b)   # True  -> same values
print(a is b)   # False -> different objects in memory

**Operator precedence (common trap)**
result = 2 + 3 * 4      # 14, not 20 — * before +
result2 = (2 + 3) * 4   # 20 — parentheses override precedence
