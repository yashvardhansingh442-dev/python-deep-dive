# Python Deep Dive

[![CI](https://github.com/yashvardhansingh442-dev/python-deep-dive/actions/workflows/ci.yml/badge.svg)](https://github.com/yashvardhansingh442-dev/python-deep-dive/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active%20learning-orange)

**Learning Python properly, in public.** This repo is where I study Python from the basics up to how it works underneath, write down what I learn, build projects with it, and keep every step visible: the notes, the experiments, the mistakes and the fixes.

It has two audiences: **me**, because explaining something in writing is the fastest way to find out whether I really understand it, and **you**, if you are learning Python and want to see what the process actually looks like instead of only the polished result.

---

## Table of contents

1. [Why this repo exists](#1-why-this-repo-exists)
2. [The goal](#2-the-goal)
3. [What makes it different](#3-what-makes-it-different)
4. [How the learning path works](#4-how-the-learning-path-works)
5. [What is in the repo today](#5-what-is-in-the-repo-today)
6. [How to use this repo](#6-how-to-use-this-repo)
7. [Run it yourself](#7-run-it-yourself)
8. [Quality and automation](#8-quality-and-automation)
9. [Roadmap](#9-roadmap)
10. [Feedback and contributing](#10-feedback-and-contributing)
11. [About](#11-about)

---

## 1. Why this repo exists

Most places to learn Python fall into one of two groups:

- **Tutorials** that explain everything neatly and never show a single mistake. You finish them feeling like you understand, then freeze in front of an empty file.
- **Code dumps** with no explanation. You can read the result, but you cannot tell how anyone got there or why a decision was made.

Neither shows how learning actually goes: you read something, think you understand it, build something, and it breaks in a way you did not expect. The real understanding comes from working out why.

This repo keeps that whole loop in one place, so that the thinking is as visible as the code.

---

## 2. The goal

**Short version:** go from "I can follow a tutorial" to "I can build, debug and explain real Python," and leave a clear public record of the journey.

Concretely, the repo is working towards four things:

| Goal | What it means in practice |
|---|---|
| **Solid fundamentals** | Every core Python topic written up in my own words, with small runnable examples |
| **Real projects** | Programs that do something useful, built step by step and improved over time |
| **Depth, not just syntax** | Understanding what Python is doing underneath: memory, scope, the data model, performance |
| **Professional habits** | Linting, type checking, tests and CI from the start, so the work stays correct as it grows |

The end state is a portfolio that shows not only *what* I built but *how I think*: how I break a problem down, test an idea, find a bug and fix it.

---

## 3. What makes it different

These are the principles the repo is built around. Where something is not done yet, section 5 and the [roadmap](#9-roadmap) say so plainly.

**It shows the process, not only the result.**
Notes, experiments and projects sit side by side. Dead ends and wrong guesses are allowed to stay in, because that is where most of the learning happens.

**Explain it to learn it.**
Each topic is written as an explanation for someone else. If I cannot explain a concept simply with a working example, I do not understand it yet, and the gap becomes my next thing to study.

**Small steps, always running.**
Examples are short and executable. You can copy any script, run it, change it and see what happens.

**Built to stay correct.**
Linting, strict type checking and tests run automatically on every push, on two Python versions. The goal is that the examples do not quietly rot.

**Honest about status.**
The README separates what exists today from what is planned. A learning repo that claims more than it contains is not much use to a learner.

**Connected, not scattered.**
The aim is that any topic can be followed from the idea (notes), to experiments (scripts), to real use (projects), to code you can reuse (`src/`).

---

## 4. How the learning path works

Each topic follows the same loop. This is the method I am trying to apply to everything in the repo:

```
 1. Read & write   ->  explain the concept in my own words        (curriculum/)
 2. Experiment     ->  small scripts to test what I think is true (learning-codes/)
 3. Build          ->  use it in a real project                   (projects/)
 4. Extract        ->  move reusable code into a tested package   (src/pydeep/)
 5. Verify         ->  tests + CI confirm it still works          (tests/)
```

When something breaks along the way, the plan is to keep it: the smallest example that reproduces the bug, why it happened, and the fix.

---

## 5. What is in the repo today

| Folder | Purpose | Status |
|---|---|---|
| [`curriculum/`](curriculum/) | Written notes, one file per core Python topic | 15 notes |
| [`learning-codes/`](learning-codes/) | Small experiment scripts: Python basics, NumPy, linear algebra, SciPy | about 30 scripts |
| [`projects/`](projects/) | Projects built with what I learn | 1 in progress |
| [`src/pydeep/`](src/pydeep/) | Reusable, typed, tested package | just started |
| [`tests/`](tests/) | Test suite run by CI | just started |

```
python-deep-dive/
├── curriculum/            # topic notes (markdown)
├── learning-codes/
│   ├── python/            # variables, f-strings, typecasting, input
│   ├── numpy/             # arrays, slicing, broadcasting, filtering, random numbers
│   ├── linalg/            # vectors, matrices, elimination, determinants
│   └── scipy/             # first notebook
├── projects/
│   └── numpy/SpendSense.py
├── src/pydeep/            # reusable package
├── tests/
├── .github/workflows/ci.yml
├── Makefile
└── pyproject.toml
```

### Curriculum

Each note covers what the concept is, short runnable examples, and common pitfalls.

| Area | Notes |
|---|---|
| **Basics** | [Variables](curriculum/variabale.md) · [Data types](curriculum/datatypes.md) · [Operators](curriculum/operator.md) |
| **Control flow** | [Conditionals](curriculum/conditionals.md) · [Loops](curriculum/loops.md) |
| **Data structures** | [Strings](curriculum/strings.md) · [Lists](curriculum/list.md) · [Tuples](curriculum/tuples.md) · [Sets](curriculum/sets.md) · [Dictionaries](curriculum/dictonaries.md) |
| **Functions** | [Functions](curriculum/functions.md) · [Scope, closures and the LEGB rule](curriculum/Function%20Scope%2C%20Closures%2C%20LEGB%20Rule.md) |
| **Real-world code** | [File I/O](curriculum/files_io.md) · [Exception handling](curriculum/exception_handling.md) |
| **Objects** | [OOP basics](curriculum/OOPs_baisc.md) |

### Experiments (`learning-codes/`)

- **`python/`**: variables, f-strings, type casting, user input
- **`numpy/`**: array creation, indexing and slicing, vectorized math, broadcasting, filtering, random numbers
- **`linalg/`**: vectors, matrices, Gaussian elimination, determinants, with a small experiment counting the steps elimination takes against recursive determinants
- **`scipy/`**: first notebook

### Projects

**SpendSense** ([`projects/numpy/SpendSense.py`](projects/numpy/SpendSense.py)) is a command-line spending tracker built on NumPy.

- **Today:** asks for a name, a number of days, daily amounts for four categories and a monthly income; validates every input; stores the data as a `(days, categories)` array.
- **Next:** summary report (totals per category, biggest-spend day, savings against income), a proper `main()` entry point, and tests.

---

## 6. How to use this repo

**If you are learning Python**

1. Read a [curriculum](curriculum/) note on a topic.
2. Run the matching scripts in [`learning-codes/`](learning-codes/) and change them to see what breaks.
3. Try to build a small version yourself before reading how SpendSense does it.
4. Compare your attempt to the code here, and note what differs.

**If you are a recruiter or reviewer**

- [`curriculum/`](curriculum/) shows how I explain concepts.
- [`projects/`](projects/) and [`src/`](src/) show how I build and structure code.
- The commit history and [CI](.github/workflows/ci.yml) show how I work over time.

**If you are on a similar journey**

Fork it, copy the structure, and keep your own log. The method matters more than my particular notes.

---

## 7. Run it yourself

Requires **Python 3.11 or newer**.

```bash
git clone https://github.com/yashvardhansingh442-dev/python-deep-dive.git
cd python-deep-dive
make install     # creates .venv and installs the dev tools
make check       # ruff lint, mypy --strict on src/, pytest (same as CI)
```

Run a script:

```bash
.venv/bin/python projects/numpy/SpendSense.py
```

`make help` lists all commands:

| Command | What it does |
|---|---|
| `make install` | Create `.venv` and install dependencies |
| `make lint` | Lint with ruff |
| `make format` | Auto-format and fix lint issues |
| `make typecheck` | Strict type-check `src/` with mypy |
| `make test` | Run the test suite |
| `make cov` | Tests with coverage (fails under 85%) |
| `make check` | Everything CI runs |
| `make clean` | Remove caches and build output |

---

## 8. Quality and automation

On every push and pull request, GitHub Actions runs `make check` on **Python 3.11 and 3.12**:

- **ruff** for linting and import order
- **mypy --strict** on the reusable package in `src/`
- **pytest** for tests

The scripts in `learning-codes/` are study notes, so they follow the lint rules except for line length, and the markdown notes are left exactly as written.

---

## 9. Roadmap

| Phase | Focus | Status |
|---|---|---|
| **1. Foundations** | Core Python notes and basic scripts | Done |
| **2. Numerical Python** | NumPy and linear algebra experiments | In progress |
| **3. First real project** | Finish SpendSense with a report and tests | Next |
| **4. Package and tests** | Move reusable code into `src/pydeep/` with proper tests | Planned |
| **5. Debugging casebook** | Small broken examples with a failing test, the cause and the fix | Planned |
| **6. Rebuild to understand** | Own versions of an LRU cache and a dataclass, tested against the real ones | Planned |
| **7. Under the hood** | Write-ups on bytecode, memory, the GIL and `asyncio`, backed by experiments | Planned |
| **8. Tidy-up** | Consistent file naming, a progress tracker | Planned |

---

## 10. Feedback and contributing

This is a personal learning repo, but feedback is welcome. If you spot a mistake in a note, a better way to explain something, or a topic I should cover, please open an issue or a pull request. Corrections are the fastest way I learn.

---

## 11. About

Built by [Yash](https://github.com/yashvardhansingh442-dev) while learning Python in depth. Licensed under the [MIT License](LICENSE).
