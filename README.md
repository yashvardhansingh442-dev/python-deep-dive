# Python Deep Dive

A repo where I put everything I build, break and fix while learning Python properly. Projects, bug write-ups, from-scratch rebuilds, experiments and notes, all in one place, all with proof that they work.

I made it for two reasons: to show my work, and so anyone reading it can learn from the same work.

---

## Table of contents

1. [Why this repo exists](#1-why-this-repo-exists)
2. [What makes it special](#2-what-makes-it-special)
3. [How the repo is structured](#3-how-the-repo-is-structured)
4. [What you can learn from this](#4-what-you-can-learn-from-this)
5. [Run it yourself](#5-run-it-yourself)

---

## 1. Why this repo exists

Most Python repos fall into one of two types. Either they are tutorials that explain everything neatly and never show a single mistake, or they are project dumps with no explanation of how anything was figured out.

Neither shows how learning actually goes. You read something, you think you understand it, you build something, and it breaks in a way you didn't expect. The real understanding comes from fixing that.

So this repo keeps all of it:

- the things I built
- the things that broke while building them
- how I found out why
- what I rebuilt from scratch to be sure I understood it

It is my portfolio, and it is also a place you can learn from, because every piece of work explains its reasoning instead of just showing the result.

---

## 2. What makes it special

**Every claim has proof.** If I say I understand something, there is a test, a benchmark, a bytecode dump or a merged pull request next to it. Nothing here is just "trust me".

**The bugs are the main content.** The `fixes/` folder is a debugging casebook. Each fix keeps the broken code and a failing test, so you can try to solve it first and then compare with my solution.

**Things are rebuilt, not just used.** I recreate pieces of Python (a cache, an event loop, a dataclass, a hash table) and test them against the real thing. This is the quickest way I know to find out whether I really understand something.

**Nothing is hidden.** Every project has a "what broke" section. Dead ends and wrong guesses stay in the write-ups, because that is where most of the learning is.

**Everything stays connected.** A project links to the deep dive behind it, the bugs I hit while building it, and the experiments that tested my assumptions. You can follow any topic from explanation to real use.

**It stays working.** CI runs linting, strict type checks and tests on every push, so the examples and fixes do not rot.

---

## 3. How the repo is structured

```
python-deep-dive/
├── projects/
├── fixes/
├── contributions/
├── deep-dives/
├── implementations/
├── experiments/
├── benchmarks/
├── cheatsheets/
├── journal/
├── to-learn/
├── src/pydeep/
├── scripts/
└── tests/
```

### `projects/`: things I built

Larger pieces of work, each written up as a case study with the same sections: the problem, the design, the key decisions and why I made them, what broke, the results, and what I would do differently.

| Project | What it covers |
|---|---|
| `01-cli-task-manager` | Packaging, typing, testing, clean command-line design |
| `02-async-web-scraper` | Concurrency, retries, back-pressure, graceful shutdown |
| `03-mini-orm` | Descriptors, metaclasses, generating SQL |
| `04-plugin-framework` | Abstract base classes, dynamic loading, `__init_subclass__` |
| `05-interpreter` | Lexer, parser and a small bytecode VM |

### `fixes/`: bugs I hit and solved

The debugging casebook. Each entry follows the same steps: what went wrong, the smallest example that reproduces it, how I investigated, the root cause, the fix, the proof, and the lesson.

```
fixes/
├── concurrency-bugs/
├── memory-leaks/
├── performance/
├── gotchas/                  # mutable defaults, late binding, and similar traps
└── <date>-<short-name>/
    ├── README.md             # the full write-up
    ├── broken/               # buggy code + a failing test
    └── fixed/                # corrected code + passing test
```

### `contributions/`: fixes to other people's code

Bugs I found and fixed in open-source projects. Each write-up links the issue or pull request and explains how I tracked the problem down in code I did not write.

### `deep-dives/`: how things work underneath

Long-form explanations of one topic each, such as decorators and descriptors, the GIL, the `asyncio` event loop, and CPython bytecode. Every explanation is backed by an experiment or real output, never just prose.

### `implementations/`: rebuilt from scratch

My own versions of things Python already provides, each with tests that compare it with the real one, plus a short note on what I learned from the differences.

- `lru_cache`
- `event_loop`
- `dataclass_lite`
- `dict_hash_table`

### `experiments/` and `benchmarks/`: questions and measurements

Small scripts that each answer one question about Python, with the result written at the top of the file. Benchmarks store the actual numbers and charts, so speed claims can be checked.

### `cheatsheets/`: one-page references

Short summaries you can keep open while coding.

### `journal/` and `to-learn/`: the learning log

`journal/` has dated entries of what I learned and shipped. `to-learn/` holds my backlog of topics and my open questions, so you can see what I am working on next and what I still do not understand.

### `src/pydeep/`, `scripts/`, `tests/`: the supporting code

Reusable code pulled out of the projects, helper scripts, and the test suite that CI runs.

---

## 4. What you can learn from this

Each topic below points to where it is explained, rebuilt, used and debugged, so you can go from theory to real code.

| If you want to learn | Read | Then rebuild | Then see it used | Then see it break |
|---|---|---|---|---|
| **How decorators and descriptors work** | `deep-dives/decorators-and-descriptors` | `implementations/dataclass_lite` | `projects/03-mini-orm` | `fixes/gotchas` |
| **Async and the event loop** | `deep-dives/asyncio-event-loop` | `implementations/event_loop` | `projects/02-async-web-scraper` | `fixes/concurrency-bugs` |
| **Threads, processes and the GIL** | `deep-dives/gil-and-threading` | `experiments/` | `benchmarks/` | `fixes/concurrency-bugs` |
| **Python's data model and memory** | `deep-dives/cpython-bytecode` | `implementations/dict_hash_table` | `projects/05-interpreter` | `fixes/memory-leaks` |
| **Writing code that is easy to extend** | `projects/04-plugin-framework` | `implementations/lru_cache` | `projects/01-cli-task-manager` | `fixes/gotchas` |

### Skills you can pick up

- **Debugging properly.** Reproduce the bug in the smallest example, form a guess, test it, and prove the fix with a test. Every entry in `fixes/` demonstrates this.
- **Reading what Python is really doing.** Using `dis`, `tracemalloc`, `cProfile` and `py-spy` to see bytecode, memory use and time spent.
- **Measuring before optimizing.** The benchmarks show before and after numbers instead of guesses.
- **Designing larger programs.** The project write-ups explain the trade-offs behind each decision, not just the final code.
- **Testing and tooling.** `pytest`, type checking with `mypy`, linting with `ruff`, and CI, all set up and working in the repo.
- **Reading other people's code.** The `contributions/` write-ups show how to find your way around an unfamiliar codebase and fix a real bug in it.

### Try the fixes yourself

Pick any entry in `fixes/`, run its failing test, and try to fix it before reading my solution:

```bash
make fix-demo F=<fix-name>
```

### Difficulty tags

Used across the repo so you know what you are getting into: 🟢 foundation, 🟡 intermediate, 🔴 advanced, ⚫ expert.

---

## 5. Run it yourself

```bash
git clone https://github.com/yashvardhansingh442-dev/python-deep-dive.git
cd python-deep-dive
make install     # creates .venv and installs everything
make check       # lint, strict type-check, tests (same as CI)
```

`make help` lists all commands. Requires Python 3.11 or newer.

---

Built by [Yash](https://github.com/yashvardhansingh442-dev). Licensed under [MIT](LICENSE).
