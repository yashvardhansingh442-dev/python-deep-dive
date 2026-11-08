# File I/O

## What Is File I/O?

File I/O (Input/Output) lets a program read data from files and write data to files — for saving results, loading configs, processing datasets, etc.

---

## Opening a File — `open()`

```python
f = open("data.txt", "r")   # open in read mode
content = f.read()
f.close()                    # always close when done manually
```

| Mode | Meaning |
|---|---|
| `"r"` | Read (default) — file must exist |
| `"w"` | Write — creates file if missing, **overwrites** if it exists |
| `"a"` | Append — adds to the end, creates file if missing |
| `"x"` | Create — fails if file already exists |
| `"r+"` | Read and write |
| `"b"` (suffix) | Binary mode, e.g. `"rb"`, `"wb"` |

---

## The `with` Statement (Preferred Way)

Using `with` automatically closes the file, even if an error occurs — always prefer this over manual `open()`/`close()`.

```python
with open("data.txt", "r") as f:
    content = f.read()

# file is automatically closed here, even if read() raised an error
print(content)
```

---

## Reading Files

```python
# Read entire file as one string
with open("data.txt", "r") as f:
    content = f.read()

# Read all lines into a list
with open("data.txt", "r") as f:
    lines = f.readlines()   # ['line1\n', 'line2\n', ...]

# Read one line at a time (memory-efficient for large files)
with open("data.txt", "r") as f:
    line = f.readline()

# Iterate line by line (most common, most memory-efficient)
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())   # .strip() removes the trailing newline
```

---

## Writing Files

```python
# "w" mode — overwrites the file completely
with open("output.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("Second line\n")

# "a" mode — appends without erasing existing content
with open("output.txt", "a") as f:
    f.write("This gets added at the end\n")
```

**Trap:** `"w"` mode erases the file's existing content immediately when opened — even before you write anything.

```python
# ❌ this empties output.txt even if you never call f.write()
with open("output.txt", "w") as f:
    pass
```

---

## Writing Multiple Lines

```python
lines = ["apple\n", "banana\n", "cherry\n"]

with open("fruits.txt", "w") as f:
    f.writelines(lines)
```

---

## Handling Missing Files Safely

```python
try:
    with open("missing.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File does not exist")
```

---

## Working with CSV-like Data (Manual Approach)

```python
with open("students.csv", "r") as f:
    for line in f:
        name, age, gpa = line.strip().split(",")
        print(f"{name} is {age} years old, GPA: {gpa}")
```

*(You'll use the `csv` module or Pandas for real CSV work — this is just the raw-text version to understand what's happening underneath.)*

---

## Checking If a File Exists (Without Exceptions)

```python
import os

if os.path.exists("data.txt"):
    print("File found")
else:
    print("File not found")
```

---

## Quick Reference

| Concept | Key takeaway |
|---|---|
| `with open(...) as f` | Always prefer this — auto-closes the file |
| `"r"`, `"w"`, `"a"` | Read, write (overwrite), append |
| `.read()` | Whole file as one string |
| `.readlines()` | List of lines |
| `for line in f` | Most memory-efficient way to process large files |
| `"w"` mode danger | Opening in `"w"` erases existing content immediately |
| `os.path.exists()` | Check for a file without triggering an exception |

---

## Practice Task

```python
# file_io_check.py

# 1. Write some lines to a file
with open("notes_practice.txt", "w") as f:
    f.write("Day 1: Learned variables\n")
    f.write("Day 2: Learned data types\n")
    f.write("Day 3: Learned operators\n")

# 2. Read and print each line, numbered
with open("notes_practice.txt", "r") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}. {line.strip()}")

# 3. Append a new line
with open("notes_practice.txt", "a") as f:
    f.write("Day 4: Learned conditionals\n")

# 4. Count total lines
with open("notes_practice.txt", "r") as f:
    line_count = len(f.readlines())
print(f"Total lines: {line_count}")   # 4
```

Predict the final line count before running, and confirm the append didn't overwrite the earlier lines.
