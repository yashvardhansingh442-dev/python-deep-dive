**What is a variable?**

A variable is a name that points to a value stored in memory. 
In Python, you don't declare types — just assign and go.

name = "Yash"          # str
age  = 21              # int
gpa  = 8.5             # float
active = True          # bool

Python is dynamically typed — the type is attached to the value, not the variable name.

**Multiple assignment**

x = y = z = 0          # all three → 0

a, b, c = 1, 2, 3      # unpacking

first, *rest = [10, 20, 30, 40]
# first = 10, rest = [20, 30, 40]
Swap without temp
a, b = 5, 10
a, b = b, a   # a=10, b=5  ✓
This is Python's classic one-liner swap — no temp variable needed.
