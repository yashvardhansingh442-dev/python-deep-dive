90-Day Roadmap: Python + DSA + AGI/ML

Single track, single focus. No Blender, no Internshala — this is the whole sprint now.

Daily budget: 60–75 min/day. ~20 min concept, ~40–55 min on the build.
Commit convention: Day X: <topic> — one commit per day, no batching.

Three phases, each a real 30-day unit. Don't start Phase 2 until Phase 1 is
actually done — slide the calendar, not the order.


Repo Structure

your-dsa-repo/                       ← existing repo, keep using it
├── leetcode/                        ← already exists
├── python-fundamentals/             ← Phase 1
│   ├── week1-core/
│   ├── week2-advanced-ds/
│   ├── week3-algorithms/
│   └── week4-trees-graphs-dp/
├── numpy-pandas-ml/                 ← Phase 2 (NEW)
│   ├── week5-numpy/
│   ├── week6-pandas/
│   ├── week7-ml-fundamentals/
│   └── week8-embeddings-attention/
├── agi-ml-systems/                  ← Phase 3 (NEW)
│   ├── week10-agent-memory/
│   ├── week11-memory-build-math/
│   ├── week12-capstone/
│   └── week13-wrapup/
├── ROADMAP.md                       ← this file, repo root
└── README.md                        ← progress checklist (bottom of this file)


Phase 1 — Day 1–30: Python Core Mechanics + DSA

