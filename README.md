**90-Day AGI Foundations Roadmap — v2.1 (Restructured)**


What changed from v2.0: Fixed Week 7's day range (45–53, not 45–51 — Days 52–53 were listed under it but excluded from the header). Added explicit daily breakdowns for sections v2.0 only described at the week/pipeline level (Week 6 Pandas, Week 9 Agent Memory, Week 10 Observability, Capstone). Added setup commands, exit criteria per phase, and a master tracker.



1. Daily System

BlockDurationPurpose1 — Concept Learning20 minRead/watch the day's topic. No coding yet.2 — Build / Coding40–60 minImplement the concept + solve the assigned problem.3 — Git Commit + Notes5–10 minCommit your work, write 2–3 lines of notes.

Total: 65–90 min/day

Commit message format:

Day XX: Topic Name

Example: Day 14: Implemented Linked List and Reverse Linked List

Rule: If you miss a day, don't renumber — resume at the next calendar day with the Day XX label you missed. Catching up matters more than streak length.

2. Setup Checklist

ToolPurposeInstallPython 3.11+Core languagesudo apt install python3VS CodeEditorapt/snap or .debGitVersion controlsudo apt install gitGitHub accountRemote repo + portfolio proof—NumPyArrays/linear algebrapip install numpyPandasData wranglingpip install pandasMatplotlibPlottingpip install matplotlibScikit-learnClassical MLpip install scikit-learnPyTorchDeep learningpip install torchJupyterNotebookspip install jupyter

3. Repository Structure

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
└── ROADMAP.md           # this file

4. Daily Workflow


Open notes/dayXX.md, write today's date + topic.
Block 1: read/watch the concept material.
Block 2: write code in the matching week folder.
Run/test the code.
git add . && git commit -m "Day XX: Topic Name"
git push
Add 2–3 lines to notes/dayXX.md: what you learned, what was hard.



PHASE 1 — Python + DSA (Days 1–30)

Exit criteria: All 30 days committed individually (not batched), every LeetCode problem solved and pushed, Day 30 review written.

Week 1 — Python Core (Days 1–7)

Goal: Understand how Python actually works under the hood, not just syntax.

DayConcept LearningBuild TaskLeetCode1is vs ==, object identity, mutabilityCustom class with manual __eq__ comparisons#1 Two Sum2Function scope, closures, LEGB ruleClosure-based counter function#9 Palindrome Number3*args, **kwargs, mutable default trapFunction demonstrating the mutable-default bug + fix#66 Plus One4Decorators@timer, @debug#344 Reverse String5Generators, yield, lazy evaluationInfinite sequence generator#26 Remove Duplicates6OOP dunder methodsClass with __repr__, __str__, __eq__, __len__#242 Valid Anagram7Git basicsinit/add/commit/push/branch — push this week's code#387 First Unique Character

Week 2 — Data Structures (Days 8–14)

DayConcept LearningBuild TaskLeetCode8Context managersCustom with MyTimer():#20 Valid Parentheses9ExceptionsCustom exception hierarchy#189 Rotate Array10Linked listsNode + LinkedList class from scratch#206 Reverse Linked List11StacksStack from scratch#225 Implement Stack Using Queues12Queues + DequeQueue from scratch#232 Implement Queue Using Stacks13Hash tables — collisions, chainingHash table from scratch with chaining#49 Group Anagrams14Complexity analysis (O(1)→O(n²))Go back and annotate Big-O on every function from Days 1–13—

Week 3 — Algorithms (Days 15–21)

DayConcept LearningBuild TaskLeetCode15RecursionRecursive Fibonacci + memoized version#509 Fibonacci16Basic sortingBubble, Selection, Insertion sort—17Advanced sortingMerge Sort, Quick Sort#215 Kth Largest Element18Binary searchIterative + recursive#704 Binary Search19Two pointers—#11 Container With Most Water20Sliding window—#3 Longest Substring Without Repeating Characters21Review daySolve 2 Easy + 1 Medium, closed notes, timed—

Week 4 — Trees, Graphs, DP (Days 22–30)

DayConcept LearningBuild TaskLeetCode22Binary treesInorder/preorder/postorder traversal#102 Binary Tree Level Order Traversal23Binary Search TreesInsert, delete, search#98 Validate BST24GraphsBFS + DFS#200 Number of Islands25Greedy algorithms—#55 Jump Game26Dynamic Programming I—#70 Climbing Stairs27Dynamic Programming II—#62 Unique Paths28Iterator protocolMini dataset class: __getitem__, __len__, custom iterator—29Mock test3 problems, closed notes—30Phase 1 reviewWrite: What I Learned / Mistakes / Next Phase Goals—


PHASE 2 — NumPy + Pandas + ML (Days 31–60)

Exit criteria: Working from-scratch Linear + Logistic Regression, a 2-layer MLP in both raw Python and PyTorch, a toy self-attention implementation, Day 60 review written.

Week 5 — NumPy (Days 31–37)

v2.0 listed this week's topics/builds in bulk — mapped 1:1 to days here.

