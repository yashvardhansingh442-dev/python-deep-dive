# Strings

## What Is a String?

A string is a sequence of characters, enclosed in quotes. Strings are **immutable** — once created, they can't be changed in place (recap from Data Types).

```python
name = "Yash"
message = 'Hello, world!'
multiline = """This spans
multiple lines"""
```

---

## Indexing and Slicing

Strings are indexed from `0`, and support negative indexing from the end.

```python
s = "Python"

print(s[0])     # 'P'
print(s[-1])    # 'n'
print(s[2:5])   # 'tho'   (slice: start inclusive, end exclusive)
print(s[:3])    # 'Pyt'
print(s[3:])    # 'hon'
print(s[::-1])  # 'nohtyP'  (reversed string)
```

---

## Strings Are Immutable

```python
s = "hello"
s[0] = "H"     # ❌ TypeError

s = "H" + s[1:]   # ✅ create a new string instead
print(s)          # "Hello"
```

---

## Common String Methods

| Method | Purpose | Example |
|---|---|---|
| `.upper()` | Convert to uppercase | `"abc".upper()` → `"ABC"` |
| `.lower()` | Convert to lowercase | `"ABC".lower()` → `"abc"` |
| `.strip()` | Remove leading/trailing whitespace | `"  hi  ".strip()` → `"hi"` |
| `.replace(old, new)` | Replace substring | `"cat".replace("c","b")` → `"bat"` |
| `.split(sep)` | Split into a list | `"a,b,c".split(",")` → `['a','b','c']` |
| `.join(iterable)` | Join list into a string | `"-".join(["a","b"])` → `"a-b"` |
| `.find(sub)` | Index of first match, or `-1` | `"hello".find("l")` → `2` |
| `.startswith(sub)` | Check prefix | `"hello".startswith("he")` → `True` |
| `.endswith(sub)` | Check suffix | `"hello".endswith("lo")` → `True` |
| `.count(sub)` | Count occurrences | `"banana".count("a")` → `3` |
| `len(s)` | Length of the string | `len("hello")` → `5` |

```python
text = "  Hello, World!  "

print(text.strip())            # "Hello, World!"
print(text.strip().lower())    # "hello, world!"
print(text.strip().split(","))  # ['Hello', ' World!']
```

---

## String Formatting

### f-strings (preferred, Python 3.6+)

```python
name = "Yash"
age = 21
print(f"{name} is {age} years old")
# Yash is 21 years old

print(f"Next year: {age + 1}")   # expressions work inside {}
# Next year: 22
```

### `.format()` (older style)

```python
print("{} is {} years old".format(name, age))
```

### `%` formatting (legacy)

```python
print("%s is %d years old" % (name, age))
```

---

## String Concatenation and Repetition

```python
first = "Py"
second = "thon"

print(first + second)   # "Python"
print("ab" * 3)          # "ababab"
```

**Note:** concatenating strings in a loop with `+` is inefficient for large amounts of text — use `.join()` instead.

```python
# ❌ slow for many iterations
result = ""
for word in ["a", "b", "c"]:
    result += word

# ✅ better
result = "".join(["a", "b", "c"])
```

---

## Checking String Content

```python
s = "Python3"

print(s.isalpha())    # False (contains a digit)
print(s.isdigit())    # False
print("123".isdigit()) # True
print(s.isalnum())    # True (letters + digits, no symbols)
```

---

## Iterating Over a String

```python
for char in "abc":
    print(char)
# a b c
```

---

## Quick Reference

| Concept | Key takeaway |
|---|---|
| Indexing/slicing | `s[start:end:step]`, negative indices count from the end |
| Immutability | Strings can't be changed in place — operations return new strings |
| f-strings | `f"{variable}"` — preferred formatting method |
| `.split()` / `.join()` | Convert between strings and lists |
| Loop concatenation | Prefer `.join()` over repeated `+=` |

---

## Practice Task

```python
# strings_check.py
sentence = "  The Quick Brown Fox  "

cleaned = sentence.strip()
print(cleaned)                     # "The Quick Brown Fox"
print(cleaned.lower())             # "the quick brown fox"
print(cleaned.split())             # ['The', 'Quick', 'Brown', 'Fox']
print("-".join(cleaned.split()))   # "The-Quick-Brown-Fox"
print(cleaned[::-1])               # "xoF nworB kciuQ ehT"
print(cleaned.replace("Fox", "Cat"))  # "The Quick Brown Cat"
```

Predict each output before running — pay attention to what `.strip()` does (and doesn't) remove.
