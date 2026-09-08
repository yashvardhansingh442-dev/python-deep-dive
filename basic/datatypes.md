**What are data types?**
A data type tells Python what kind of value a variable holds, and what
operations are valid on it.

**Basic built-in types**
name    = "Yash"        # str   — text
age     = 21            # int   — whole numbers
gpa     = 8.5           # float — decimal numbers
active  = True          # bool  — True/False
nothing = None          # NoneType — absence of a value

**Checking type**
print(type(name))    # <class 'str'>
print(type(age))     # <class 'int'>

**Type casting (converting between types)**
x = "10"
y = int(x)      # "10" -> 10
z = str(25)     # 25   -> "25"
f = float("3.14")  # "3.14" -> 3.14

**Mutable vs Immutable types**
Immutable (can't be changed in place): int, float, str, bool, tuple
Mutable (can be changed in place): list, dict, set

s = "hello"
s[0] = "H"     # ❌ TypeError — strings are immutable

lst = [1, 2, 3]
lst[0] = 99    # ✅ works — lists are mutable → [99, 2, 3]

**Why this matters**
Immutable objects are safe to share/pass around — nothing else can silently
change them under you. Mutable objects can be changed by any reference to
them, which is a common source of bugs (see the linked-list append example
from Day 1's identity/mutability notes).
