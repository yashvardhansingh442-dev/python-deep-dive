# 90-Day AGI Foundations Roadmap — v2.1 (Restructured)

**What changed from v2.0:** Fixed Week 7's day range (45–53, not 45–51 — Days 52–53 were listed under it but excluded from the header). Added explicit daily breakdowns for sections v2.0 only described at the week/pipeline level (Week 6 Pandas, Week 9 Agent Memory, Week 10 Observability, Capstone). Added setup commands, exit criteria per phase, and a master tracker.

---

## 1. Daily System

| Block | Duration | Purpose |
|---|---|---|
| 1 — Concept Learning | 20 min | Read/watch the day's topic. No coding yet. |
| 2 — Build / Coding | 40–60 min | Implement the concept + solve the assigned problem. |
| 3 — Git Commit + Notes | 5–10 min | Commit your work, write 2–3 lines of notes. |

**Total:** 65–90 min/day

**Commit message format:**
```
Day XX: Topic Name
```
Example: `Day 14: Implemented Linked List and Reverse Linked List`

**Rule:** If you miss a day, don't renumber — resume at the next calendar day with the Day XX label you missed. Catching up matters more than streak length.

---

## 2. Setup Checklist

| Tool | Purpose | Install |
|---|---|---|
| Python 3.11+ | Core language | `sudo apt install python3` |
| VS Code | Editor | apt/snap or .deb |
| Git | Version control | `sudo apt install git` |
| GitHub account | Remote repo + portfolio proof | — |
| NumPy | Arrays/linear algebra | `pip install numpy` |
| Pandas | Data wrangling | `pip install pandas` |
| Matplotlib | Plotting | `pip install matplotlib` |
| Scikit-learn | Classical ML | `pip install scikit-learn` |
| PyTorch | Deep learning | `pip install torch` |
| Jupyter | Notebooks | `pip install jupyter` |

---

## 3. Repository Structure

```
agi-foundations/
├── python-dsa/
│   ├── week1-python-core/
│   ├── week2-data-structures/
│   ├── week3-algorithms/
│   └── week4-trees-graphs-dp/
├── ml-foundations/
│   ├── week5-numpy/
│   ├── week6-pandas/
│   ├── week7-machine-learning/
│   └── week8-transformers/
├── agi-systems/
│   ├── week9-agent-memory/
│   ├── week10-observability/
│   ├── week11-reasoning/
│   └── week12-13-capstone/
├── notes/              # one .md file per day, 2-3 lines each
├── README.md           # roadmap summary + progress tracker
└── ROADMAP.md          # this file
```

---

## 4. Daily Workflow

1. Open `notes/dayXX.md`, write today's date + topic.
2. Block 1: read/watch the concept material.
3. Block 2: write code in the matching week folder.
4. Run/test the code.
5. `git add . && git commit -m "Day XX: Topic Name"`
6. `git push`
7. Add 2–3 lines to `notes/dayXX.md`: what you learned, what was hard.

---

## PHASE 1 — Python + DSA (Days 1–30)

**Exit criteria:** All 30 days committed individually (not batched), every LeetCode problem solved and pushed, Day 30 review written.

### Week 1 — Python Core (Days 1–7)

*Goal: Understand how Python actually works under the hood, not just syntax.*

| Day | Concept Learning | Build Task | LeetCode |
|---|---|---|---|
| 1 | `is` vs `==`, object identity, mutability | Custom class with manual `__eq__` comparisons | #1 Two Sum |
| 2 | Function scope, closures, LEGB rule | Closure-based counter function | #9 Palindrome Number |
| 3 | `*args`, `**kwargs`, mutable default trap | Function demonstrating the mutable-default bug + fix | #66 Plus One |
| 4 | Decorators | `@timer`, `@debug` | #344 Reverse String |
| 5 | Generators, `yield`, lazy evaluation | Infinite sequence generator | #26 Remove Duplicates |
| 6 | OOP dunder methods | Class with `__repr__`, `__str__`, `__eq__`, `__len__` | #242 Valid Anagram |
| 7 | Git basics | `init`/`add`/`commit`/`push`/`branch` — push this week's code | #387 First Unique Character |

### Week 2 — Data Structures (Days 8–14)

