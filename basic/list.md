# Lists

## What Is a List?

A list is an **ordered, mutable** collection of items — can hold mixed types, duplicates, and grow/shrink after creation.

```python
fruits = ["apple", "banana", "cherry"]
mixed = [1, "two", 3.0, True]
empty = []
```

---

## Indexing and Slicing

Same rules as strings — 0-based, negative indices count from the end.

```python
nums = [10, 20, 30, 40, 50]

print(nums[0])     # 10
print(nums[-1])    # 50
print(nums[1:3])   # [20, 30]
print(nums[::-1])  # [50, 40, 30, 20, 10]
```

---

## Lists Are Mutable

```python
nums = [1, 2, 3]
nums[0] = 99
print(nums)   # [99, 2, 3]
```

---

## Common List Methods

| Method | Purpose | Example |
|---|---|---|
| `.append(x)` | Add item to the end | `nums.append(4)` |
| `.insert(i, x)` | Insert at index `i` | `nums.insert(1, 99)` |
| `.remove(x)` | Remove first matching value | `nums.remove(99)` |
| `.pop(i)` | Remove and return item at index (default: last) | `nums.pop()` |
| `.sort()` | Sort in place | `nums.sort()` |
| `.reverse()` | Reverse in place | `nums.reverse()` |
| `.extend(iterable)` | Add multiple items | `nums.extend([5, 6])` |
| `.index(x)` | Index of first match | `nums.index(3)` |
| `.count(x)` | Count occurrences | `nums.count(2)` |
| `.clear()` | Remove all items | `nums.clear()` |

```python
nums = [3, 1, 4, 1, 5]

nums.append(9)
print(nums)          # [3, 1, 4, 1, 5, 9]

nums.sort()
print(nums)          # [1, 1, 3, 4, 5, 9]

nums.remove(1)       # removes first "1" only
print(nums)          # [1, 3, 4, 5, 9]

last = nums.pop()
print(last, nums)    # 9  [1, 3, 4, 5]
```

---

## `sorted()` vs `.sort()`

`.sort()` mutates the list in place and returns `None`.
`sorted()` returns a **new** sorted list, leaving the original unchanged.

```python
nums = [3, 1, 2]

new_list = sorted(nums)
print(new_list)   # [1, 2, 3]
print(nums)       # [3, 1, 2]  <- unchanged

nums.sort()
print(nums)       # [1, 2, 3]  <- mutated
```

---

## Copying a List (Important Trap)

```python
a = [1, 2, 3]
b = a              # ❌ NOT a copy — b points to the same list
b.append(4)
print(a)           # [1, 2, 3, 4]  <- a changed too!

c = a.copy()       # ✅ actual shallow copy
# or: c = a[:]
# or: c = list(a)
c.append(5)
print(a)           # unaffected by changes to c
```

---

## List Comprehension

A compact way to build a list from an existing iterable.

```python
squares = [x ** 2 for x in range(5)]
print(squares)          # [0, 1, 4, 9, 16]

evens = [x for x in range(10) if x % 2 == 0]
print(evens)             # [0, 2, 4, 6, 8]

upper_names = [name.upper() for name in ["yash", "raj"]]
print(upper_names)       # ['YASH', 'RAJ']
```

---

## Nested Lists

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])   # 6  (row 1, column 2)

for row in matrix:
    for val in row:
        print(val, end=" ")
# 1 2 3 4 5 6 7 8 9
```

---

## Membership and Length

```python
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)      # True
print("mango" not in fruits)   # True
print(len(fruits))             # 3
```

---

## Quick Reference

| Concept | Key takeaway |
|---|---|
| Mutability | Lists can be changed in place — unlike strings/tuples |
| `.sort()` vs `sorted()` | In-place mutation vs new list |
| Copying | `b = a` shares the same object — use `.copy()`, `a[:]`, or `list(a)` |
| List comprehension | `[expr for item in iterable if condition]` |
| Nested lists | Index with `list[row][col]` |

---

## Practice Task

```python
# lists_check.py
scores = [88, 92, 79, 95, 60, 73]

print(max(scores))                     # 95
print(min(scores))                     # 60
print(sum(scores) / len(scores))       # average -> 81.166...

passing = [s for s in scores if s >= 75]
print(passing)                         # [88, 92, 79, 95]

scores.sort(reverse=True)
print(scores)                          # [95, 92, 88, 79, 73, 60]
```

Predict each output before running — especially the average and the sorted order.
