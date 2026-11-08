# Loops

## What Are Loops?

Loops let you repeat a block of code multiple times — instead of writing the same line over and over.

---

## `for` Loop

Used when you know how many times to iterate, or you're iterating over a sequence (list, string, range, etc.).

```python
for i in range(5):
    print(i)
# 0 1 2 3 4
```

### `range()` variations

```python
range(5)         # 0, 1, 2, 3, 4
range(2, 6)      # 2, 3, 4, 5
range(0, 10, 2)  # 0, 2, 4, 6, 8  (step of 2)
range(5, 0, -1)  # 5, 4, 3, 2, 1  (counting down)
```

### Iterating over a list

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

### Iterating with index — `enumerate()`

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
# 0 apple
# 1 banana
# 2 cherry
```

### Iterating over a string

```python
for char in "abc":
    print(char)
# a b c
```

---

## `while` Loop

Used when you don't know in advance how many iterations you need — it runs as long as a condition stays `True`.

```python
count = 0

while count < 5:
    print(count)
    count += 1
# 0 1 2 3 4
```

**Watch out:** if the condition never becomes `False`, you get an infinite loop.

```python
# ❌ infinite loop — count never changes
count = 0
while count < 5:
    print(count)
```

---

## `break` — Exit the Loop Early

```python
for num in range(10):
    if num == 5:
        break
    print(num)
# 0 1 2 3 4
```

---

## `continue` — Skip to the Next Iteration

```python
for num in range(6):
    if num % 2 == 0:
        continue
    print(num)
# 1 3 5
```

---

## `else` Clause on Loops

The `else` block runs only if the loop completes **without** hitting a `break`. Rarely used, but useful for search patterns.

```python
for num in range(2, 10):
    if num % 7 == 0:
        print("Found a multiple of 7")
        break
else:
    print("No multiple of 7 found")
```

---

## Nested Loops

A loop inside another loop — the inner loop completes fully for each single iteration of the outer loop.

```python
for i in range(3):
    for j in range(2):
        print(i, j)
# 0 0
# 0 1
# 1 0
# 1 1
# 2 0
# 2 1
```

---

## List Comprehension (Compact Loop for Building Lists)

```python
squares = [x ** 2 for x in range(5)]
print(squares)   # [0, 1, 4, 9, 16]

evens = [x for x in range(10) if x % 2 == 0]
print(evens)     # [0, 2, 4, 6, 8]
```

This is a preview — worth knowing early since it replaces a lot of manual `for` + `.append()` patterns.

---

## Quick Reference

| Concept | Key takeaway |
|---|---|
| `for` | Iterate over a known sequence or range |
| `while` | Repeat while a condition holds — watch for infinite loops |
| `break` | Exit the loop immediately |
| `continue` | Skip the rest of this iteration, move to the next |
| `enumerate()` | Get index + value together while iterating |
| `else` on loops | Runs only if the loop finished without `break` |
| List comprehension | `[expr for item in iterable if condition]` |

---

## Practice Task

```python
# loops_check.py

# 1. Print all even numbers from 1 to 20 using a for loop
for num in range(1, 21):
    if num % 2 == 0:
        print(num)

# 2. Sum numbers from 1 to 100 using a while loop
total = 0
n = 1
while n <= 100:
    total += n
    n += 1
print(total)   # 5050

# 3. Find the first number divisible by both 3 and 5, under 100
for num in range(1, 100):
    if num % 3 == 0 and num % 5 == 0:
        print(num)
        break
```

Predict each output before running — especially the `while` sum, since off-by-one errors are the most common loop bug.