(Concept fused into that day's LeetCode problem — the problem is the build.)

Week 1 (Day 1–7): Core mechanics

DayConceptPaired LeetCode1Data model — is vs ==, __eq__#1 Two Sum2Scope & closures#9 Palindrome Number3*args/**kwargs, mutable default trap#66 Plus One4Decorators — @timer from scratch#344 Reverse String5Generators & lazy eval#26 Remove Duplicates6OOP I — dunders (__repr__, __eq__, __len__)#242 Valid Anagram7OOP II — inheritance, ABCs#387 First Unique Char

Week 2 (Day 8–14): Advanced features + data structures from scratch

DayConceptPaired LeetCode8Context managers#20 Valid Parentheses9Custom exception hierarchies#189 Rotate Array10Linked Lists, implemented from scratch#206 Reverse Linked List11Stacks & Queues, from scratch#225 Implement Stack using Queues12Hash Maps, with collision handling#49 Group Anagrams13Concurrency basics — the GIL#146 LRU Cache (design, attempt)14Big-O review — no new problemAnnotate complexity for Days 1–13

Week 3 (Day 15–21): Algorithms

DayConceptPaired LeetCode15Recursion, call stack#509 Fibonacci Number16Sorting I — bubble, selection, insertion#912 Sort an Array (your own sort)17Sorting II — merge sort, quicksort#215 Kth Largest Element18Binary search, incl. rotated variants#704, #3319Two pointers#11 Container With Most Water20Sliding window#3 Longest Substring Without Repeating21NumPy intro — ndarray internalsNo problem — transition into Phase 2

Week 4 (Day 22–30): Trees, graphs, DP

DayConceptPaired LeetCode22Binary trees — traversals#102 Level Order Traversal23BST — insert, search, validate#98 Validate BST24Graphs — BFS, DFS#200 Number of Islands25Greedy#55 Jump Game26DP — 1D#70 Climbing Stairs27DP — 2D#62 Unique Paths28Dataset class — __getitem__/__len__ + generator batch iteratorNo new problem29Mock practice — timed, 3 problems, no notesPick 3 from Days 1–2830Phase 1 wrap-up — README + "what I learned" notes—


Phase 2 — Day 31–60: NumPy, Pandas, ML Fundamentals

Week 5 (Day 31–37): NumPy

DayTopicBuild31ndarray internals — dtype, stridesInspect .strides/.flags on reshaped/transposed arrays32Indexing & slicing — views vs copiesProve a slice is a view; a fancy index isn't33BroadcastingBenchmark vectorized vs loop sum of 1M elements34Linear algebra — dot, matmul, inv, eigRedo one exercise from your Linear Algebra Playground directly in NumPy35Aggregation & reshapingNormalize an image batch (NHWC) along the right axis36Random & statisticsSimulate 10,000 coin flips, plot convergence to 0.537PerformanceProfile float64 vs float32 memory at 10M elements

Week 6 (Day 38–44): Pandas for ML pipelines

DayTopicBuild38Series & DataFrame basicsLoad a CSV, fix wrongly-inferred dtypes39Data cleaningClean a messy CSV (inject nulls/dupes first)40GroupBy & aggregationGroup a dataset, compute multiple aggregates41Merge/join/concatJoin two related datasets, validate row counts42.apply() vs vectorizedBenchmark both on the same transform43Custom Dataset class for MLExtend Day 28's class to wrap a real DataFrame44IntegrationMini pipeline: CSV → clean → NumPy batches via your Dataset

Week 7 (Day 45–51): ML fundamentals, from scratch first

DayTopicBuild45Supervised learning — train/test splitSplit + evaluate a toy dataset46Linear regressionImplement from scratch with NumPy47Gradient descentBatch gradient descent on synthetic data, plot convergence48Logistic regressionImplement from scratch, no sklearn49Evaluation metricsAccuracy, precision/recall, confusion matrix — from scratch50scikit-learn or PyTorch intro (pick one)Reimplement Days 46–48 with the library, compare51Neural network basics2-layer feedforward net from scratch in NumPy

Week 8 (Day 52–58): Embeddings, attention — the bridge to AGI/ML

DayTopicBuild52Vector spaces, cosine similarityCompute similarity between toy vectors53EmbeddingsTrain a tiny embedding on a small text corpus, visualize in 2D54Dimensionality reduction (PCA)Apply PCA to Day 53's embeddings, plot55Attention mechanism intuitionToy attention over a 5-token sequence56Transformer structure overviewDiagram + minimal forward pass of one attention block57Mock reviewTimed mixed NumPy/Pandas/ML exercise58Catch-upFinish anything carried over from Days 31–57

Week 9 partial (Day 59–60)

DayTopic59Repo + notebook cleanup60Phase 2 wrap-up — "what I learned" notes


Phase 3 — Day 61–90: AGI/ML Systems

Week 10 (Day 61–67): Agent memory fundamentals

DayTopicBuild61What agent memory is — short vs long-term, context windowsIn-memory key-value state store for a toy agent62Decision logs / audit trailsStructured logging wrapper around agent actions63Vector retrieval basicsEmbedding store + nearest-neighbor search over a small corpus64Observability for agentsAdd basic tracing to Days 61–63's mini-agent65Durable memory patternsAdd persistence (file or SQLite) to Day 61's store66Bridge to your existing Agent Memory Layer roadmapUse Days 61–65 as the foundation, start the formal build67Continue Agent Memory Layer build—

Week 11 (Day 68–74): Continue the build + math gaps, applied

DayTopicBuild68Continue Agent Memory Layer build—69Continue Agent Memory Layer build—70Causal inference, applied introToy causal graph + a simple do-calculus example71Formal logic, applied introSmall propositional-logic statement evaluator72Category theory, applied intro (functors, composition)Implement a simple Functor/Monad-style pattern in Python73Apply one of Days 70–72 to strengthen the decision-audit logic—74Continue Agent Memory Layer build—

Week 12 (Day 75–81): Capstone

Combine Phase 1 (custom data structures) + Phase 2 (NumPy/ML/embeddings) +
Phase 3 (agent memory): an agent that retrieves from a vector store, logs
every decision with an audit trail, and uses at least one Phase-1-built
data structure somewhere in its own pipeline.

DayStage75Scope + design doc76–79Build80Test81Polish

Week 13 (Day 82–90): Mock practice + wrap-up

DayTopic82–84Timed mixed DSA practice, 3 problems/day from earlier days85–86Polish capstone repo — README, architecture diagram, demo script87Write "what I learned" notes covering all 3 phases88Buffer / catch-up89–90Final wrap-up — full 90-day README progress table, retrospective


README.md Checklist Block

markdown## 90-Day Python + DSA + AGI/ML Progress
- [ ] Phase 1: Python Core + DSA (Day 1-30)
- [ ] Phase 2: NumPy / Pandas / ML Fundamentals (Day 31-60)
- [ ] Phase 3: AGI/ML Systems — Agent Memory + Capstone (Day 61-90)
