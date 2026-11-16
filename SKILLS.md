# Skills

A living record of what I can do in Python today, what I am still learning, and where the proof is in this repo. Every skill links to the file that shows it. If a skill has no link, it does not belong on this page yet.

> **Self-assessed.** Levels are my own honest judgement, not a certification. The evidence links are there so you can judge for yourself.

---

## How to read this page

| Level | Meaning |
|---|---|
| 🟢 **Working** | I use it without looking things up, and the repo has code or notes that show it |
| 🟡 **Learning** | I understand the idea and have examples, but I still make mistakes or need references |
| ⚪ **Planned** | On the roadmap, not started yet. No claim is made |

Last reviewed: **November 2026**

---

## Summary

| Area | Level | Evidence |
|---|---|---|
| [Python fundamentals](#1-python-fundamentals) | 🟢 Working | [`curriculum/`](curriculum/) |
| [Data structures](#2-data-structures) | 🟢 Working | [`curriculum/`](curriculum/) |
| [Functions and scope](#3-functions-and-scope) | 🟢 Working | [`functions.md`](curriculum/functions.md) |
| [Error handling and files](#4-error-handling-and-files) | 🟢 Working | [`exception_handling.md`](curriculum/exception_handling.md) |
| [Object-oriented basics](#5-object-oriented-basics) | 🟡 Learning | [`OOPs_baisc.md`](curriculum/OOPs_baisc.md) |
| [NumPy](#6-numpy) | 🟢 Working | [`learning-codes/numpy/`](learning-codes/numpy/) |
| [Linear algebra with code](#7-linear-algebra-with-code) | 🟡 Learning | [`learning-codes/linalg/`](learning-codes/linalg/) |
| [SciPy](#8-scipy) | ⚪ Planned | [`learning-codes/scipy/`](learning-codes/scipy/) |
| [Building a program](#9-building-a-program) | 🟡 Learning | [`SpendSense.py`](projects/numpy/SpendSense.py) |
| [Tooling and quality](#10-tooling-and-quality) | 🟡 Learning | [`ci.yml`](.github/workflows/ci.yml), [`Makefile`](Makefile) |
| [Git and GitHub](#11-git-and-github) | 🟢 Working | [commit history](../../commits/main) |
| [Testing](#12-testing) | ⚪ Planned | [`tests/`](tests/) has one smoke test so far |
| [Advanced Python](#13-advanced-python) | ⚪ Planned | see [roadmap](README.md#9-roadmap) |

---

## 1. Python fundamentals

🟢 **Working**

| Skill | What I can do | Evidence |
|---|---|---|
| Variables and naming | Create and reassign variables, explain that a name points to a value, follow naming rules | [`variabale.md`](curriculum/variabale.md), [`var.py`](learning-codes/python/var.py) |
| Data types | Use `int`, `float`, `str`, `bool`, check types with `type()` | [`datatypes.md`](curriculum/datatypes.md), [`datatype_check.py`](learning-codes/datatype_check.py) |
| Type casting | Convert between types, and know that implicit and explicit casting differ | [`typecasting.py`](learning-codes/python/typecasting.py) |
| Operators | Arithmetic, comparison, logical and assignment operators; identity versus equality; operator precedence | [`operator.md`](curriculum/operator.md) |
| User input and output | Read with `input()`, format with f-strings | [`inp-user.py`](learning-codes/python/inp-user.py), [`f-string.py`](learning-codes/python/f-string.py), [`rectangle_area.py`](learning-codes/python/rectangle_area.py) |
| Conditionals | `if` / `elif` / `else`, nested conditions, truthy and falsy values, ternary expressions | [`conditionals.md`](curriculum/conditionals.md) |
| Loops | `for`, `while`, `break`, `continue`, loop `else`, nested loops | [`loops.md`](curriculum/loops.md) |

---

## 2. Data structures

🟢 **Working**

| Skill | What I can do | Evidence |
|---|---|---|
| Strings | Indexing, slicing, immutability, common methods, formatting | [`strings.md`](curriculum/strings.md) |
| Lists | Mutate in place, slice, use methods, copy safely, build lists with comprehensions | [`list.md`](curriculum/list.md), [`loops.md`](curriculum/loops.md) |
| Tuples | Use them as immutable sequences, unpack them | [`tuples.md`](curriculum/tuples.md) |
| Sets | Remove duplicates, test membership, use set operations | [`sets.md`](curriculum/sets.md) |
| Dictionaries | Add, update, remove, nest, merge, use dictionary comprehensions | [`dictonaries.md`](curriculum/dictonaries.md) |
| Choosing the right one | Explain when to use a list, tuple, set or dictionary and why | the notes above |

---

## 3. Functions and scope

🟢 **Working**

| Skill | What I can do | Evidence |
|---|---|---|
| Defining functions | Parameters, return values, default and keyword arguments | [`functions.md`](curriculum/functions.md) |
| Flexible arguments | `*args` and `**kwargs`, and combining argument types | [`functions.md`](curriculum/functions.md) |
| Scope | Explain the LEGB rule, use `global` and `nonlocal` | [`Function Scope, Closures, LEGB Rule.md`](curriculum/Function%20Scope%2C%20Closures%2C%20LEGB%20Rule.md) |
| Closures | Build a closure-based counter | same note |
| Input validation | Write small helpers that keep asking until the input is valid | [`SpendSense.py`](projects/numpy/SpendSense.py) (`read_days`, `read_numbers`, `read_income`) |

---

## 4. Error handling and files

🟢 **Working**

| Skill | What I can do | Evidence |
|---|---|---|
| Exceptions | `try` / `except` / `else` / `finally`, catching specific exceptions, reading the exception object | [`exception_handling.md`](curriculum/exception_handling.md) |
| Raising errors | Raise built-in exceptions and define custom ones | same note |
| File I/O | Open files with `with`, read and write text, handle missing files safely | [`files_io.md`](curriculum/files_io.md) |
| Defensive input | Reject bad values (non-numbers, negatives, wrong counts) instead of crashing | [`SpendSense.py`](projects/numpy/SpendSense.py) |

---

## 5. Object-oriented basics

🟡 **Learning**

| Skill | What I can do | Evidence |
|---|---|---|
| Classes and objects | Define classes, `__init__`, instance methods | [`OOPs_baisc.md`](curriculum/OOPs_baisc.md) |
| Attributes | Tell class attributes from instance attributes | same note |
| Inheritance and encapsulation | Basic inheritance, convention-based privacy | same note |
| Dunder methods | Implement `__eq__` and `__repr__`, and explain `==` versus `is` | [`__eq__.py`](learning-codes/__eq__.py) |

**Still to learn:** properties, `__slots__`, abstract base classes, dataclasses, composition versus inheritance.

---

## 6. NumPy

🟢 **Working**

| Skill | What I can do | Evidence |
|---|---|---|
| Creating arrays | 0-D, 1-D and multi-dimensional arrays, `ndim` and `shape` | [`zero-dim-arr.py`](learning-codes/numpy/zero-dim-arr.py), [`single-dim-arr.py`](learning-codes/numpy/single-dim-arr.py), [`multi-dim-arr.py`](learning-codes/numpy/multi-dim-arr.py) |
| Indexing and slicing | Index across several dimensions, slice with steps, reverse | [`slicing.py`](learning-codes/numpy/slicing.py), [`multi-dim-indexing.py`](learning-codes/numpy/multi-dim-indexing.py) |
| Vectorized math | Scalar and element-wise arithmetic, math functions without loops | [`arthimetic-scalar.py`](learning-codes/numpy/arthimetic-scalar.py), [`element-wise-arthimetic.py`](learning-codes/numpy/element-wise-arthimetic.py), [`arthimetic-vectorized-math-func.py`](learning-codes/numpy/arthimetic-vectorized-math-func.py) |
| Aggregation | Sum, mean, standard deviation, variance, min, max, argmin, argmax, along an axis | [`aggregate-function.py`](learning-codes/numpy/aggregate-function.py) |
| Broadcasting | Explain the shape rules and use them on `(1, n)` and `(n, 1)` arrays | [`broadcasting.py`](learning-codes/numpy/broadcasting.py) |
| Filtering | Boolean masks, comparison operators, `np.where` | [`filtering.py`](learning-codes/numpy/filtering.py), [`comp-operator.py`](learning-codes/numpy/comp-operator.py) |
| Random numbers | Seeded generators, random integers, floats and uniform values | [`rand-num.py`](learning-codes/numpy/rand-num.py), [`uniform_rng.py`](learning-codes/numpy/uniform_rng.py) |

**Still to learn:** structured arrays, `np.einsum`, memory layout and views versus copies, performance profiling.

---

## 7. Linear algebra with code

🟡 **Learning**

| Skill | What I can do | Evidence |
|---|---|---|
| Vectors and matrices | Create and add vectors, build matrices | [`vectoradd.py`](learning-codes/linalg/vectoradd.py), [`firstmatrix.py`](learning-codes/linalg/firstmatrix.py), [`raw.py`](learning-codes/linalg/raw.py) |
| Solving systems | Solve small systems with elimination and with `np.linalg.solve`, and compare the answers | [`elimination.py`](learning-codes/linalg/elimination.py), [`elimination_method.py`](learning-codes/linalg/elimination_method.py), [`numpy_and_det.py`](learning-codes/linalg/numpy_and_det.py) |
| Classifying systems | Tell whether a system has one, none or infinitely many solutions | [`elimination.py`](learning-codes/linalg/elimination.py) |
| Visualizing equations | Plot a line and mark its intercepts with Matplotlib | [`equation.py`](learning-codes/linalg/equation.py) |
| Cost of algorithms | Measure how recursive determinants blow up compared with `np.linalg.solve`, and count elimination steps | [`det-exp.py`](learning-codes/linalg/det-exp.py), [`Counting_steps.py`](learning-codes/linalg/Counting_steps.py) |

**Still to learn:** eigenvalues, decompositions (LU, QR, SVD), numerical stability.

---

## 8. SciPy

⚪ **Planned**

No claims yet. [`main.ipynb`](learning-codes/scipy/main.ipynb) is only a placeholder notebook. I will add real SciPy work (optimization, statistics, interpolation) and then list skills here.

---

## 9. Building a program

🟡 **Learning**

| Skill | What I can do | Evidence |
|---|---|---|
| Structuring a script | Split a program into small functions with docstrings | [`SpendSense.py`](projects/numpy/SpendSense.py) |
| Combining inputs into arrays | Turn several validated inputs into a `(days, categories)` NumPy array with `np.column_stack` | same file |
| Planning in small steps | Build the input layer first, then the report | [README roadmap](README.md#9-roadmap) |
| Entry point | Use `main()` and `if __name__ == "__main__":` | same file |
| Separating logic from I/O | Input helpers take `input_fn`/`output_fn`, so they can be tested | [`inputs.py`](src/pydeep/inputs.py) |

**Still to learn:** command-line arguments, packaging a small tool.

---

## 10. Tooling and quality

🟡 **Learning**

| Skill | What I can do | Evidence |
|---|---|---|
| Project layout | `src/` layout, `pyproject.toml`, optional dependency groups | [`pyproject.toml`](pyproject.toml), [`src/pydeep/`](src/pydeep/) |
| Linting and formatting | Configure and run `ruff`, fix what it reports | [`pyproject.toml`](pyproject.toml) |
| Type checking | Run `mypy --strict` on a package | [`Makefile`](Makefile) |
| Automation | Write a GitHub Actions workflow with a Python version matrix | [`ci.yml`](.github/workflows/ci.yml) |
| Task running | Wrap common commands in a `Makefile` | [`Makefile`](Makefile) |
| Virtual environments | Create and use a `.venv` | [`Makefile`](Makefile) |

---

## 11. Git and GitHub

🟢 **Working**

| Skill | What I can do | Evidence |
|---|---|---|
| Daily workflow | Commit in small steps with clear messages and push to GitHub | [commit history](../../commits/main) |
| Repository hygiene | Maintain a `.gitignore`, a license, and a readable README | [`.gitignore`](.gitignore), [`LICENSE`](LICENSE), [`README.md`](README.md) |
| Line endings | Keep them consistent with `.gitattributes` | [`.gitattributes`](.gitattributes) |

---

## 12. Testing

⚪ **Planned**

The repo has a smoke test and a first real test file, [`test_inputs.py`](tests/test_inputs.py), for the input helpers. Testing stays Planned until fixtures and more cases are in.

**Plan:** `pytest` basics, fixtures, parametrized tests, testing code that reads input, measuring coverage.

---

## 13. Advanced Python

⚪ **Planned**

No claims yet. These are the topics I intend to study and then write up with experiments:

- Decorators and descriptors
- Generators and iterators
- The Python data model and memory (references, mutability, `id`, the garbage collector)
- Reading bytecode with `dis`
- Concurrency: threads, processes, the GIL, `asyncio`
- Profiling and performance (`cProfile`, `timeit`)
- Type hints in depth (generics, protocols)

---

## Current focus

1. Finish SpendSense: summary report, entry point, tests.
2. Move reusable pieces into `src/pydeep/` with real tests.
3. Start the debugging casebook: small broken examples, the cause and the fix.

---

## How this page is kept honest

- A skill is only listed if a file in this repo shows it.
- A skill moves from 🟡 to 🟢 only when I have used it in a project, not just in an example.
- When I find I was wrong about something, I change the level and say why.
- Corrections are welcome: open an issue if a claim here does not match the evidence.