| Day | Concept Learning | Build Task | LeetCode |
|---|---|---|---|
| 8 | Context managers | Custom `with MyTimer():` | #20 Valid Parentheses |
| 9 | Exceptions | Custom exception hierarchy | #189 Rotate Array |
| 10 | Linked lists | Node + LinkedList class from scratch | #206 Reverse Linked List |
| 11 | Stacks | Stack from scratch | #225 Implement Stack Using Queues |
| 12 | Queues + Deque | Queue from scratch | #232 Implement Queue Using Stacks |
| 13 | Hash tables — collisions, chaining | Hash table from scratch with chaining | #49 Group Anagrams |
| 14 | Complexity analysis (O(1)→O(n²)) | Go back and annotate Big-O on every function from Days 1–13 | — |

### Week 3 — Algorithms (Days 15–21)

| Day | Concept Learning | Build Task | LeetCode |
|---|---|---|---|
| 15 | Recursion | Recursive Fibonacci + memoized version | #509 Fibonacci |
| 16 | Basic sorting | Bubble, Selection, Insertion sort | — |
| 17 | Advanced sorting | Merge Sort, Quick Sort | #215 Kth Largest Element |
| 18 | Binary search | Iterative + recursive | #704 Binary Search |
| 19 | Two pointers | — | #11 Container With Most Water |
| 20 | Sliding window | — | #3 Longest Substring Without Repeating Characters |
| 21 | Review day | Solve 2 Easy + 1 Medium, closed notes, timed | — |

### Week 4 — Trees, Graphs, DP (Days 22–30)

| Day | Concept Learning | Build Task | LeetCode |
|---|---|---|---|
| 22 | Binary trees | Inorder/preorder/postorder traversal | #102 Binary Tree Level Order Traversal |
| 23 | Binary Search Trees | Insert, delete, search | #98 Validate BST |
| 24 | Graphs | BFS + DFS | #200 Number of Islands |
| 25 | Greedy algorithms | — | #55 Jump Game |
| 26 | Dynamic Programming I | — | #70 Climbing Stairs |
| 27 | Dynamic Programming II | — | #62 Unique Paths |
| 28 | Iterator protocol | Mini dataset class: `__getitem__`, `__len__`, custom iterator | — |
| 29 | Mock test | 3 problems, closed notes | — |
| 30 | Phase 1 review | Write: What I Learned / Mistakes / Next Phase Goals | — |

---

## PHASE 2 — NumPy + Pandas + ML (Days 31–60)

**Exit criteria:** Working from-scratch Linear + Logistic Regression, a 2-layer MLP in both raw Python and PyTorch, a toy self-attention implementation, Day 60 review written.

### Week 5 — NumPy (Days 31–37)

*v2.0 listed this week's topics/builds in bulk — mapped 1:1 to days here.*

| Day | Concept | Build |
|---|---|---|
| 31 | Arrays & dtype | Array creation, dtype casting tests |
| 32 | Strides & views | Visualize how slicing creates views vs. copies |
| 33 | Broadcasting | Broadcasting rules with shape-mismatch examples |
| 34 | Vectorization | Benchmark vectorized vs. loop-based ops |
| 35 | Linear algebra ops | Matrix multiplication, transpose, inverse |
| 36 | Applied build | Image normalization pipeline |
| 37 | Applied build | Memory benchmarks + coin-flip Monte Carlo simulation |

### Week 6 — Pandas (Days 38–44)

*v2.0 only gave the pipeline shape (CSV → Cleaning → Feature Engineering → NumPy) for the whole week — broken into daily steps.*

| Day | Focus | Build |
|---|---|---|
| 38 | Loading & inspecting data | Load CSV, `.info()`, `.describe()`, dtypes |
| 39 | Cleaning | Handle nulls, duplicates, type coercion |
| 40 | Indexing & filtering | `.loc`/`.iloc`, boolean masks, groupby |
| 41 | Feature engineering | Derived columns, binning, encoding categoricals |
| 42 | Pandas → NumPy bridge | Convert cleaned DataFrame to NumPy arrays |
| 43 | Assemble the pipeline | One script: CSV → Cleaning → Feature Engineering → NumPy output |
| 44 | Test & document | Run on a second dataset, document edge cases |

### Week 7 — Machine Learning (Days 45–53)

*Corrected range — v2.0 labeled "Days 45–51" but listed Days 52–53 under it too.*

| Day | Topic | Build |
|---|---|---|
| 45 | Train/test split | Manual split function vs. sklearn |
| 46 | Linear Regression | From scratch |
| 47 | Gradient Descent | Visualize loss curve / convergence |
| 48 | Logistic Regression | From scratch |
| 49 | Metrics | Accuracy, Precision, Recall, F1 — implemented manually |
| 50 | PyTorch foundations | Tensors, Dataset, DataLoader |
| 51 | Neural networks | 2-layer MLP, raw Python, manual forward pass |
| 52 | Backpropagation | Manual gradient derivation for the Day 51 MLP |
| 53 | PyTorch MLP | Rebuild Day 51's MLP in PyTorch, compare results |

