# Sets

## What Is a Set?

A set is an **unordered, mutable** collection of **unique** elements. Duplicates are automatically removed, and elements must be hashable (like dict keys).

```python
nums = {1, 2, 3, 3, 2}
print(nums)   # {1, 2, 3}  <- duplicates dropped automatically

empty_set = set()   # NOT {} — that creates an empty dict!
```

---

## Creating Sets

```python
a = {1, 2, 3}
b = set([1, 2, 2, 3])       # from a list
c = set("hello")             # from a string -> {'h', 'e', 'l', 'o'}

print(b)   # {1, 2, 3}
print(c)   # {'h', 'e', 'l', 'o'}  (order not guaranteed)
```

---

## Adding and Removing Elements

| Method | Behavior |
|---|---|
| `.add(x)` | Add a single element |
| `.update(iterable)` | Add multiple elements |
| `.remove(x)` | Remove element; raises `KeyError` if missing |
| `.discard(x)` | Remove element; does nothing if missing |
| `.pop()` | Remove and return an arbitrary element |
| `.clear()` | Remove all elements |

```python
s = {1, 2, 3}

s.add(4)
print(s)          # {1, 2, 3, 4}

s.update([5, 6])
print(s)          # {1, 2, 3, 4, 5, 6}

s.remove(1)
print(s)          # {2, 3, 4, 5, 6}

s.discard(100)    # no error, even though 100 isn't in the set
```

---

## Set Operations (Math-style)

| Operation | Symbol | Method | Meaning |
|---|---|---|---|
| Union | `\|` | `.union()` | All elements from both sets |
| Intersection | `&` | `.intersection()` | Elements in both sets |
| Difference | `-` | `.difference()` | Elements in first set, not second |
| Symmetric difference | `^` | `.symmetric_difference()` | Elements in either, not both |

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # {1, 2, 3, 4, 5, 6}  union
print(a & b)   # {3, 4}              intersection
print(a - b)   # {1, 2}              difference (in a, not b)
print(a ^ b)   # {1, 2, 5, 6}        symmetric difference
```

---

## Why Use a Set?

1. **Removing duplicates fast**
```python
nums = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(nums))
print(unique)   # [1, 2, 3, 4]  (order may vary)
```

2. **Fast membership checks** — `in` on a set is O(1) average, vs O(n) for a list.
```python
big_list = list(range(1000000))
big_set = set(big_list)

999999 in big_set    # fast
999999 in big_list   # much slower for large data
```

3. **Set algebra** — comparing two collections (e.g., common tags, shared followers).

---

## Membership and Length

```python
s = {1, 2, 3}

print(2 in s)       # True
print(5 not in s)   # True
print(len(s))       # 3
```

---

## Set Comprehension

```python
squares = {x**2 for x in range(6)}
print(squares)   # {0, 1, 4, 9, 16, 25}
```

---

## Frozenset — Immutable Set

A `frozenset` is like a set but can't be modified after creation — usable as a dict key or set element (regular sets can't be, since they're mutable/unhashable).

```python
fs = frozenset([1, 2, 3])
fs.add(4)   # ❌ AttributeError — frozensets have no .add()

d = {frozenset([1, 2]): "pair"}   # valid — frozenset is hashable
```

---

## Sets vs Lists vs Tuples — Quick Comparison

| Feature | List | Tuple | Set |
|---|---|---|---|
| Ordered | ✅ | ✅ | ❌ |
| Mutable | ✅ | ❌ | ✅ |
| Duplicates allowed | ✅ | ✅ | ❌ |
| Indexable (`s[0]`) | ✅ | ✅ | ❌ |
| Fast membership check | ❌ (O(n)) | ❌ (O(n)) | ✅ (O(1) avg) |

---

## Quick Reference

| Concept | Key takeaway |
|---|---|
| Uniqueness | Sets automatically drop duplicates |
| `{}` is a dict, not a set | Use `set()` for an empty set |
| Union/Intersection/Difference | `\|`, `&`, `-`, `^` |
| No indexing | Sets are unordered — `s[0]` doesn't work |
| Fast lookups | `in` is much faster on a set than a list |
| `frozenset` | Immutable, hashable version of a set |

---

## Practice Task

```python
# sets_check.py
class_a = {"Yash", "Raj", "Priya", "Aman"}
class_b = {"Priya", "Neha", "Aman", "Karan"}

# Students in both classes
print(class_a & class_b)      # {'Priya', 'Aman'}

# Students in class_a only
print(class_a - class_b)      # {'Yash', 'Raj'}

# All students combined (no duplicates)
print(class_a | class_b)      # {'Yash','Raj','Priya','Aman','Neha','Karan'}

# Students not in both (unique to each)
print(class_a ^ class_b)      # {'Yash','Raj','Neha','Karan'}
```

Predict each output before running — set order in printed output may vary, but the *contents* should match.