DayConceptBuild31Arrays & dtypeArray creation, dtype casting tests32Strides & viewsVisualize how slicing creates views vs. copies33BroadcastingBroadcasting rules with shape-mismatch examples34VectorizationBenchmark vectorized vs. loop-based ops35Linear algebra opsMatrix multiplication, transpose, inverse36Applied buildImage normalization pipeline37Applied buildMemory benchmarks + coin-flip Monte Carlo simulation

Week 6 — Pandas (Days 38–44)

v2.0 only gave the pipeline shape (CSV → Cleaning → Feature Engineering → NumPy) for the whole week — broken into daily steps.

DayFocusBuild38Loading & inspecting dataLoad CSV, .info(), .describe(), dtypes39CleaningHandle nulls, duplicates, type coercion40Indexing & filtering.loc/.iloc, boolean masks, groupby41Feature engineeringDerived columns, binning, encoding categoricals42Pandas → NumPy bridgeConvert cleaned DataFrame to NumPy arrays43Assemble the pipelineOne script: CSV → Cleaning → Feature Engineering → NumPy output44Test & documentRun on a second dataset, document edge cases

Week 7 — Machine Learning (Days 45–53)

Corrected range — v2.0 labeled "Days 45–51" but listed Days 52–53 under it too.

DayTopicBuild45Train/test splitManual split function vs. sklearn46Linear RegressionFrom scratch47Gradient DescentVisualize loss curve / convergence48Logistic RegressionFrom scratch49MetricsAccuracy, Precision, Recall, F1 — implemented manually50PyTorch foundationsTensors, Dataset, DataLoader51Neural networks2-layer MLP, raw Python, manual forward pass52BackpropagationManual gradient derivation for the Day 51 MLP53PyTorch MLPRebuild Day 51's MLP in PyTorch, compare results

Week 8 — Embeddings + Transformers (Days 54–60)

DayTopicBuild54Vector spacesCosine similarity from scratch55EmbeddingsTrain a tiny embedding on a toy corpus56PCAVisualize the Day 55 embeddings in 2D57AttentionToy self-attention implementation58Transformer architectureStudy MHA, FFN, residuals, LayerNorm59Mini transformerForward pass only (no training)60Phase 2 reviewWhat I Learned / Mistakes / Next Phase Goals


PHASE 3 — AGI Systems (Days 61–90)

Exit criteria: Working Memory-Augmented Agent with persistence, vector retrieval, logging/audit trail, and one custom data structure (from Phase 1) integrated into the pipeline.

Week 9 — Agent Memory (Days 61–67)

v2.0 gave a 4-stage pipeline (Memory Store → Persistence → Retrieval → Logging) for the whole week — expanded into 7 days.

DayFocusBuild61Memory store designSchema: what fields does a "memory" need?62In-memory storeadd/get/delete memory entries63Persistence — SQLiteSave/load memory store to SQLite64Persistence — JSONAlternate JSON persistence, compare tradeoffs65RetrievalEmbedding-based similarity search over stored memories66LoggingEvery memory write/read gets logged67Integration testwrite → persist → retrieve → log, end-to-end

Week 10 — Observability (Days 68–70)

v2.0 didn't give day numbers here — these are the 3 days left between Week 9 ending and Week 11's explicit Day 71 start.

DayFocusBuild68TracingWrap agent calls with trace IDs / spans69Logging + metricsStructured logs + counters (calls, latency, errors)70Audit trailAppend-only log of every agent decision

Week 11 — Reasoning Foundations (Days 71–74)

DayTopicBuild71ProbabilityDistributions, expectation, variance72Bayes' TheoremSimple Bayesian updater73Causal graphsBuild a small causal DAG, reason about interventions74Decision systemsApply 71–73 to a decision module in your agent

Weeks 12–13 — Capstone: Memory-Augmented AI Agent (Days 75–90)

v2.0 listed the capstone's components as a flat list — sequenced into a 16-day build.

DayFocus75Define scope: what tasks will the agent do, what must it remember?76Short-term memory module77Long-term memory module78Embedding pipeline for memories79Vector similarity search (retrieval)80SQLite persistence layer81Logging integration82Audit trail integration83Plug in your own custom data structure (Linked List or Hash Table) into the pipeline84Wire all modules together85End-to-end test #1: simple conversation/task loop86Fix bugs from Day 85, add error handling87End-to-end test #2: stress test with larger memory volume88Write documentation (README, architecture diagram)89Polish: clean code, comments, final commit90Final review: What I Learned across all 90 days, what's next


Master Progress Tracker

PhaseDaysStatusPhase 1 — Python + DSA1–30☐Phase 2 — NumPy/Pandas/ML31–60☐Phase 3 — AGI Systems61–90☐


Changes Made From v2.0


Week 7 date range fixed: 45–53 (9 days), not 45–51 — Days 52–53 were listed but excluded from the header range.
Daily breakdowns added where v2.0 only gave week-level or pipeline-level descriptions: Week 6 (Pandas), Week 9 (Agent Memory), Week 10 (Observability), Capstone (Days 75–90).
Week 10 day range inferred as 68–70 (3 days) — the only days available between Week 9 ending Day 67 and Week 11's explicit Day 71 start.
Setup checklist, repo annotations, daily workflow, exit criteria, master tracker added for usability.