### Week 8 — Embeddings + Transformers (Days 54–60)

| Day | Topic | Build |
|---|---|---|
| 54 | Vector spaces | Cosine similarity from scratch |
| 55 | Embeddings | Train a tiny embedding on a toy corpus |
| 56 | PCA | Visualize the Day 55 embeddings in 2D |
| 57 | Attention | Toy self-attention implementation |
| 58 | Transformer architecture | Study MHA, FFN, residuals, LayerNorm |
| 59 | Mini transformer | Forward pass only (no training) |
| 60 | Phase 2 review | What I Learned / Mistakes / Next Phase Goals |

---

## PHASE 3 — AGI Systems (Days 61–90)

**Exit criteria:** Working Memory-Augmented Agent with persistence, vector retrieval, logging/audit trail, and one custom data structure (from Phase 1) integrated into the pipeline.

### Week 9 — Agent Memory (Days 61–67)

*v2.0 gave a 4-stage pipeline (Memory Store → Persistence → Retrieval → Logging) for the whole week — expanded into 7 days.*

| Day | Focus | Build |
|---|---|---|
| 61 | Memory store design | Schema: what fields does a "memory" need? |
| 62 | In-memory store | add/get/delete memory entries |
| 63 | Persistence — SQLite | Save/load memory store to SQLite |
| 64 | Persistence — JSON | Alternate JSON persistence, compare tradeoffs |
| 65 | Retrieval | Embedding-based similarity search over stored memories |
| 66 | Logging | Every memory write/read gets logged |
| 67 | Integration test | write → persist → retrieve → log, end-to-end |

### Week 10 — Observability (Days 68–70)

*v2.0 didn't give day numbers here — these are the 3 days left between Week 9 ending and Week 11's explicit Day 71 start.*

| Day | Focus | Build |
|---|---|---|
| 68 | Tracing | Wrap agent calls with trace IDs / spans |
| 69 | Logging + metrics | Structured logs + counters (calls, latency, errors) |
| 70 | Audit trail | Append-only log of every agent decision |

### Week 11 — Reasoning Foundations (Days 71–74)

| Day | Topic | Build |
|---|---|---|
| 71 | Probability | Distributions, expectation, variance |
| 72 | Bayes' Theorem | Simple Bayesian updater |
| 73 | Causal graphs | Build a small causal DAG, reason about interventions |
| 74 | Decision systems | Apply 71–73 to a decision module in your agent |

### Weeks 12–13 — Capstone: Memory-Augmented AI Agent (Days 75–90)

*v2.0 listed the capstone's components as a flat list — sequenced into a 16-day build.*

| Day | Focus |
|---|---|
| 75 | Define scope: what tasks will the agent do, what must it remember? |
| 76 | Short-term memory module |
| 77 | Long-term memory module |
| 78 | Embedding pipeline for memories |
| 79 | Vector similarity search (retrieval) |
| 80 | SQLite persistence layer |
| 81 | Logging integration |
| 82 | Audit trail integration |
| 83 | Plug in your own custom data structure (Linked List or Hash Table) into the pipeline |
| 84 | Wire all modules together |
| 85 | End-to-end test #1: simple conversation/task loop |
| 86 | Fix bugs from Day 85, add error handling |
| 87 | End-to-end test #2: stress test with larger memory volume |
| 88 | Write documentation (README, architecture diagram) |
| 89 | Polish: clean code, comments, final commit |
| 90 | Final review: What I Learned across all 90 days, what's next |

---

## Master Progress Tracker

| Phase | Days | Status |
|---|---|---|
| Phase 1 — Python + DSA | 1–30 | ☐ |
| Phase 2 — NumPy/Pandas/ML | 31–60 | ☐ |
| Phase 3 — AGI Systems | 61–90 | ☐ |

---

## Changes Made From v2.0

- **Week 7 date range fixed:** 45–53 (9 days), not 45–51 — Days 52–53 were listed but excluded from the header range.
- **Daily breakdowns added** where v2.0 only gave week-level or pipeline-level descriptions: Week 6 (Pandas), Week 9 (Agent Memory), Week 10 (Observability), Capstone (Days 75–90).
- **Week 10 day range inferred** as 68–70 (3 days) — the only days available between Week 9 ending Day 67 and Week 11's explicit Day 71 start.
- **Setup checklist, repo annotations, daily workflow, exit criteria, master tracker** added for usability.
