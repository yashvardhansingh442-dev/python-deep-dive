# Tuples

## What Is a Tuple?

A tuple is an **ordered, immutable** collection — like a list, but once created it can't be changed. Written with parentheses `()` instead of square brackets.

```python
point = (3, 4)
colors = ("red", "green", "blue")
single = (5,)     # note the comma — without it, (5) is just an int in parens
empty = ()
```

---

## Indexing and Slicing

Same rules as lists and strings.

```python
point = (10, 20, 30, 40)

print(point[0])     # 10
print(point[-1])    # 40
print(point[1:3])   # (20, 30)
```

---

## Tuples Are Immutable

```python
t = (1, 2, 3)
t[0] = 99     # ❌ TypeError — tuples can't be changed in place
```

If you need a "changed" version, you build a new tuple:

```python
t = (1, 2, 3)
t = (99,) + t[1:]
print(t)      # (99, 2, 3)
```

**Caveat:** if a tuple contains a mutable object (like a list), that inner object can still be mutated — only the tuple's own structure (what it points to) is locked.

```python
t = (1, [2, 3])
t[1].append(4)
print(t)      # (1, [2, 3, 4])  <- allowed, the list inside changed, not the tuple itself
```

---

## Why Use a Tuple Instead of a List?

| Reason | Explanation |
|---|---|
| Immutability | Guarantees the data won't be accidentally modified |
| Performance | Slightly faster and more memory-efficient than lists |
| Hashable | Can be used as dictionary keys or set elements (if all elements are also hashable) |
| Semantic meaning | Signals "this is a fixed record," not a growing collection |

```python
locations = {
    (28.6, 77.2): "Delhi",
    (19.0, 72.8): "Mumbai"
}
# tuples as dict keys — a list here would raise TypeError
```

---

## Tuple Unpacking

```python
point = (3, 4)
x, y = point
print(x, y)   # 3 4

first, *rest = (1, 2, 3, 4)
print(first, rest)   # 1 [2, 3, 4]
```

This is the same mechanism behind the swap trick from the Variables notes:

```python
a, b = 5, 10
a, b = b, a   # Python builds the tuple (b, a) then unpacks it into a, b
```

---

## Common Tuple Operations

| Operation | Example | Result |
|---|---|---|
| `len(t)` | `len((1,2,3))` | `3` |
| `in` | `2 in (1,2,3)` | `True` |
| `+` (concatenation) | `(1,2) + (3,4)` | `(1,2,3,4)` |
| `*` (repetition) | `(1,2) * 2` | `(1,2,1,2)` |
| `.count(x)` | `(1,2,2,3).count(2)` | `2` |
| `.index(x)` | `(1,2,3).index(2)` | `1` |

```python
t = (1, 2, 2, 3)
print(t.count(2))   # 2
print(t.index(3))   # 3
```

---

## Tuples vs Lists — Quick Comparison

| Feature | List | Tuple |
|---|---|---|
| Mutable | ✅ Yes | ❌ No |
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` |
| Hashable (usable as dict key) | ❌ No | ✅ Yes (if contents are hashable) |
| Use case | Data that changes | Fixed records, coordinates, dict keys |

---

## Quick Reference

| Concept | Key takeaway |
|---|---|
| Immutability | Can't reassign elements — build a new tuple instead |
| Single-element tuple | Needs a trailing comma: `(5,)` |
| Hashability | Tuples (of hashable items) can be dict keys / set elements |
| Unpacking | `x, y = point` — same mechanism as the swap trick |
| Mutable contents | A list *inside* a tuple can still be mutated |

---

## Practice Task

```python
# tuples_check.py
point = (4, 7)
x, y = point
print(f"x={x}, y={y}")            # x=4, y=7

coords = {(0,0): "origin", (1,1): "diagonal"}
print(coords[(0,0)])              # origin

nested = (1, [2, 3])
nested[1].append(4)
print(nested)                     # (1, [2, 3, 4])

try:
    nested[0] = 99
except TypeError as e:
    print("Can't modify tuple:", e)
```

Predict each output before running — especially what happens with the nested list vs. the direct tuple element.
