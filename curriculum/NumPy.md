# NumPy: The Complete Guide (Start to End)

> A full, structured reference and tutorial for NumPy 1.2x / 2.x. Every section has runnable code. Read top to bottom once, then use it as a reference.

---

## Table of Contents

0. [Learning Roadmap (8 Phases)](#learning-roadmap-8-phases)
1. [What is NumPy and Why Use It](#1-what-is-numpy-and-why-use-it)
2. [Installation and Setup](#2-installation-and-setup)
3. [The ndarray: Core Concepts](#3-the-ndarray-core-concepts)
4. [Creating Arrays](#4-creating-arrays)
5. [Data Types (dtype)](#5-data-types-dtype)
6. [Array Attributes](#6-array-attributes)
7. [Indexing and Slicing](#7-indexing-and-slicing)
8. [Boolean Indexing and Fancy Indexing](#8-boolean-indexing-and-fancy-indexing)
9. [Views vs Copies](#9-views-vs-copies)
10. [Reshaping and Manipulating Shape](#10-reshaping-and-manipulating-shape)
11. [Joining, Splitting, Tiling](#11-joining-splitting-tiling)
12. [Arithmetic and Universal Functions (ufuncs)](#12-arithmetic-and-universal-functions-ufuncs)
13. [Broadcasting](#13-broadcasting)
14. [Aggregations and Statistics](#14-aggregations-and-statistics)
15. [Sorting, Searching, Set Operations](#15-sorting-searching-set-operations)
16. [Conditional Logic: where, select, piecewise](#16-conditional-logic-where-select-piecewise)
17. [Linear Algebra (np.linalg)](#17-linear-algebra-nplinalg)
18. [Random Numbers](#18-random-numbers)
19. [Working with Missing Data (NaN, inf, masked arrays)](#19-working-with-missing-data-nan-inf-masked-arrays)
20. [Structured and Record Arrays](#20-structured-and-record-arrays)
21. [File Input/Output](#21-file-inputoutput)
22. [einsum, tensordot, and Advanced Products](#22-einsum-tensordot-and-advanced-products)
23. [Polynomials, FFT, Interpolation, Integration](#23-polynomials-fft-interpolation-integration)
24. [Memory Layout, Strides, Performance](#24-memory-layout-strides-performance)
25. [Vectorization Patterns](#25-vectorization-patterns)
26. [NumPy for Machine Learning (Worked Examples)](#26-numpy-for-machine-learning-worked-examples)
27. [Common Pitfalls and Gotchas](#27-common-pitfalls-and-gotchas)
28. [NumPy 2.x Changes](#28-numpy-2x-changes)
29. [Practice Problems with Solutions](#29-practice-problems-with-solutions)
30. [Phase 1 Deep Dive: Foundations](#30-phase-1-deep-dive-foundations)
31. [Phase 2 Deep Dive: Creating and Inspecting Arrays](#31-phase-2-deep-dive-creating-and-inspecting-arrays)
32. [Phase 3 Deep Dive: Indexing and Manipulation](#32-phase-3-deep-dive-indexing-and-manipulation)
33. [Phase 4 Deep Dive: Operations and Broadcasting](#33-phase-4-deep-dive-operations-and-broadcasting)
34. [Phase 5 Deep Dive: Array Processing](#34-phase-5-deep-dive-array-processing)
35. [Phase 6 Deep Dive: Random Numbers and Linear Algebra](#35-phase-6-deep-dive-random-numbers-and-linear-algebra)
36. [Phase 7 Deep Dive: Advanced NumPy](#36-phase-7-deep-dive-advanced-numpy)
37. [Phase 8 Deep Dive: Data Science and ML Applications](#37-phase-8-deep-dive-data-science-and-ml-applications)
38. [String and Character Arrays](#38-string-and-character-arrays)
39. [Cheat Sheet](#39-cheat-sheet)
40. [Appendix A: Review of My Practice Scripts](#appendix-a-review-of-my-practice-scripts-numpy-folder)

---

## Learning Roadmap (8 Phases)

Follow the phases in order. Each phase lists where the topic lives in this guide. Sections 1 to 29 are the main tutorial; sections 30 to 37 are **deep dives** that fill the remaining gaps for each phase.

| Phase | Focus | Main result | Main sections | Deep dive |
|---|---|---|---|---|
| 1 | Foundations | Understand arrays and NumPy | 1, 2, 3 | 30 |
| 2 | Creating and inspecting arrays | Build arrays and read their properties | 4, 5, 6 | 31, 38 (strings) |
| 3 | Indexing and manipulation | Select, update, and reshape data | 7, 8, 9, 10 | 32 |
| 4 | Operations and broadcasting | Compute efficiently without manual loops | 12, 13, 14 | 33 |
| 5 | Array processing | Combine, split, sort, search, and filter | 11, 15, 16 | 34 |
| 6 | Random numbers and linear algebra | Generate data and work with matrices | 17, 18 | 35 |
| 7 | Advanced NumPy | Memory, missing data, files, and performance | 19, 20, 21, 22, 23, 24, 25 | 36 |
| 8 | Data science and ML applications | Build numerical workflows and ML foundations | 26 (+ 29 practice) | 37 |

Cross-cutting sections: 27 (pitfalls), 28 (NumPy 2.x changes), 29 (practice problems), 39 (cheat sheet), Appendix A (review of my practice scripts and the next scripts to write).

**How to use each phase:** read the main sections, run every code block, read the deep dive, then answer the **Checkpoint** questions at the end of the deep dive without looking at the answers.

---

## 1. What is NumPy and Why Use It

**NumPy** (Numerical Python) is the foundation of scientific computing in Python. It provides:

- `ndarray`: a fast, fixed-type, N-dimensional array.
- Vectorized operations (no Python loops needed).
- Broadcasting rules for operating on arrays of different shapes.
- Linear algebra, random numbers, FFT, and more.
- The base layer for Pandas, SciPy, scikit-learn, Matplotlib, TensorFlow, PyTorch (tensors mimic the NumPy API), OpenCV, and nearly every data/ML library.

### Why is it fast?

| Reason | Explanation |
|---|---|
| Contiguous memory | Elements are stored in one block, cache-friendly |
| Fixed dtype | No per-element type checking like Python lists |
| C implementation | Loops run in compiled C/Fortran, often SIMD-optimized |
| BLAS/LAPACK | Matrix operations use optimized libraries |

### Python list vs NumPy array

```python
import numpy as np
import time

n = 1_000_000
py_list = list(range(n))
np_arr = np.arange(n)

t = time.perf_counter()
result = [x * 2 for x in py_list]
print("List :", time.perf_counter() - t)

t = time.perf_counter()
result = np_arr * 2
print("NumPy:", time.perf_counter() - t)
# NumPy is typically 20x-100x faster
```

---

## 2. Installation and Setup

```bash
pip install numpy
# or
conda install numpy
```

```python
import numpy as np          # universal convention
print(np.__version__)
np.show_config()            # shows BLAS/LAPACK backend
```

Useful display settings:

```python
np.set_printoptions(precision=3, suppress=True, linewidth=120, threshold=100)
# precision: decimals, suppress: no scientific notation for small numbers
# threshold: arrays longer than this are summarized with ...
```

Getting help:

```python
np.info(np.sum)
help(np.linspace)
np.lookfor("moving average")   # search docs by keyword
```

---

## 3. The ndarray: Core Concepts

An `ndarray` is a **homogeneous** (all same dtype), **N-dimensional** grid indexed by non-negative integers.

- **Axis**: a dimension. A 2D array has axis 0 (rows, going down) and axis 1 (columns, going across).
- **Shape**: tuple of sizes along each axis.
- **Rank / ndim**: number of axes.

```python
a = np.array([1, 2, 3])                  # 1D, shape (3,)
b = np.array([[1, 2, 3], [4, 5, 6]])     # 2D, shape (2, 3)
c = np.zeros((2, 3, 4))                  # 3D, shape (2, 3, 4)
```

Mental model for 3D: `(depth/batch, rows, columns)`. For images: `(height, width, channels)`. For ML batches: `(batch, features)` or `(batch, time, features)`.

---

## 4. Creating Arrays

### 4.1 From Python sequences

```python
np.array([1, 2, 3])
np.array([[1, 2], [3, 4]])
np.array([1, 2, 3], dtype=np.float32)
np.array([1, 2.5, 3])           # upcasts to float64
np.asarray(my_list)             # no copy if already an ndarray
np.array(my_array, copy=True)   # explicit copy
```

### 4.2 Built-in constructors

```python
np.zeros((3, 4))                # all 0.0
np.ones((2, 2), dtype=int)      # all 1
np.full((2, 3), 7)              # filled with 7
np.empty((2, 2))                # uninitialized (garbage values, fast)
np.eye(3)                       # identity matrix
np.identity(3)                  # same as eye(3)
np.eye(3, 4, k=1)               # ones on k-th diagonal
np.diag([1, 2, 3])              # diagonal matrix from vector
np.diag(matrix)                 # extract diagonal from matrix
np.tri(3)                       # lower triangular ones
np.tril(matrix)                 # lower triangle of matrix
np.triu(matrix)                 # upper triangle of matrix
```

### 4.3 `_like` variants (copy shape and dtype of another array)

```python
np.zeros_like(a)
np.ones_like(a)
np.full_like(a, 9)
np.empty_like(a)
```

### 4.4 Ranges

```python
np.arange(10)                   # 0..9
np.arange(2, 10, 3)             # 2, 5, 8  (start, stop, step) stop excluded
np.arange(0, 1, 0.1)            # float steps can be imprecise!

np.linspace(0, 1, 5)            # 5 points, endpoints INCLUDED: 0, .25, .5, .75, 1
np.linspace(0, 1, 5, endpoint=False)
np.logspace(0, 3, 4)            # 10^0 .. 10^3 -> 1, 10, 100, 1000
np.geomspace(1, 1000, 4)        # geometric spacing
```

> Rule of thumb: use `arange` for integers, `linspace` for floats (you control the count, not the step).

### 4.5 Grids

```python
x = np.linspace(-1, 1, 3)
y = np.linspace(-2, 2, 4)
X, Y = np.meshgrid(x, y)                # shape (4, 3) each; indexing='xy' default
X, Y = np.meshgrid(x, y, indexing='ij') # matrix-style indexing, shape (3, 4)

np.mgrid[0:3, 0:3]                      # dense grid, slice notation
np.ogrid[0:3, 0:3]                      # open grid (broadcastable, memory-light)
```

### 4.6 From functions and iterables

```python
np.fromfunction(lambda i, j: i + j, (3, 3), dtype=int)
np.fromiter((x*x for x in range(5)), dtype=int)
np.frombuffer(b'\x01\x02\x03', dtype=np.uint8)
np.fromstring("1 2 3", sep=" ")         # text mode only
```

### 4.7 Random creation (preview, see Section 18)

```python
rng = np.random.default_rng(42)
rng.random((2, 3))
rng.integers(0, 10, size=5)
rng.normal(0, 1, size=(3, 3))
```

---

## 5. Data Types (dtype)

### 5.1 Common dtypes

| Category | dtypes |
|---|---|
| Boolean | `bool_` / `np.bool` (2.x) |
| Signed int | `int8, int16, int32, int64` |
| Unsigned int | `uint8, uint16, uint32, uint64` |
| Float | `float16, float32, float64` (`float128` on some platforms) |
| Complex | `complex64, complex128` |
| String | `str_` (`U10`), `bytes_` (`S10`) |
| Datetime | `datetime64[D]`, `timedelta64[s]` |
| Object | `object` (any Python object, slow) |

Default: Python `int` becomes `int64` (on most platforms), `float` becomes `float64`.

### 5.2 Specifying and converting

```python
a = np.array([1, 2, 3], dtype=np.float32)
b = a.astype(np.int16)             # returns a NEW array
a.dtype                            # dtype('float32')
np.dtype('f4')                     # shorthand: 'f4' = float32, 'i8' = int64, 'u1' = uint8, '?' = bool

np.iinfo(np.int32)                 # min, max of ints
np.finfo(np.float32)               # eps, max, min of floats
```

### 5.3 Overflow

```python
x = np.array([250], dtype=np.uint8)
x + 10          # wraps around silently -> array([4], dtype=uint8)
```

Integer overflow is **silent** in NumPy arrays. Pick dtype carefully (e.g., image math: cast to `float32` before computing).

### 5.4 Type promotion

```python
np.result_type(np.int8, np.float32)   # float32
np.promote_types('i4', 'f4')          # float64
np.can_cast(np.float64, np.int32)     # False
```

Mixing `int64` and `float64` gives `float64`. Operations between arrays follow promotion rules; Python scalars are "weak" in NumPy 2 (NEP 50), so `np.uint8(1) + 300` raises/behaves differently than in 1.x.

### 5.5 Datetimes

```python
d = np.array(['2026-01-01', '2026-03-15'], dtype='datetime64[D]')
d + np.timedelta64(30, 'D')
np.diff(d)                              # timedelta64
np.arange('2026-01', '2026-06', dtype='datetime64[M]')
np.busday_count('2026-01-01', '2026-02-01')   # business days
```

---

## 6. Array Attributes

```python
a = np.arange(24).reshape(2, 3, 4)

a.shape       # (2, 3, 4)
a.ndim        # 3
a.size        # 24 (total elements)
a.dtype       # int64
a.itemsize    # bytes per element (8)
a.nbytes      # total bytes = size * itemsize
a.strides     # bytes to step along each axis
a.T           # transpose
a.flat        # 1D iterator over elements
a.real, a.imag
a.base        # the array it is a view of (None if owns data)
a.flags       # C_CONTIGUOUS, F_CONTIGUOUS, OWNDATA, WRITEABLE, ...
```

---

## 7. Indexing and Slicing

### 7.1 1D

```python
a = np.array([10, 20, 30, 40, 50])
a[0]        # 10
a[-1]       # 50
a[1:4]      # [20 30 40]
a[:3]       # [10 20 30]
a[::2]      # [10 30 50]
a[::-1]     # reversed
```

### 7.2 2D and nD

```python
m = np.arange(12).reshape(3, 4)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

m[1, 2]         # 6          (preferred over m[1][2])
m[0]            # first row
m[:, 1]         # second column
m[1:, :2]       # rows 1.., cols 0..1
m[::2, ::2]     # every other row and column
m[..., 0]       # Ellipsis: all leading axes, last index 0
m[:, None, :]   # np.newaxis: insert new axis -> shape (3, 1, 4)
```

### 7.3 Assignment

```python
m[0, :] = 99
m[:, 1] = [1, 2, 3]
m[1:, 2:] = 0
m[m > 50] = -1
```

### 7.4 Index helpers

```python
np.s_[1:3, ::2]            # build slice objects
np.ix_([0, 2], [1, 3])     # open mesh for fancy-indexing submatrix
m[np.ix_([0, 2], [1, 3])]  # rows 0,2 and cols 1,3
np.take(a, [0, 2])
np.put(a, [0, 2], [-1, -2])
np.diag_indices(3)
np.tril_indices(3)
np.unravel_index(7, (3, 4))   # flat index -> (row, col)
np.ravel_multi_index((1, 3), (3, 4))
```

---

## 8. Boolean Indexing and Fancy Indexing

### 8.1 Boolean masks

```python
a = np.array([5, 12, 7, 20, 3])
mask = a > 6                 # [False True True True False]
a[mask]                      # [12 7 20]
a[(a > 6) & (a < 15)]        # use & | ~ with parentheses (NOT and/or/not)
a[~(a > 6)]
a[a % 2 == 0] = 0            # conditional assignment
```

Useful companions:

```python
np.any(a > 10)
np.all(a > 0)
np.count_nonzero(a > 6)
(a > 6).sum()
np.nonzero(a > 6)            # indices where True
np.flatnonzero(a > 6)
np.argwhere(a > 6)           # (n, ndim) array of coordinates
```

### 8.2 Fancy (integer-array) indexing

```python
a = np.array([10, 20, 30, 40, 50])
a[[0, 2, 4]]                 # [10 30 50]
a[[4, 0, 0]]                 # repeats allowed

m = np.arange(12).reshape(3, 4)
m[[0, 2], [1, 3]]            # elements (0,1) and (2,3) -> paired!
m[[0, 2]]                    # rows 0 and 2
m[:, [0, 3]]                 # columns 0 and 3
```

Fancy indexing with several index arrays **pairs them** (zip-like); use `np.ix_` for the cross product.

### 8.3 Fancy indexing always returns a copy

```python
b = a[[0, 1]]
b[0] = 999       # does NOT modify a
```

(But assignment `a[[0, 1]] = ...` does modify `a`.)

### 8.4 Repeated indices in assignment

```python
a = np.zeros(3)
a[[0, 0, 1]] += 1      # a = [1, 1, 0]   (increments NOT accumulated)
np.add.at(a, [0, 0, 1], 1)   # a += [2, 1, 0], unbuffered, accumulates
```

---

## 9. Views vs Copies

| Operation | Result |
|---|---|
| Basic slicing `a[1:3]` | **View** (shares memory) |
| `reshape`, `ravel` (when possible), `T`, `transpose` | Usually view |
| `a.view()` | View |
| Boolean / fancy indexing | **Copy** |
| `a.copy()`, `flatten()`, `astype()` | Copy |

```python
a = np.arange(6)
v = a[1:4]
v[0] = 100
print(a)             # [0 100 2 3 4 5]  -> original changed!

c = a[1:4].copy()    # independent

np.shares_memory(a, v)     # True
np.may_share_memory(a, v)
v.base is a                # True
```

`ravel()` returns a view when possible, `flatten()` always copies.

---

## 10. Reshaping and Manipulating Shape

```python
a = np.arange(12)

a.reshape(3, 4)
a.reshape(3, -1)         # -1: infer dimension
a.reshape(2, 2, 3)
a.reshape(3, 4, order='F')   # Fortran (column-major) order

a.ravel()                # flatten, view if possible
a.flatten()              # flatten, copy
a.resize(3, 4)           # in-place (may pad with zeros)
np.resize(a, (2, 8))     # repeats data to fill

m = a.reshape(3, 4)
m.T                      # transpose
np.transpose(m, (1, 0))
np.swapaxes(m, 0, 1)
np.moveaxis(x, 0, -1)    # move axis 0 to last
np.rollaxis(x, 2)        # legacy, prefer moveaxis

np.expand_dims(a, axis=0)   # shape (1, 12)
a[np.newaxis, :]            # same
a[:, None]                  # column vector (12, 1)
np.squeeze(x)               # remove length-1 axes
np.squeeze(x, axis=0)

np.atleast_1d(5)
np.atleast_2d(a)
np.atleast_3d(a)

np.flip(m, axis=0)       # reverse along axis
np.fliplr(m); np.flipud(m)
np.rot90(m, k=1)
np.roll(a, 3)            # circular shift
np.roll(m, 1, axis=1)
```

---

## 11. Joining, Splitting, Tiling

### 11.1 Joining

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

np.concatenate([a, b], axis=0)    # stack rows -> (4, 2)
np.concatenate([a, b], axis=1)    # side by side -> (2, 4)
np.vstack([a, b])                 # = concatenate axis=0 (for 1D: makes rows)
np.hstack([a, b])                 # = concatenate axis=1
np.dstack([a, b])                 # along 3rd axis -> (2, 2, 2)
np.stack([a, b], axis=0)          # NEW axis -> (2, 2, 2)
np.stack([a, b], axis=-1)         # new last axis
np.column_stack([[1, 2], [3, 4]]) # 1D arrays become columns
np.block([[a, b], [b, a]])        # block matrix
np.append(a, [[9, 9]], axis=0)    # convenience (slow in loops!)
np.insert(arr, 1, 99)
np.delete(arr, [0, 2])
```

> `concatenate` joins along an **existing** axis; `stack` creates a **new** axis.

### 11.2 Splitting

```python
x = np.arange(12).reshape(3, 4)
np.split(x, 3, axis=0)             # 3 equal parts (must divide evenly)
np.array_split(x, 5, axis=1)       # allows uneven
np.hsplit(x, 2)
np.vsplit(x, 3)
np.split(np.arange(10), [3, 7])    # split at indices -> [0:3], [3:7], [7:]
```

### 11.3 Repeating and tiling

```python
np.repeat([1, 2], 3)            # [1 1 1 2 2 2]
np.repeat(m, 2, axis=0)         # repeat each row twice
np.tile([1, 2], 3)              # [1 2 1 2 1 2]
np.tile(m, (2, 2))              # tile in a grid
np.pad(m, pad_width=1, mode='constant', constant_values=0)
np.pad(m, ((1, 0), (0, 2)), mode='edge')   # also 'reflect', 'wrap'
```

---

## 12. Arithmetic and Universal Functions (ufuncs)

### 12.1 Element-wise operators

```python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

a + b; a - b; a * b; a / b      # element-wise
a ** 2; a // 2; a % 2           # power, floor div, modulo
-a
a + 5                            # scalar broadcast
a == b; a != b; a < b            # boolean arrays
```

`*` is **element-wise**, NOT matrix multiplication. Use `@` or `np.matmul` for that.

### 12.2 Math ufuncs

```python
np.sqrt(a); np.cbrt(a); np.square(a); np.power(a, 3)
np.exp(a); np.expm1(a); np.exp2(a)
np.log(a); np.log10(a); np.log2(a); np.log1p(a)
np.sin(a); np.cos(a); np.tan(a)
np.arcsin(x); np.arccos(x); np.arctan(x); np.arctan2(y, x)
np.sinh(a); np.tanh(a)
np.deg2rad(180); np.rad2deg(np.pi); np.radians; np.degrees
np.abs(a); np.sign(a)
np.floor(x); np.ceil(x); np.round(x, 2); np.trunc(x); np.rint(x)
np.clip(a, 0, 10)
np.maximum(a, b); np.minimum(a, b)       # element-wise (not reductions)
np.hypot(3, 4)                           # 5.0
np.mod(a, 3); np.remainder; np.fmod; np.divmod(a, 3)
np.gcd(12, 18); np.lcm(4, 6)
np.reciprocal(a.astype(float))
np.isnan(x); np.isinf(x); np.isfinite(x)
np.isclose(a, b, rtol=1e-5, atol=1e-8)
np.allclose(a, b)
np.array_equal(a, b)
```

### 12.3 Ufunc methods

```python
np.add.reduce([1, 2, 3, 4])           # 10  (same as sum)
np.add.accumulate([1, 2, 3, 4])       # [1 3 6 10]  (cumsum)
np.multiply.reduce([1, 2, 3, 4])      # 24
np.multiply.outer([1, 2, 3], [10, 20])   # outer product table
np.add.outer(a, b)
np.add.at(arr, idx, vals)             # unbuffered in-place
np.maximum.reduce(x, axis=0)
```

### 12.4 `out=` and `where=`

```python
out = np.empty_like(a, dtype=float)
np.sqrt(a, out=out)                   # avoids allocating a new array
a += 1                                # in-place operators save memory
np.divide(a, b, out=np.zeros_like(a, dtype=float), where=(b != 0))
```

### 12.5 Custom ufuncs

```python
def f(x, y):
    return x if x > y else y * 2
vf = np.vectorize(f)    # convenience only; NOT faster (still a Python loop)
vf(a, b)
```

For real speed use vectorized expressions, `np.where`, Numba, or Cython.

---

## 13. Broadcasting

Broadcasting lets NumPy operate on arrays of **different shapes** without copying data.

### 13.1 Rules

Compare shapes **from the trailing (rightmost) dimension** moving left:

1. If dimensions are equal, OK.
2. If one of them is **1**, it is stretched to match the other.
3. Otherwise: error (`ValueError: operands could not be broadcast together`).

Missing leading dimensions are treated as 1.

```
A      (3, 4)
B         (4,)      -> (1, 4) -> (3, 4)     OK
A      (3, 1)
B      (1, 4)       -> (3, 4)               OK (outer-like)
A      (3, 4)
B      (3,)         -> ERROR (4 vs 3)
```

### 13.2 Examples

```python
m = np.arange(12).reshape(3, 4)

m + 10                        # scalar
m + np.array([1, 2, 3, 4])    # add to every row
m + np.array([[1], [2], [3]]) # add to every column (shape (3, 1))

col = np.array([1, 2, 3])
m + col[:, None]              # fix shape error by adding axis

# Outer product via broadcasting
x = np.arange(3)[:, None]
y = np.arange(4)[None, :]
x * y                         # (3, 4) multiplication table

# Pairwise distances between points (n, d) and (m, d)
A = np.random.rand(5, 2)
B = np.random.rand(7, 2)
D = np.sqrt(((A[:, None, :] - B[None, :, :]) ** 2).sum(axis=-1))   # (5, 7)

# Normalize columns (standardize features)
X = np.random.rand(100, 4)
X_std = (X - X.mean(axis=0)) / X.std(axis=0)

np.broadcast_to(np.array([1, 2, 3]), (4, 3))   # read-only view
np.broadcast_arrays(a, b)
np.broadcast_shapes((3, 1), (1, 4))            # (3, 4)
```

---

## 14. Aggregations and Statistics

### 14.1 Reductions

```python
a = np.array([[1, 2, 3], [4, 5, 6]])

a.sum()                 # 21 (all)
a.sum(axis=0)           # [5 7 9]   collapse rows -> per-column
a.sum(axis=1)           # [6 15]    collapse columns -> per-row
a.sum(axis=(0, 1))
a.sum(axis=1, keepdims=True)    # shape (2, 1), handy for broadcasting

a.mean(); a.median      # np.median(a) is a function only
np.median(a, axis=0)
a.min(); a.max(); a.ptp()       # ptp = max - min (np.ptp in 2.x)
a.argmin(); a.argmax()          # index in flattened array
a.argmax(axis=1)                # per row
a.prod()
a.std(); a.var()
a.std(ddof=1)                   # sample std (default ddof=0 is population)
a.cumsum(axis=1); a.cumprod()
np.diff(a, axis=1)              # consecutive differences
np.gradient(y, x)
np.average(a, weights=w, axis=0)
np.percentile(a, [25, 50, 75])
np.quantile(a, 0.9)
np.count_nonzero(a)
np.any(a > 5); np.all(a > 0)
```

### 14.2 Axis intuition

> **`axis=k` means "collapse axis k"**. The result has that axis removed.
> Shape `(2, 3)` with `axis=0` gives `(3,)`. With `axis=1` gives `(2,)`.

### 14.3 NaN-safe versions

```python
np.nansum, np.nanmean, np.nanmedian, np.nanstd, np.nanvar
np.nanmin, np.nanmax, np.nanargmax, np.nanargmin
np.nanpercentile, np.nancumsum
```

### 14.4 Correlation and histograms

```python
np.corrcoef(x, y)            # correlation matrix
np.cov(x, y)                 # covariance matrix (rows = variables)
np.correlate(a, v, 'full')   # 1D cross-correlation
np.convolve(a, [1/3]*3, mode='valid')     # moving average

counts, edges = np.histogram(data, bins=10, range=(0, 1), density=False)
np.histogram2d(x, y, bins=20)
np.histogramdd(sample)
np.digitize(x, bins=[0, 1, 2])            # bin index for each value
np.bincount([0, 1, 1, 3])                 # [1 2 0 1] counts of non-neg ints
np.bincount(idx, weights=w)               # weighted counts (group-by sum)
```

---

## 15. Sorting, Searching, Set Operations

### 15.1 Sorting

```python
a = np.array([3, 1, 2])
np.sort(a)                       # new sorted copy
a.sort()                         # in place
np.sort(m, axis=0)               # sort each column
np.sort(m, axis=None)            # sort flattened
np.argsort(a)                    # indices that sort a -> [1 2 0]
np.argsort(a)[::-1]              # descending order
np.sort(a, kind='stable')        # 'quicksort' (default), 'mergesort', 'heapsort', 'stable'

# sort rows of 2D array by column 1
m[m[:, 1].argsort()]

# multi-key sort (last key is primary)
np.lexsort((secondary, primary))

# partial sort (k smallest without full sort)
np.partition(a, 2)               # element at index 2 is in sorted position
np.argpartition(a, 2)[:3]        # indices of 3 smallest (unordered)
```

### 15.2 Searching

```python
np.searchsorted([1, 3, 5, 7], 4)           # 2 (insertion index in sorted array)
np.searchsorted(arr, vals, side='right')
np.argmax(a); np.argmin(a)
np.nonzero(a); np.where(cond)              # indices
np.extract(cond, a)
```

### 15.3 Set operations

```python
np.unique([3, 1, 2, 1, 3])                          # [1 2 3]
np.unique(a, return_counts=True)
np.unique(a, return_index=True)
np.unique(a, return_inverse=True)
np.unique(m, axis=0)                                # unique rows
np.intersect1d(a, b)
np.union1d(a, b)
np.setdiff1d(a, b)
np.setxor1d(a, b)
np.isin(a, [1, 2])                                  # boolean membership mask
```

---

## 16. Conditional Logic: where, select, piecewise

```python
a = np.array([-2, -1, 0, 1, 2])

np.where(a > 0, a, 0)                       # ReLU: [0 0 0 1 2]
np.where(a > 0, 'pos', 'non-pos')
np.where(a > 0)                             # one-arg: indices

np.select(
    [a < 0, a == 0, a > 0],
    ['neg', 'zero', 'pos'],
    default='?'
)

np.piecewise(a, [a < 0, a >= 0], [lambda x: -x, lambda x: x ** 2])

np.choose([0, 1, 0, 1, 0], [a, a * 10])
np.clip(a, -1, 1)
np.copyto(dst, src, where=mask)
```

---

## 17. Linear Algebra (np.linalg)

### 17.1 Products

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
v = np.array([1, 2])

A @ B                  # matrix multiplication (preferred)
np.matmul(A, B)
np.dot(A, B)           # same for 2D; for ND differs from matmul
A @ v                  # matrix-vector
v @ v                  # dot product (scalar)
np.inner(v, v)
np.outer(v, v)         # outer product
np.cross([1, 0, 0], [0, 1, 0])
np.vdot(a, b)          # conjugates first arg
np.kron(A, B)          # Kronecker product
np.linalg.matrix_power(A, 3)
```

Batched matmul: `np.matmul` broadcasts over leading dims. Shapes `(batch, n, k) @ (batch, k, m)` give `(batch, n, m)`.

### 17.2 Core routines

```python
np.linalg.det(A)
np.linalg.inv(A)                 # avoid when you can solve instead
np.linalg.pinv(A)                # Moore-Penrose pseudo-inverse
np.linalg.matrix_rank(A)
np.linalg.trace(A)               # or np.trace(A)
np.linalg.norm(v)                # L2 norm
np.linalg.norm(v, ord=1)         # L1
np.linalg.norm(v, ord=np.inf)
np.linalg.norm(A, 'fro')         # Frobenius
np.linalg.norm(A, axis=1)        # per-row norms
np.linalg.cond(A)                # condition number
```

### 17.3 Solving systems

```python
# Solve Ax = b  (preferred over inv(A) @ b: faster and more accurate)
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x = np.linalg.solve(A, b)            # [2. 3.]

# Least squares (overdetermined): minimize ||Ax - b||
x, residuals, rank, sv = np.linalg.lstsq(A, b, rcond=None)
```

### 17.4 Decompositions

```python
# Eigenvalues / eigenvectors
vals, vecs = np.linalg.eig(A)            # general; columns of vecs are eigenvectors
vals, vecs = np.linalg.eigh(S)           # symmetric/Hermitian; sorted ascending, real

# SVD: A = U @ diag(s) @ Vt
U, s, Vt = np.linalg.svd(A)
U, s, Vt = np.linalg.svd(A, full_matrices=False)    # economy SVD

# QR
Q, R = np.linalg.qr(A)

# Cholesky (positive-definite): A = L @ L.T
L = np.linalg.cholesky(S)

# Verify eigen decomposition
np.allclose(A @ vecs, vecs * vals)
```

### 17.5 Example: PCA from scratch

```python
X = np.random.rand(200, 5)
Xc = X - X.mean(axis=0)
cov = np.cov(Xc, rowvar=False)
vals, vecs = np.linalg.eigh(cov)
order = np.argsort(vals)[::-1]
vals, vecs = vals[order], vecs[:, order]
X_pca = Xc @ vecs[:, :2]                 # project to 2 components
explained = vals / vals.sum()
```

### 17.6 Misc

```python
np.linalg.slogdet(A)                      # sign and log|det| (stable)
np.linalg.multi_dot([A, B, C])            # optimal association order
np.linalg.tensorsolve; np.linalg.tensorinv
np.linalg.eigvals(A)
```

---

## 18. Random Numbers

### 18.1 Modern API (Generator) - use this

```python
rng = np.random.default_rng(seed=42)       # reproducible

rng.random(5)                              # uniform [0, 1)
rng.random((2, 3))
rng.uniform(low=-1, high=1, size=4)
rng.integers(0, 10, size=5)                # [0, 10) ints
rng.integers(1, 7, size=(2, 2), endpoint=True)   # include 7
rng.normal(loc=0, scale=1, size=(3, 3))
rng.standard_normal(5)
rng.binomial(n=10, p=0.5, size=5)
rng.poisson(lam=3, size=5)
rng.exponential(scale=2, size=5)
rng.gamma(2.0, 1.0, size=5)
rng.beta(2, 5, size=5)
rng.multivariate_normal(mean, cov, size=100)
rng.choice([1, 2, 3, 4], size=3, replace=False)
rng.choice(5, size=10, p=[.1, .2, .3, .2, .2])
rng.permutation(10)                        # shuffled copy
rng.shuffle(arr)                           # in-place
rng.permuted(m, axis=1)                    # shuffle each row independently
```

### 18.2 Legacy API (still works, widely seen)

```python
np.random.seed(0)
np.random.rand(2, 3)
np.random.randn(2, 3)
np.random.randint(0, 10, 5)
np.random.choice(...)
```

### 18.3 Reproducibility tips

```python
# Independent streams for parallel work
ss = np.random.SeedSequence(12345)
child_seeds = ss.spawn(4)
rngs = [np.random.default_rng(s) for s in child_seeds]
```

Pass a `rng` object into functions instead of using global state.

---

## 19. Working with Missing Data (NaN, inf, masked arrays)

```python
a = np.array([1.0, np.nan, 3.0, np.inf])

np.isnan(a)                  # [F T F F]
np.isinf(a)
np.isfinite(a)
np.nan == np.nan             # False! use isnan
np.nan_to_num(a, nan=0, posinf=1e9, neginf=-1e9)

np.nanmean(a[np.isfinite(a)])
a[~np.isnan(a)]              # drop NaNs
```

NaN only exists for floats. Integer arrays cannot hold NaN.

### Masked arrays

```python
import numpy.ma as ma
x = ma.masked_array([1, 2, -999, 4], mask=[0, 0, 1, 0])
x.mean()                                  # ignores masked -> 2.333
ma.masked_equal([1, -999, 3], -999)
ma.masked_where(arr > 100, arr)
ma.masked_invalid(arr)
x.filled(0)                               # replace masked with value
x.compressed()                            # 1D array of unmasked
```

---

## 20. Structured and Record Arrays

```python
dt = np.dtype([('name', 'U10'), ('age', 'i4'), ('score', 'f8')])
data = np.array([('Ann', 25, 88.5), ('Bob', 30, 92.1)], dtype=dt)

data['name']                 # field access
data[0]                      # one record
data[data['age'] > 26]
data.sort(order='score')

rec = data.view(np.recarray)
rec.name                     # attribute access
```

For heavy tabular work, prefer **Pandas** (built on NumPy), but structured arrays are good for fixed binary layouts.

---

## 21. File Input/Output

### 21.1 Native binary formats

```python
np.save('arr.npy', a)                   # single array (fast, preserves dtype/shape)
b = np.load('arr.npy')
np.load('big.npy', mmap_mode='r')       # memory-map, read lazily from disk

np.savez('multi.npz', x=a, y=b)         # several arrays, uncompressed
np.savez_compressed('multi.npz', x=a, y=b)
d = np.load('multi.npz')
d['x']; d.files
```

`allow_pickle=False` is the default for loading: only enable for trusted files (pickle can execute code).

### 21.2 Text formats

```python
np.savetxt('data.csv', m, delimiter=',', fmt='%.4f', header='a,b,c', comments='')
m = np.loadtxt('data.csv', delimiter=',', skiprows=1)
m = np.genfromtxt('data.csv', delimiter=',', skip_header=1,
                  filling_values=np.nan, dtype=float)   # handles missing values
cols = np.loadtxt('d.csv', delimiter=',', usecols=(0, 2), unpack=True)
```

### 21.3 Raw binary

```python
a.tofile('raw.bin')
b = np.fromfile('raw.bin', dtype=np.float64)
a.tolist()
a.tobytes()
```

### 21.4 Memory mapping for huge arrays

```python
mm = np.memmap('big.dat', dtype='float32', mode='w+', shape=(10000, 1000))
mm[0] = 1.0
mm.flush()
```

---

## 22. einsum, tensordot, and Advanced Products

### 22.1 einsum

Einstein summation: describe the computation by index labels. Repeated labels are summed; labels after `->` are kept.

```python
A = np.random.rand(3, 4)
B = np.random.rand(4, 5)
v = np.random.rand(4)

np.einsum('ij,jk->ik', A, B)        # matrix multiply
np.einsum('ij,j->i', A, v)          # matrix-vector
np.einsum('i,i->', v, v)            # dot product
np.einsum('i,j->ij', v, v)          # outer product
np.einsum('ii->i', M)               # diagonal
np.einsum('ii', M)                  # trace
np.einsum('ij->ji', A)              # transpose
np.einsum('ij->', A)                # sum of all
np.einsum('ij->i', A)               # row sums
np.einsum('bij,bjk->bik', X, Y)     # batched matmul
np.einsum('bi,bi->b', U, V)         # row-wise dot products
np.einsum('...ij->...ji', T)        # transpose last two axes
np.einsum('ij,ij->', A, A)          # Frobenius norm squared
# Attention scores style: (batch, heads, q, d) x (batch, heads, k, d)
np.einsum('bhqd,bhkd->bhqk', Q, K)
```

Use `optimize=True` for multi-operand contractions.

### 22.2 tensordot

```python
np.tensordot(A, B, axes=1)               # ordinary matmul-like for 2D
np.tensordot(A, B, axes=([1], [0]))      # contract A's axis 1 with B's axis 0
```

---

## 23. Polynomials, FFT, Interpolation, Integration

### 23.1 Polynomials

```python
# Modern API
from numpy.polynomial import Polynomial
p = Polynomial([1, 2, 3])       # 1 + 2x + 3x^2 (lowest degree first!)
p(2)                            # evaluate
p.deriv(); p.integ()
p.roots()
Polynomial.fit(x, y, deg=3)     # least-squares fit

# Legacy
np.polyfit(x, y, 2)             # highest degree first
np.polyval([3, 2, 1], 2)
np.roots([1, -3, 2])            # roots of x^2 - 3x + 2 -> [2, 1]
np.polyder, np.polyint
```

### 23.2 FFT

```python
sig = np.sin(2 * np.pi * 5 * np.linspace(0, 1, 500, endpoint=False))
F = np.fft.fft(sig)
freqs = np.fft.fftfreq(sig.size, d=1 / 500)
mag = np.abs(F)
np.fft.rfft(sig)                # real input, half spectrum
np.fft.ifft(F)
np.fft.fft2(img)                # 2D (images)
np.fft.fftshift(F)
```

### 23.3 Interpolation and integration

```python
np.interp(2.5, xp=[1, 2, 3], fp=[10, 20, 30])    # linear 1D interpolation
np.trapezoid(y, x)              # numerical integration (np.trapz before 2.0)
np.cumsum(y) * dx
np.gradient(y, dx)              # numerical derivative
```

For advanced needs use **SciPy** (`scipy.interpolate`, `scipy.integrate`, `scipy.optimize`).

---

## 24. Memory Layout, Strides, Performance

### 24.1 C vs Fortran order

```python
a = np.arange(6).reshape(2, 3)         # C-order (row-major), default
a.flags['C_CONTIGUOUS']                # True
a.strides                              # (24, 8): step 24 bytes per row, 8 per column
f = np.asfortranarray(a)
f.strides                              # (8, 16)
np.ascontiguousarray(a.T)              # make a contiguous copy
```

Iterating along the last axis (C-order) is fastest. Operations on contiguous memory are faster.

### 24.2 Strides tricks (advanced, careful)

```python
from numpy.lib.stride_tricks import sliding_window_view, as_strided

x = np.arange(10)
w = sliding_window_view(x, window_shape=3)      # (8, 3) view, no copy
w.mean(axis=1)                                   # moving average
```

Prefer `sliding_window_view` over raw `as_strided` (which can read invalid memory).

### 24.3 Performance checklist

| Do | Avoid |
|---|---|
| Vectorize with ufuncs and broadcasting | Python `for` loops over elements |
| Preallocate (`np.empty`) then fill | `np.append` / `concatenate` inside loops |
| Use in-place ops (`+=`, `out=`) | Needless temporary arrays |
| Use `float32` when precision allows (half memory) | Silent upcasting to `float64` |
| Use views (slicing) | Unnecessary `.copy()` |
| Use `@`/BLAS for matrix math | Manual triple loops |
| `np.einsum(..., optimize=True)` | Naive chained `dot` on large tensors |
| Check `np.shares_memory` when unsure | Assuming fancy index = view |

### 24.4 Timing

```python
%timeit np.sum(a)                       # in Jupyter
import timeit
timeit.timeit(lambda: a.sum(), number=1000)
```

### 24.5 Beyond NumPy when you need more

Numba (`@njit`), Cython, CuPy (GPU, near-identical API), JAX, PyTorch tensors, Dask (out-of-core and parallel).

---

## 25. Vectorization Patterns

### 25.1 Replace loops with array expressions

```python
# Loop version
out = np.empty(n)
for i in range(n):
    out[i] = a[i] ** 2 + 3 * b[i]
# Vectorized
out = a ** 2 + 3 * b
```

### 25.2 Common recipes

```python
# Moving average
def moving_avg(x, k):
    c = np.cumsum(np.insert(x, 0, 0))
    return (c[k:] - c[:-k]) / k

# Normalize to [0, 1]
x = (x - x.min()) / (x.max() - x.min())

# Softmax (numerically stable)
def softmax(z, axis=-1):
    z = z - z.max(axis=axis, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=axis, keepdims=True)

# Sigmoid
sigmoid = lambda z: 1 / (1 + np.exp(-z))

# One-hot encoding
labels = np.array([0, 2, 1])
onehot = np.eye(3)[labels]

# Euclidean distance matrix
def pdist(X):
    sq = (X ** 2).sum(1)
    return np.sqrt(np.maximum(sq[:, None] + sq[None, :] - 2 * X @ X.T, 0))

# Group-by sum with bincount
group_ids = np.array([0, 1, 0, 2, 1])
vals = np.array([10., 20., 30., 40., 50.])
np.bincount(group_ids, weights=vals)       # [40, 70, 40]

# Rolling max / windowed ops
sliding_window_view(x, 5).max(axis=1)

# Cosine similarity matrix
Xn = X / np.linalg.norm(X, axis=1, keepdims=True)
S = Xn @ Xn.T

# Rotation matrix applied to many points (n, 2)
th = np.pi / 4
R = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
rotated = pts @ R.T
```

---

## 26. NumPy for Machine Learning (Worked Examples)

### 26.1 Linear regression (normal equation)

```python
rng = np.random.default_rng(0)
X = rng.random((100, 3))
true_w = np.array([2.0, -1.0, 0.5])
y = X @ true_w + 3 + rng.normal(0, 0.1, 100)

Xb = np.c_[np.ones(len(X)), X]                 # add bias column
w = np.linalg.solve(Xb.T @ Xb, Xb.T @ y)       # [bias, w1, w2, w3]
# or: w, *_ = np.linalg.lstsq(Xb, y, rcond=None)
```

### 26.2 Gradient descent

```python
w = np.zeros(Xb.shape[1])
lr, epochs = 0.1, 1000
for _ in range(epochs):
    grad = (2 / len(y)) * Xb.T @ (Xb @ w - y)
    w -= lr * grad
```

### 26.3 Logistic regression

```python
def sigmoid(z): return 1 / (1 + np.exp(-z))

def fit_logreg(X, y, lr=0.1, epochs=2000):
    w = np.zeros(X.shape[1])
    for _ in range(epochs):
        p = sigmoid(X @ w)
        w -= lr * X.T @ (p - y) / len(y)
    return w

def log_loss(y, p, eps=1e-12):
    p = np.clip(p, eps, 1 - eps)
    return -np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))
```

### 26.4 K-Means

```python
def kmeans(X, k, iters=100, seed=0):
    rng = np.random.default_rng(seed)
    C = X[rng.choice(len(X), k, replace=False)]
    for _ in range(iters):
        d = ((X[:, None, :] - C[None, :, :]) ** 2).sum(-1)   # (n, k)
        labels = d.argmin(1)
        newC = np.array([X[labels == j].mean(0) if np.any(labels == j) else C[j]
                         for j in range(k)])
        if np.allclose(newC, C):
            break
        C = newC
    return labels, C
```

### 26.5 Neural network forward and backward pass (2-layer MLP)

```python
def init(n_in, n_hid, n_out, seed=0):
    rng = np.random.default_rng(seed)
    return {
        'W1': rng.normal(0, np.sqrt(2 / n_in), (n_in, n_hid)),
        'b1': np.zeros(n_hid),
        'W2': rng.normal(0, np.sqrt(2 / n_hid), (n_hid, n_out)),
        'b2': np.zeros(n_out),
    }

def forward(P, X):
    z1 = X @ P['W1'] + P['b1']
    a1 = np.maximum(0, z1)                    # ReLU
    z2 = a1 @ P['W2'] + P['b2']
    return z1, a1, softmax(z2)

def backward(P, X, Y_onehot, z1, a1, probs):
    n = len(X)
    dz2 = (probs - Y_onehot) / n
    dW2 = a1.T @ dz2
    db2 = dz2.sum(0)
    da1 = dz2 @ P['W2'].T
    dz1 = da1 * (z1 > 0)
    dW1 = X.T @ dz1
    db1 = dz1.sum(0)
    return {'W1': dW1, 'b1': db1, 'W2': dW2, 'b2': db2}
```

### 26.6 Convolution (naive 2D) and image basics

```python
img = np.random.rand(28, 28)
kernel = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])   # Sobel x

from numpy.lib.stride_tricks import sliding_window_view
patches = sliding_window_view(img, (3, 3))               # (26, 26, 3, 3)
out = np.einsum('ijkl,kl->ij', patches, kernel)           # (26, 26)

# Image ops: img shape (H, W, 3) uint8
gray = (img_rgb @ np.array([0.299, 0.587, 0.114])).astype(np.uint8)
flipped = img_rgb[:, ::-1]
cropped = img_rgb[50:150, 100:200]
normalized = img_rgb.astype(np.float32) / 255.0
```

### 26.7 Train/test split and batching

```python
def train_test_split(X, y, test_size=0.2, seed=0):
    rng = np.random.default_rng(seed)
    idx = rng.permutation(len(X))
    cut = int(len(X) * (1 - test_size))
    tr, te = idx[:cut], idx[cut:]
    return X[tr], X[te], y[tr], y[te]

def batches(X, y, bs, rng):
    idx = rng.permutation(len(X))
    for i in range(0, len(X), bs):
        b = idx[i:i + bs]
        yield X[b], y[b]
```

### 26.8 Metrics

```python
accuracy = (y_pred == y_true).mean()
TP = np.sum((y_pred == 1) & (y_true == 1))
FP = np.sum((y_pred == 1) & (y_true == 0))
FN = np.sum((y_pred == 0) & (y_true == 1))
precision = TP / (TP + FP)
recall = TP / (TP + FN)
f1 = 2 * precision * recall / (precision + recall)
mse = np.mean((y - y_hat) ** 2)
r2 = 1 - ((y - y_hat) ** 2).sum() / ((y - y.mean()) ** 2).sum()
conf = np.zeros((k, k), int); np.add.at(conf, (y_true, y_pred), 1)   # confusion matrix
```

### 26.9 Simulation / robotics flavored examples

```python
# 2D rigid transform (homogeneous coordinates)
def transform(theta, tx, ty):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s, tx], [s, c, ty], [0, 0, 1]])

pts = np.array([[1, 0], [0, 1], [1, 1]]).T          # (2, n)
H = np.vstack([pts, np.ones(pts.shape[1])])          # (3, n)
moved = (transform(np.pi / 2, 2, 1) @ H)[:2]

# Euler integration of a simple dynamical system (mass-spring-damper)
dt, m, k, c = 0.01, 1.0, 10.0, 0.5
x, v = np.zeros(1000), np.zeros(1000)
x[0] = 1.0
for i in range(999):
    a = (-k * x[i] - c * v[i]) / m
    v[i + 1] = v[i] + a * dt
    x[i + 1] = x[i] + v[i + 1] * dt

# Batch of 3D rotation matrices about z (shape (n, 3, 3))
th = np.linspace(0, np.pi, 5)
Rz = np.zeros((5, 3, 3))
Rz[:, 0, 0] = np.cos(th); Rz[:, 0, 1] = -np.sin(th)
Rz[:, 1, 0] = np.sin(th); Rz[:, 1, 1] = np.cos(th)
Rz[:, 2, 2] = 1
rotated = Rz @ np.array([1.0, 0, 0])                 # (5, 3)
```

---

## 27. Common Pitfalls and Gotchas

1. **`*` is not matrix multiplication.** Use `@`.
2. **Slices are views.** Modifying a slice modifies the original; use `.copy()` if you need independence.
3. **`a = b` does not copy.** Both names refer to the same array.
4. **Integer division and overflow.** `np.array([1,2]) / 2` returns floats; `uint8` math wraps silently.
5. **`and`/`or` on arrays raise errors.** Use `&`, `|`, `~` with parentheses: `(a > 1) & (a < 5)`.
6. **`np.nan == np.nan` is `False`.** Use `np.isnan`.
7. **1D arrays are not row or column vectors.** Shape `(n,)` differs from `(n, 1)` and `(1, n)`. Broadcasting surprises come from here:
   ```python
   a = np.arange(3)          # (3,)
   a[:, None] + a[None, :]   # (3, 3) outer sum
   ```
8. **`np.append` copies every time.** Collect in a list, then convert once, or preallocate.
9. **`np.arange` with float steps** may give an unexpected length; use `linspace`.
10. **Mutable default and `np.empty`** contains garbage; never read before writing.
11. **`a[[0, 0, 1]] += 1` does not accumulate.** Use `np.add.at`.
12. **`np.vectorize` is not fast.** It is a loop in disguise.
13. **Mixed dtypes silently upcast** (int + float = float; bool + int = int).
14. **`reshape` of a non-contiguous array may copy**; `shape` assignment (`a.shape = ...`) raises instead.
15. **`np.float_`, `np.int_`, `np.bool8`, `np.object0`... aliases** were removed or changed in NumPy 2.0 (see next section).
16. **Comparing floats:** use `np.isclose`/`np.allclose`, not `==`.
17. **`np.matrix` is deprecated.** Always use `ndarray`.
18. **Axis confusion:** `axis=0` collapses rows (operates down columns). Use `keepdims=True` to keep broadcasting simple.
19. **`np.random.seed` is global state.** Prefer `default_rng`.
20. **Pickle risk:** do not `np.load(..., allow_pickle=True)` from untrusted files.

---

## 28. NumPy 2.x Changes

Key differences when upgrading from 1.x:

| Change | Details |
|---|---|
| Promotion rules (NEP 50) | Python scalars are "weak": `np.float32(3) + 3.0` stays `float32`; `np.uint8(1) + 300` can overflow or error |
| Removed aliases | `np.float_`, `np.complex_`, `np.Inf`, `np.NaN`, `np.PINF`, `np.infty`, `np.string_`, `np.unicode_`: use `np.float64`, `np.complex128`, `np.inf`, `np.nan`, `np.bytes_`, `np.str_` |
| `np.trapz` | Renamed `np.trapezoid` (old name deprecated) |
| `np.in1d` | Deprecated; use `np.isin` |
| `np.row_stack` | Deprecated; use `np.vstack` |
| `np.cast`, `np.source`, `np.who`, `np.lookfor` | Removed or moved |
| `copy=False` | Now means "never copy, raise if needed"; use `copy=None` for "copy only if needed" |
| `np.linalg.*` | Now has `np.linalg.matrix_transpose`, `vecdot`, `matvec`; also `np.matvec`, `np.vecmat` |
| `np.unique` | New `sorted` and `equal_nan` options; results may be in different layout |
| New | `np.StringDType` (variable-length strings), `np.strings` module, improved `np.bool` name, array API standard compliance (`np.astype`, `np.isdtype`, `np.unstack`) |
| C API | ABI changes: compiled extensions must be rebuilt for 2.x |

Run `ruff check --select NPY201 .` to find 2.0 incompatibilities automatically.

---

## 29. Practice Problems with Solutions

**Problem 1.** Create a 5x5 matrix with 1s on the border and 0s inside.

```python
a = np.ones((5, 5), int)
a[1:-1, 1:-1] = 0
```

**Problem 2.** Create a checkerboard 8x8 pattern.

```python
a = np.zeros((8, 8), int)
a[1::2, ::2] = 1
a[::2, 1::2] = 1
# or: (np.indices((8, 8)).sum(0) % 2)
```

**Problem 3.** Normalize each row of a matrix to unit length.

```python
X = X / np.linalg.norm(X, axis=1, keepdims=True)
```

**Problem 4.** Find the second largest value in each row.

```python
np.sort(X, axis=1)[:, -2]
```

**Problem 5.** Replace all negative values in an array with the mean of non-negative ones.

```python
a[a < 0] = a[a >= 0].mean()
```

**Problem 6.** Given a 1D array, compute a moving average of window 3.

```python
np.convolve(a, np.ones(3) / 3, mode='valid')
```

**Problem 7.** Find the indices of the 3 largest elements.

```python
np.argsort(a)[-3:][::-1]
# faster for big arrays: np.argpartition(a, -3)[-3:]
```

**Problem 8.** Compute the pairwise Euclidean distance between rows of X (n, d) without loops.

```python
sq = (X ** 2).sum(1)
D = np.sqrt(np.maximum(sq[:, None] + sq[None] - 2 * X @ X.T, 0))
```

**Problem 9.** Count occurrences of each unique value.

```python
vals, counts = np.unique(a, return_counts=True)
```

**Problem 10.** One-hot encode `[2, 0, 1, 2]` with 3 classes.

```python
np.eye(3)[[2, 0, 1, 2]]
```

**Problem 11.** Remove rows containing any NaN.

```python
X = X[~np.isnan(X).any(axis=1)]
```

**Problem 12.** Compute the cumulative maximum of an array.

```python
np.maximum.accumulate(a)
```

**Problem 13.** Standardize columns (z-score), safe against zero std.

```python
std = X.std(0)
Z = (X - X.mean(0)) / np.where(std == 0, 1, std)
```

**Problem 14.** Given points (n, 2), find the one closest to the origin.

```python
pts[np.argmin(np.linalg.norm(pts, axis=1))]
```

**Problem 15.** Build a Vandermonde-based polynomial fit of degree 2 using only linear algebra.

```python
V = np.vander(x, 3)                           # columns: x^2, x, 1
coef = np.linalg.lstsq(V, y, rcond=None)[0]
```

---

## 30. Phase 1 Deep Dive: Foundations

### 30.1 When NumPy is (and is not) the right tool

| Use NumPy when | Use something else when |
|---|---|
| Large homogeneous numeric data | Small data where a list is clearer |
| Math over whole arrays (vectorized) | Mixed types per column (use **Pandas**) |
| Linear algebra, FFT, random sampling | Sparse matrices (use `scipy.sparse`) |
| Image, signal, simulation grids | Data larger than RAM (use `memmap`, **Dask**, **Zarr**) |
| Feeding ML libraries | GPU or autodiff needed (use **PyTorch**, **JAX**, **CuPy**) |

### 30.2 Mental model: one buffer plus metadata

An `ndarray` is a raw block of memory plus a description of how to read it:

```
data pointer  ->  [ 0 | 1 | 2 | 3 | 4 | 5 ]   (contiguous bytes)
dtype         ->  int32   (4 bytes each)
shape         ->  (2, 3)
strides       ->  (12, 4) (bytes to jump per axis)
```

Different arrays can describe the **same buffer** differently, which is why views are free:

```python
a = np.arange(6, dtype=np.int32)
b = a.reshape(2, 3)                  # same buffer, new shape/strides
c = a.view(np.uint8)                 # same buffer, reinterpreted as bytes -> shape (24,)
a.__array_interface__['data'][0] == b.__array_interface__['data'][0]   # True
a.__array_interface__                # pointer, shape, strides, typestr
```

### 30.3 List vs array vs `array.array`

| Feature | `list` | `array.array` | `np.ndarray` |
|---|---|---|---|
| Mixed types | Yes | No | No |
| Memory per element | ~28+ bytes (objects) | Fixed | Fixed (`itemsize`) |
| Math on whole container | No | No | Yes (vectorized) |
| N-dimensional | Nested lists | No | Yes |
| Slicing | Copy | Copy | **View** |
| Speed on numeric loops | Slow | Slow | Fast |

### 30.4 Scalars, 0-d arrays, and NumPy scalar types

```python
s = np.float64(3.5)          # NumPy scalar (type np.float64), immutable
z = np.array(3.5)            # 0-d array, shape ()
z.shape, z.ndim              # (), 0
z.item()                     # Python float 3.5
s.dtype, type(s)
isinstance(s, np.generic)    # True: base class of NumPy scalars
```

NumPy scalars behave like arrays in most operations (`.shape`, `.astype`, etc.), but Python `float` is faster for single-value math inside loops.

### 30.5 The ecosystem map

```
NumPy ──► SciPy (algorithms: optimize, integrate, signal, sparse, stats)
      ├─► Pandas (labelled tabular data)
      ├─► Matplotlib / Seaborn / Plotly (visualization)
      ├─► scikit-learn (classic ML)
      ├─► PyTorch / TensorFlow / JAX (deep learning, autodiff, GPU)
      ├─► OpenCV / Pillow / scikit-image (images are ndarrays)
      └─► Numba / Cython / CuPy / Dask (speed and scale)
```

### 30.6 Habits that prevent bugs from day one

```python
print(a.shape, a.dtype)                       # inspect constantly
assert X.shape == (n_samples, n_features)     # document and enforce shapes
y = y.reshape(-1, 1)                          # be explicit about column vectors
# Comment shapes in your code:
Z = X @ W            # (n, d) @ (d, k) -> (n, k)
```

### Checkpoint 1

1. Why is `a[1:3]` free but `a[[1, 2]]` not? *(Slices are views of the same buffer; fancy indexing builds a new array.)*
2. What 3 things besides the data does an ndarray store? *(dtype, shape, strides.)*
3. When is a Python list better? *(Tiny data, mixed types, frequent appends.)*

---

## 31. Phase 2 Deep Dive: Creating and Inspecting Arrays

### 31.1 More creation tools

```python
np.array([1, 2, 3], ndmin=2)            # shape (1, 3)
np.asanyarray(x)                        # keeps subclasses (e.g., masked arrays)
np.ascontiguousarray(x)                 # guarantee C-contiguous (copies if needed)
np.copy(a)                              # same as a.copy()

# r_ and c_: quick concatenation / range builders
np.r_[1:4, 10, 20]                      # [ 1  2  3 10 20]
np.r_[0:1:5j]                           # complex step = number of points -> linspace
np.c_[[1, 2, 3], [4, 5, 6]]             # columns side by side, shape (3, 2)

np.indices((2, 3))                      # coordinate grids, shape (2, 2, 3)
np.vander([1, 2, 3], 3)                 # [[1 1 1] [4 2 1] [9 3 1]]
np.diagflat([1, 2])                     # diagonal matrix from flattened input
np.tri(3, 3, k=-1)                      # strictly lower triangle of ones
```

Creating from a function over indices:

```python
np.fromfunction(lambda i, j: (i + j) % 2, (4, 4), dtype=int)    # checkerboard
```

### 31.2 Inspecting arrays: everything you can ask

```python
a = np.arange(12, dtype=np.float32).reshape(3, 4)

np.shape(a), np.ndim(a), np.size(a)
a.item(5)                               # Python scalar at flat index 5
a.tolist()                              # nested Python lists
np.array2string(a, separator=', ', precision=2)
np.array_repr(a)

with np.printoptions(precision=2, suppress=True):    # temporary print settings
    print(a / 3)

a.flags                                  # C_CONTIGUOUS, F_CONTIGUOUS, OWNDATA, WRITEABLE
a.flags.writeable = False                # make read-only (protects against accidental edits)
a.base is None                           # True if this array owns its data
```

### 31.3 dtype introspection

```python
a.dtype.kind          # 'b' bool, 'i' int, 'u' uint, 'f' float, 'c' complex,
                      # 'U' unicode, 'S' bytes, 'M' datetime, 'm' timedelta, 'O' object
a.dtype.name          # 'float32'
a.dtype.itemsize      # 4
a.dtype.byteorder     # '=' native, '<' little, '>' big
np.issubdtype(a.dtype, np.floating)       # True
np.isdtype(a.dtype, 'real floating')      # NumPy 2.x
np.can_cast(np.int16, np.int32)           # True  (safe)
np.can_cast(np.int32, np.int16)           # False (could overflow)
np.can_cast(np.float64, np.int32, casting='unsafe')   # True (forced)
```

Casting modes: `'no'`, `'equiv'`, `'safe'`, `'same_kind'`, `'unsafe'`.

### 31.4 A reusable "describe" helper

```python
def describe(a):
    a = np.asarray(a)
    print(f"shape={a.shape} ndim={a.ndim} size={a.size} dtype={a.dtype} "
          f"nbytes={a.nbytes} C={a.flags.c_contiguous} owns={a.base is None}")
    if a.size and np.issubdtype(a.dtype, np.number):
        print(f"min={a.min():.4g} max={a.max():.4g} mean={a.mean():.4g}")

describe(np.random.rand(3, 4))
```

### Checkpoint 2

1. Difference between `np.empty` and `np.zeros`? *(`empty` is uninitialized garbage, faster.)*
2. How do you build `[0, .25, .5, .75, 1]` three ways? *(`linspace(0,1,5)`, `arange(0,1.25,.25)`, `r_[0:1:5j]`.)*
3. How do you make an array read-only? *(`a.flags.writeable = False`.)*

---

## 32. Phase 3 Deep Dive: Indexing and Manipulation

### 32.1 `take_along_axis` / `put_along_axis`: per-row (or per-column) indexing

The cleanest way to apply an `argsort` / `argmax` result row by row:

```python
m = np.array([[3, 1, 2],
              [9, 7, 8]])

idx = m.argsort(axis=1)
np.take_along_axis(m, idx, axis=1)           # sort each row: [[1 2 3] [7 8 9]]

j = m.argmax(axis=1, keepdims=True)          # shape (2, 1)
np.take_along_axis(m, j, axis=1)             # max of each row, shape (2, 1)

np.put_along_axis(m, idx[:, :1], 0, axis=1)  # zero the smallest in each row (in place)
```

### 32.2 More selection tools

```python
np.compress([True, False, True], m, axis=1)  # keep columns 0 and 2
np.diagonal(m)                               # view of the diagonal
np.fill_diagonal(M, 0)                       # set diagonal in place
np.triu_indices_from(M, k=1)                 # indices of strict upper triangle
M[np.triu_indices_from(M, k=1)]              # values of the upper triangle

np.putmask(a, a > 5, 0)                      # in-place conditional assign
np.place(a, a > 5, [1, 2, 3])                # fill True positions from sequence (cycled)
np.trim_zeros(np.array([0, 0, 1, 2, 0]))     # [1 2]
```

### 32.3 Iterating (use sparingly, prefer vectorization)

```python
m = np.arange(6).reshape(2, 3)

for idx, val in np.ndenumerate(m):           # (row, col), value
    pass
for idx in np.ndindex(2, 3):                 # all index tuples
    pass
for x in m.flat:                             # flat iterator
    pass

# nditer with write access
with np.nditer(m, op_flags=['readwrite']) as it:
    for x in it:
        x[...] = x * 2
```

### 32.4 Mixing basic and advanced indexing: the shape rule

```python
x = np.arange(24).reshape(2, 3, 4)

x[:, 1, [0, 3]].shape      # (2, 2)  advanced indices adjacent -> dims stay in place
x[0, :, [0, 1]].shape      # (2, 3)  advanced indices separated by a slice ->
                           #         advanced dim goes FIRST (famous gotcha)
x[:, :, [0, 3]].shape      # (2, 3, 2)
```

When shapes surprise you, print `.shape` and, if needed, build the selection in two steps: `x[0][:, [0, 1]]`.

### 32.5 Updating data: common patterns

```python
a = np.array([4, -1, 7, -3, 0])

a[a < 0] = 0                        # clamp negatives
a = np.clip(a, 0, 5)                # clamp both ends
a = np.where(a % 2 == 0, a, a + 1)  # conditional update (returns new array)
a[::2] *= 10                        # in-place on a strided view
a[[0, -1]] = a[[-1, 0]]             # swap first and last (fancy RHS is a copy, so safe)

m[1:3, 1:3] = np.array([[1, 2], [3, 4]])    # block assignment
m[:, 0] = m[:, 1] + m[:, 2]                 # column from other columns
m[np.arange(len(m)), j.ravel()] = -1        # set one chosen column per row
```

### 32.6 Reshape cookbook

```python
x = np.arange(24)

x.reshape(2, 3, 4)
x.reshape(-1, 6)                             # infer rows
x.reshape(4, 6).reshape(2, 2, 6)             # reshape is just re-reading the buffer
img = x.reshape(2, 3, 4)                     # (batch, rows, cols)
np.moveaxis(img, 0, -1).shape                # (3, 4, 2)
img.transpose(2, 0, 1).shape                 # (4, 2, 3)  arbitrary axis permutation
img.reshape(img.shape[0], -1).shape          # flatten all but batch: (2, 12)

# Split an axis into two (e.g., 24 -> 6 x 4) and merge back
x.reshape(6, 4).reshape(24)

# Interleave two arrays
a, b = np.array([1, 2, 3]), np.array([10, 20, 30])
np.stack([a, b], axis=1).ravel()             # [1 10 2 20 3 30]
```

### Checkpoint 3

1. `x` has shape `(2, 3, 4)`. What is `x[0, :, [0, 1]].shape`? *(`(2, 3)`.)*
2. How do you get the max of each row together with its column index? *(`j = m.argmax(1)`; `m[np.arange(len(m)), j]`.)*
3. Why does `a[[0, 1]] = a[[1, 0]]` swap correctly? *(Right side is evaluated first into a copy.)*

---

## 33. Phase 4 Deep Dive: Operations and Broadcasting

### 33.1 Logical, comparison, and bitwise functions

```python
a = np.array([1, 4, 7, 10])

np.logical_and(a > 2, a < 9)       # same as (a > 2) & (a < 9)
np.logical_or(a < 2, a > 9)
np.logical_not(a > 5)
np.logical_xor(a > 2, a < 9)

np.greater(a, 3); np.less_equal(a, 7); np.equal(a, 4); np.not_equal(a, 4)

# Bitwise on integers
np.bitwise_and(12, 10)             # 8     (12 & 10)
12 | 10, 12 ^ 10, ~12              # 14, 6, -13
1 << 3, 16 >> 2                    # 8, 4
np.unpackbits(np.array([5], dtype=np.uint8))   # [0 0 0 0 0 1 0 1]
np.packbits([1, 0, 1])                         # pack bool/bit array into bytes
```

> `&`, `|`, `~` on **boolean arrays** are logical; on **integer arrays** they are bitwise. Mixing them up is a classic bug.

### 33.2 Floating-point errors: `errstate` and `seterr`

```python
with np.errstate(divide='ignore', invalid='ignore'):
    r = np.array([1.0, 0.0]) / np.array([0.0, 0.0])    # [inf, nan], no warning

np.seterr(all='raise')                 # turn warnings into exceptions (good for debugging)
np.seterr(all='warn')                  # default-ish
old = np.seterr(over='ignore'); np.seterr(**old)       # save and restore
```

Safe division:

```python
out = np.zeros_like(a, dtype=float)
np.divide(a, b, out=out, where=(b != 0))
```

### 33.3 Integer vs float semantics

```python
np.array([-7]) // 2        # [-4]   floor division (toward -inf)
np.mod(-7, 2)              # 1      sign follows divisor (like Python)
np.fmod(-7, 2)             # -1     sign follows dividend (like C)
np.divmod(np.array([7, -7]), 2)

np.round([0.5, 1.5, 2.5])  # [0. 2. 2.]  round-half-to-even ("banker's rounding")
np.int8(127) + np.int8(1)  # scalar overflow -> RuntimeWarning
np.array([127], dtype=np.int8) + 1    # array overflow -> wraps silently (-128)
```

### 33.4 Floating-point precision

```python
0.1 + 0.2 == 0.3                       # False
np.isclose(0.1 + 0.2, 0.3)             # True
np.finfo(np.float64).eps               # 2.22e-16 (relative spacing near 1.0)
np.spacing(1e16)                       # gap to next float at that magnitude
np.nextafter(1.0, 2.0)

x32 = np.full(10_000_000, 0.1, dtype=np.float32)
x32.sum()                              # NumPy uses pairwise summation (fairly accurate)
x32.sum(dtype=np.float64)              # more accurate accumulator
import math; math.fsum(x32[:1000])     # exactly rounded sum for small data
```

Rule: accumulate in `float64` when inputs are `float32` or `float16`.

### 33.5 Numerical stability toolkit

```python
# log-sum-exp (stable)
def logsumexp(z, axis=-1):
    m = z.max(axis=axis, keepdims=True)
    return (m + np.log(np.exp(z - m).sum(axis=axis, keepdims=True))).squeeze(axis)

# stable sigmoid
def sigmoid(z):
    out = np.empty_like(z, dtype=float)
    pos = z >= 0
    out[pos] = 1 / (1 + np.exp(-z[pos]))
    ez = np.exp(z[~pos])
    out[~pos] = ez / (1 + ez)
    return out

np.log1p(1e-10)       # accurate log(1 + x) for tiny x
np.expm1(1e-10)       # accurate exp(x) - 1 for tiny x
np.hypot(3e200, 4e200)  # avoids overflow in sqrt(x^2 + y^2)
np.clip(p, 1e-12, 1 - 1e-12)   # avoid log(0)
```

### 33.6 `frompyfunc` and `vectorize` (convenience, not speed)

```python
f = np.frompyfunc(lambda x, y: x + 2 * y, 2, 1)      # returns object arrays
f(np.arange(3), np.arange(3)).astype(int)

vnorm = np.vectorize(np.linalg.norm, signature='(n)->()')
vnorm(np.random.rand(5, 3))                           # norm of each row
```

### 33.7 Broadcasting: debugging recipe and patterns

**Debug recipe when you get `operands could not be broadcast together`:**

1. Print both shapes.
2. Right-align them.
3. For each column, the sizes must be equal or one must be 1.
4. Fix by adding an axis (`[:, None]`), transposing, or reshaping.

Common patterns:

| Goal | Code | Shapes |
|---|---|---|
| Subtract column means | `X - X.mean(0)` | (n,d) - (d,) |
| Subtract row means | `X - X.mean(1, keepdims=True)` | (n,d) - (n,1) |
| Scale each row by a vector | `X * w[:, None]` | (n,d) * (n,1) |
| Outer operation | `a[:, None] * b[None, :]` | (n,1)*(1,m) -> (n,m) |
| All pairwise differences | `a[:, None] - a[None, :]` | (n,1)-(1,n) |
| Batch of matrices times vector | `A @ v` | (b,n,n) @ (n,) -> (b,n) |
| Add bias to batch activations | `Z + b` | (batch,k) + (k,) |
| Mask rows | `X[mask[:, None] & other]` | (n,1) & (n,d) |

Three-way broadcasting example (distance from every point to every centroid, per batch):

```python
P = np.random.rand(4, 100, 3)      # (batch, points, dim)
C = np.random.rand(4, 5, 3)        # (batch, centroids, dim)
D = np.linalg.norm(P[:, :, None, :] - C[:, None, :, :], axis=-1)   # (4, 100, 5)
```

Memory warning: this builds a `(4, 100, 5, 3)` temporary. For huge inputs, use `||a||^2 + ||b||^2 - 2ab` or chunk the work.

### Checkpoint 4

1. Result shape of `(5,1,3) + (4,1)`? *(`(5,4,3)`.)*
2. Why is `np.round(2.5)` equal to `2.0`? *(Round-half-to-even.)*
3. How do you stop `0/0` warnings for a block of code? *(`with np.errstate(divide='ignore', invalid='ignore'):`.)*

---

## 34. Phase 5 Deep Dive: Array Processing

### 34.1 Applying functions along axes

```python
m = np.array([[1, 5, 2], [9, 3, 4]])

np.apply_along_axis(lambda r: r.max() - r.min(), 1, m)    # range of each row
np.apply_over_axes(np.sum, m, [0, 1])                     # sum over several axes
```

Both are Python loops under the hood. If a built-in reduction exists (`ptp`, `sum`, `max`), use it.

### 34.2 Top-k per row (fast) and ranking

```python
X = np.random.rand(5, 10)
k = 3
idx = np.argpartition(-X, k, axis=1)[:, :k]               # unordered top-k indices
vals = np.take_along_axis(X, idx, axis=1)
order = np.argsort(-vals, axis=1)
idx = np.take_along_axis(idx, order, axis=1)              # ordered top-k indices
vals = np.take_along_axis(vals, order, axis=1)

ranks = a.argsort().argsort()                              # rank of each element (0 = smallest)
```

### 34.3 Sorting recipes

```python
A[np.lexsort(A.T[::-1])]                  # sort rows lexicographically (col 0, then 1, ...)
A[A[:, 2].argsort(kind='stable')]         # sort rows by column 2, stable
A[np.argsort(-A[:, 0])]                   # descending by column 0
np.sort(a)[::-1]                          # descending

# Sort one array by another
names_sorted = names[scores.argsort()[::-1]]
```

### 34.4 Unique, duplicates, and order preservation

```python
a = np.array([3, 1, 3, 2, 1])

u, first_idx = np.unique(a, return_index=True)
a[np.sort(first_idx)]                      # unique, original order -> [3 1 2]

x = np.array([1, 1, 2, 2, 2, 3, 1])
x[np.r_[True, x[1:] != x[:-1]]]            # drop consecutive duplicates -> [1 2 3 1]

dup_mask = np.ones(len(a), bool)
dup_mask[first_idx] = False                # True where an element is a repeat
```

### 34.5 Run-length encoding and change points

```python
x = np.array([1, 1, 2, 2, 2, 3])
starts = np.r_[0, np.flatnonzero(np.diff(x)) + 1]
lengths = np.diff(np.r_[starts, len(x)])
values = x[starts]                         # values [1 2 3], lengths [2 3 1]

# Local maxima (peaks) of a signal
y = np.array([0, 2, 1, 3, 1, 0])
peaks = np.flatnonzero((y[1:-1] > y[:-2]) & (y[1:-1] > y[2:])) + 1     # [1 3]
```

### 34.6 Group-by without Pandas

```python
keys = np.array(['a', 'b', 'a', 'c', 'b'])
vals = np.array([10., 20., 30., 40., 50.])

uniq, inv = np.unique(keys, return_inverse=True)
sums = np.bincount(inv, weights=vals)
counts = np.bincount(inv)
means = sums / counts                      # per-group mean

mx = np.full(len(uniq), -np.inf)
np.maximum.at(mx, inv, vals)               # per-group max

# Split array into groups
order = np.argsort(keys, kind='stable')
groups = np.split(vals[order], np.cumsum(counts)[:-1])
```

### 34.7 Binning and searching

```python
x = np.array([0.1, 2.5, 3.7, 9.9])
bins = np.array([0, 1, 5, 10])
np.digitize(x, bins)                       # [1 2 2 3] bin index (1-based)
np.searchsorted(bins, x, side='right') - 1 # [0 1 1 2] 0-based bin index
counts, edges = np.histogram(x, bins=bins)

np.searchsorted(sorted_arr, queries)       # vectorized binary search (O(log n) each)
```

### 34.8 Filtering recipes

```python
# Remove outliers (IQR rule)
q1, q3 = np.percentile(x, [25, 75])
iqr = q3 - q1
x_clean = x[(x >= q1 - 1.5 * iqr) & (x <= q3 + 1.5 * iqr)]

# z-score filter
z = (x - x.mean()) / x.std()
x_clean = x[np.abs(z) < 3]

# Rows where ALL / ANY / a specific column satisfies a condition
X[(X > 0).all(axis=1)]
X[(X > 0).any(axis=1)]
X[(X[:, 0] > 1) & (X[:, 2] < 5)]

# Keep rows whose id is in a whitelist
X[np.isin(ids, [3, 7, 9])]

# Drop rows/columns with NaN
X[~np.isnan(X).any(axis=1)]
X[:, ~np.isnan(X).any(axis=0)]

# Index of the first element satisfying a condition (or -1)
i = np.argmax(x > 5) if (x > 5).any() else -1
```

### 34.9 Combining and splitting (extra cases)

```python
np.concatenate([a, b], axis=0, dtype=float)   # force output dtype
np.insert(m, 1, [9, 9, 9], axis=0)            # insert a row
np.delete(m, [0, 2], axis=1)                  # delete columns
np.block([[A, B], [C, D]])                    # assemble block matrix
np.array_split(X, 3)                          # near-equal chunks (for batching)
chunks = np.array_split(np.arange(10), [2, 5])  # split at indices
```

### Checkpoint 5

1. How do you sort rows of a 2D array by column 1 descending? *(`A[np.argsort(-A[:, 1])]`.)*
2. How do you get the top 3 values per row without a full sort? *(`argpartition` + `take_along_axis`.)*
3. How do you compute a group-by mean in NumPy? *(`unique(return_inverse)` + `bincount` with weights, divide by counts.)*

---

## 35. Phase 6 Deep Dive: Random Numbers and Linear Algebra

### 35.1 Generators, bit generators, state, and parallel streams

```python
from numpy.random import Generator, PCG64, Philox, SeedSequence

rng = Generator(PCG64(123))               # explicit bit generator (default_rng uses PCG64)
state = rng.bit_generator.state           # snapshot the state
a = rng.random(3)
rng.bit_generator.state = state           # restore
b = rng.random(3)                         # identical to a

# Independent streams for parallel workers
ss = SeedSequence(2026)
streams = [Generator(PCG64(s)) for s in ss.spawn(4)]
# NumPy >= 1.25: children = rng.spawn(4)

Generator(Philox(7))                      # counter-based generator, good for parallel use
```

### 35.2 More distributions

| Call | Distribution |
|---|---|
| `rng.geometric(p, n)` | trials until first success |
| `rng.lognormal(mean, sigma, n)` | log of normal |
| `rng.chisquare(df, n)` | chi-square |
| `rng.standard_t(df, n)` | Student's t |
| `rng.f(dfnum, dfden, n)` | F distribution |
| `rng.dirichlet(alpha, n)` | probability vectors |
| `rng.multinomial(trials, pvals, n)` | counts per category |
| `rng.hypergeometric(ngood, nbad, nsample, n)` | sampling without replacement |
| `rng.negative_binomial(r, p, n)` | failures before r successes |
| `rng.laplace`, `rng.logistic`, `rng.pareto`, `rng.weibull` | heavy-tail / lifetime models |
| `rng.triangular(left, mode, right, n)` | simple bounded model |
| `rng.vonmises(mu, kappa, n)` | circular data (angles) |

### 35.3 Sampling recipes

```python
rng = np.random.default_rng(0)

# Bootstrap confidence interval for the mean
data = rng.normal(5, 2, 200)
boot = rng.choice(data, size=(5000, data.size), replace=True).mean(axis=1)
ci = np.percentile(boot, [2.5, 97.5])

# Monte Carlo estimate of pi
pts = rng.random((1_000_000, 2))
pi_est = 4 * np.mean((pts ** 2).sum(axis=1) <= 1)

# Random walk
walk = rng.choice([-1, 1], size=1000).cumsum()

# Shuffle features and labels together
perm = rng.permutation(len(X)); X, y = X[perm], y[perm]

# Weighted sampling without replacement
rng.choice(len(p), size=5, replace=False, p=p)

# Random orthogonal matrix (QR of Gaussian)
Q, R = np.linalg.qr(rng.normal(size=(4, 4)))
Q *= np.sign(np.diag(R))

# Central limit theorem demo
means = rng.exponential(1.0, size=(10000, 50)).mean(axis=1)    # approx normal
# Sanity check any sampler
sample = rng.normal(3, 2, 100_000)
sample.mean(), sample.std()           # about 3 and 2
```

### 35.4 Linear algebra: more tools

```python
A = np.array([[4., 1.], [2., 3.]])
S = np.array([[2., 1.], [1., 2.]])

np.linalg.eigvals(A)                  # eigenvalues only
np.linalg.eigvalsh(S)                 # symmetric: real, sorted
np.linalg.matrix_rank(A)

# NumPy 2.x helpers
np.linalg.vector_norm(v)              # also np.linalg.matrix_norm(A, ord='fro')
np.linalg.matrix_transpose(Xb)        # transposes the last two axes
np.vecdot(a, b)                       # dot along last axis (conjugates a)

# Error handling
try:
    np.linalg.inv(np.array([[1., 2.], [2., 4.]]))
except np.linalg.LinAlgError as e:
    print("singular:", e)
```

Solve many right-hand sides at once, and verify:

```python
A = np.random.rand(3, 3) + 3 * np.eye(3)
B = np.random.rand(3, 4)
X = np.linalg.solve(A, B)             # (3, 4)
np.allclose(A @ X, B)                 # True
residual = np.linalg.norm(A @ X - B)
```

### 35.5 Linear algebra recipes you will reuse

```python
# Ridge regression (closed form)
w = np.linalg.solve(X.T @ X + lam * np.eye(X.shape[1]), X.T @ y)

# Gram-Schmidt / orthonormal basis via QR
Q, _ = np.linalg.qr(A)                # columns of Q span the column space of A

# Orthogonal projection of vector b onto column space of A
P = A @ np.linalg.pinv(A)
b_proj = P @ b

# Low-rank approximation (compression, denoising)
U, s, Vt = np.linalg.svd(M, full_matrices=False)
k = 10
M_k = (U[:, :k] * s[:k]) @ Vt[:k]
rel_err = np.linalg.norm(M - M_k) / np.linalg.norm(M)
energy = (s[:k] ** 2).sum() / (s ** 2).sum()

# Power iteration (dominant eigenpair)
def power_iter(A, iters=200, seed=0):
    v = np.random.default_rng(seed).normal(size=A.shape[0])
    for _ in range(iters):
        v = A @ v
        v /= np.linalg.norm(v)
    return v @ A @ v, v

# Symmetric positive definite check
def is_spd(S):
    try:
        np.linalg.cholesky(S); return True
    except np.linalg.LinAlgError:
        return False

# Markov chain stationary distribution
P = np.array([[0.9, 0.1], [0.5, 0.5]])
vals, vecs = np.linalg.eig(P.T)
pi = np.real(vecs[:, np.argmax(np.isclose(vals, 1))])
pi /= pi.sum()                        # [0.8333, 0.1667]

# Ill-conditioning demo (Hilbert matrix)
n = 10
H = 1 / (np.arange(1, n + 1)[:, None] + np.arange(n))
np.linalg.cond(H)                     # about 1e13: solving with H loses ~13 digits

# Orthogonality and identity checks
np.allclose(Q.T @ Q, np.eye(Q.shape[1]))
np.allclose(A @ np.linalg.inv(A), np.eye(len(A)))

# Rotation matrix check: det = +1 and R.T @ R = I
```

### 35.6 Batched linear algebra

Most `np.linalg` functions work on stacks of matrices (leading axes are batch axes):

```python
As = np.random.rand(100, 3, 3) + 3 * np.eye(3)
bs = np.random.rand(100, 3, 1)
xs = np.linalg.solve(As, bs)          # (100, 3, 1)
dets = np.linalg.det(As)              # (100,)
vals = np.linalg.eigvals(As)          # (100, 3)
```

### Checkpoint 6

1. Why prefer `default_rng(seed)` over `np.random.seed`? *(Local, reproducible, better algorithms; no hidden global state.)*
2. Why use `solve` instead of `inv(A) @ b`? *(Faster and more accurate.)*
3. What does a large `cond(A)` tell you? *(Small input errors may become large output errors.)*

---

## 36. Phase 7 Deep Dive: Advanced NumPy

### 36.1 Missing data workflows

```python
X = np.array([[1, np.nan, 3],
              [4, 5, np.nan],
              [7, 8, 9]])

nan_per_col = np.isnan(X).sum(axis=0)             # count missing per column
col_mean = np.nanmean(X, axis=0)
X_mean = np.where(np.isnan(X), col_mean, X)       # mean imputation
col_med = np.nanmedian(X, axis=0)
X_med = np.where(np.isnan(X), col_med, X)         # median imputation

# Forward fill (1D)
def ffill(x):
    idx = np.where(~np.isnan(x), np.arange(len(x)), 0)
    np.maximum.accumulate(idx, out=idx)
    return x[idx]

# Linear interpolation of NaNs (1D)
x = np.array([1., np.nan, np.nan, 4.])
nans = np.isnan(x); xs = np.arange(len(x))
x[nans] = np.interp(xs[nans], xs[~nans], x[~nans])      # [1 2 3 4]

# Sentinel values (-999) -> NaN
data = np.where(data == -999, np.nan, data.astype(float))
```

Masked arrays carry the mask through operations:

```python
import numpy.ma as ma
m = ma.masked_invalid(X)
m.mean(axis=0)                 # ignores masked entries
m.filled(0)                    # replace masked with 0
ma.count(m, axis=0)            # valid entries per column
m.fill_value = -1
```

### 36.2 Files: details that matter

```python
# Text
np.loadtxt('f.csv', delimiter=',', skiprows=1, usecols=(0, 2),
           dtype=float, max_rows=1000, comments='#')
rec = np.genfromtxt('f.csv', delimiter=',', names=True, dtype=None, encoding='utf-8')
rec['age']                                  # access columns by header name
np.savetxt('out.csv', M, delimiter=',', fmt='%.6f', header='a,b,c', comments='')

# Native binary (.npy / .npz)
np.save('a.npy', a)                         # file starts with magic bytes \x93NUMPY
np.savez('bundle.npz', X=X, y=y)            # use np.savez_compressed to shrink
bundle = np.load('bundle.npz'); bundle['X']

# Larger than RAM
mm = np.load('big.npy', mmap_mode='r')      # read lazily, slices touch only needed pages
out = np.lib.format.open_memmap('new.npy', mode='w+', dtype='float32', shape=(100_000, 100))

def chunked_mean(mm, chunk=100_000):
    total, n = 0.0, 0
    for i in range(0, len(mm), chunk):
        part = mm[i:i + chunk]
        total += part.sum(dtype=np.float64); n += part.size
    return total / n

# Raw binary with explicit layout and endianness
arr = np.fromfile('raw.bin', dtype='<f4', count=1000, offset=128)   # little-endian float32
hdr_dt = np.dtype([('magic', 'S4'), ('n', '<u4'), ('scale', '<f4')])
header = np.fromfile('raw.bin', dtype=hdr_dt, count=1)
```

Security: `np.load(..., allow_pickle=True)` can execute code from untrusted files. Keep it `False`.

### 36.3 Endianness

```python
be = np.array([1, 256], dtype='>i4')       # big-endian
be.dtype.byteorder                          # '>'
le = be.astype('<i4')                       # convert to little-endian
be.byteswap()                               # swap bytes of the data (does not change dtype tag)
be.view(be.dtype.newbyteorder())            # reinterpret after byteswap
```

### 36.4 Memory management

```python
import sys, tracemalloc

a = np.zeros((1000, 1000))
a.nbytes                                    # 8,000,000
sys.getsizeof(a)                            # includes small header overhead
a32 = a.astype(np.float32)                  # half the memory
a16 = a.astype(np.float16)                  # quarter (low precision)

tracemalloc.start()
b = np.random.rand(2000, 2000)
cur, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

# Avoid temporaries
tmp = np.empty_like(a)
np.multiply(a, 2, out=tmp)                  # no new allocation
a *= 2                                      # in place
# Instead of: y = (a * 2 + 3) ** 2    (3 temporaries)
np.multiply(a, 2, out=tmp); tmp += 3; np.square(tmp, out=tmp)

# Release memory
del a; import gc; gc.collect()
```

Rules of thumb: pick the smallest safe dtype (`uint8` images, `float32` ML), process in chunks, use views, delete big intermediates.

### 36.5 Performance: measure first

```python
import timeit
timeit.timeit(lambda: a.sum(), number=100)          # quick check
# Jupyter: %timeit a.sum()
# Profiling: python -m cProfile -s cumtime script.py   or   line_profiler (@profile)
```

Memory order matters:

```python
A = np.random.rand(5000, 5000)
%timeit A.sum(axis=1)       # reads contiguous rows (fast)
%timeit A.sum(axis=0)       # strided access (often slower)
%timeit np.ascontiguousarray(A.T).sum(axis=1)
```

Speed checklist (beyond Section 24):

| Technique | Example |
|---|---|
| Use `bincount` / `searchsorted` / `unique` instead of loops | group sums, binning |
| Prefer `np.count_nonzero(mask)` to `mask.sum()` | slightly faster |
| `np.fromiter` for generator input | avoids list intermediate |
| Contiguous inputs before heavy ops | `np.ascontiguousarray` |
| Control BLAS threads | `OMP_NUM_THREADS=4` or `threadpoolctl` |
| Chunk big broadcasts | loop over slices of the large axis |
| `np.einsum(..., optimize=True)` / `np.einsum_path` | multi-operand contractions |
| Fuse expressions | `numexpr.evaluate("a*b + c")` |
| JIT hot loops | `numba.njit` |

```python
# Numba for loops that cannot be vectorized
from numba import njit

@njit
def ema(x, alpha):
    out = np.empty_like(x)
    out[0] = x[0]
    for i in range(1, len(x)):
        out[i] = alpha * x[i] + (1 - alpha) * out[i - 1]
    return out

# Limit BLAS threads for reproducible timings
from threadpoolctl import threadpool_limits
with threadpool_limits(limits=1):
    C = A @ A
```

### 36.6 Interoperability

```python
import pandas as pd, torch

df = pd.DataFrame(arr, columns=['a', 'b', 'c'])
df.to_numpy()                       # DataFrame -> ndarray (may copy)

t = torch.from_numpy(arr)           # SHARES memory with arr
n = t.numpy()                       # back, also shared (CPU tensors)
np.from_dlpack(t)                   # zero-copy exchange via DLPack

# Many libraries accept ndarrays directly: Matplotlib, scikit-learn, OpenCV, SciPy.
# CuPy / JAX / Dask mirror the NumPy API: code written with np.* often ports with a swap.
```

### 36.7 Testing numerical code

```python
np.testing.assert_allclose(actual, desired, rtol=1e-7, atol=1e-12)
np.testing.assert_array_equal(a, b)
np.testing.assert_almost_equal(0.1 + 0.2, 0.3, decimal=7)
np.testing.assert_array_less(a, b)

# Property tests: shapes, invariants, round trips
assert np.allclose(np.fft.ifft(np.fft.fft(x)).real, x)
```

Numerical gradient check (use it to debug any hand-written backprop; see Section 37.5):

```python
def numerical_grad(f, x, eps=1e-6):
    g = np.zeros_like(x)
    it = np.nditer(x, flags=['multi_index'])
    for _ in it:
        i = it.multi_index; old = x[i]
        x[i] = old + eps; fp = f()
        x[i] = old - eps; fm = f()
        x[i] = old
        g[i] = (fp - fm) / (2 * eps)
    return g
# relative error ||g_num - g_ana|| / (||g_num|| + ||g_ana||) should be below about 1e-6
```

### 36.8 Dispatch protocols (how NumPy-compatible libraries plug in)

- `__array__` / `__array_interface__`: let other objects convert to ndarray.
- `__array_ufunc__`: custom behavior when a ufunc (`np.add`, `np.sin`) is called on your class.
- `__array_function__`: custom behavior for high-level functions (`np.concatenate`, `np.mean`), used by CuPy, Dask, and others.

Subclass minimally (`class MyArr(np.ndarray)`) only when you really need it; wrapping is usually simpler.

### Checkpoint 7

1. How do you process a 50 GB `.npy` file on a laptop? *(`mmap_mode='r'` plus chunked loops.)*
2. How do you fill NaNs by interpolation? *(`np.interp` over indices of valid values.)*
3. Does `torch.from_numpy(a)` copy? *(No, it shares memory.)*
4. How do you check a hand-written gradient? *(Compare against central finite differences.)*

---

## 37. Phase 8 Deep Dive: Data Science and ML Applications

All code below uses only NumPy. `softmax` is the stable version from Section 25.2.

### 37.1 Exploratory analysis with NumPy

```python
rng = np.random.default_rng(0)
X = rng.normal(size=(500, 4)) * [1, 5, 0.1, 10] + [0, 20, 3, -5]
X[rng.random(X.shape) < 0.02] = np.nan                    # inject missing values

print("shape:", X.shape)
print("missing per col:", np.isnan(X).sum(0))
print("mean:", np.nanmean(X, 0).round(2))
print("std :", np.nanstd(X, 0).round(2))
print("q   :", np.nanpercentile(X, [0, 25, 50, 75, 100], axis=0).round(2))

Xc = X[~np.isnan(X).any(1)]
corr = np.corrcoef(Xc, rowvar=False)                       # feature correlations
z = (Xc - Xc.mean(0)) / Xc.std(0)
outlier_rows = np.flatnonzero((np.abs(z) > 3).any(1))
```

### 37.2 Feature engineering and the fit/transform pattern

```python
class StandardScaler:
    def fit(self, X):
        self.mean_ = X.mean(0)
        self.std_ = X.std(0); self.std_[self.std_ == 0] = 1
        return self
    def transform(self, X): return (X - self.mean_) / self.std_
    def fit_transform(self, X): return self.fit(X).transform(X)

class MinMaxScaler:
    def fit(self, X):
        self.min_, self.rng_ = X.min(0), np.ptp(X, axis=0); self.rng_[self.rng_ == 0] = 1
        return self
    def transform(self, X): return (X - self.min_) / self.rng_

class RobustScaler:                      # resistant to outliers
    def fit(self, X):
        self.med_ = np.median(X, 0)
        q1, q3 = np.percentile(X, [25, 75], axis=0)
        self.iqr_ = q3 - q1; self.iqr_[self.iqr_ == 0] = 1
        return self
    def transform(self, X): return (X - self.med_) / self.iqr_

# Fit on TRAIN only, apply to val/test (avoids data leakage)
sc = StandardScaler().fit(X_train)
X_train_s, X_test_s = sc.transform(X_train), sc.transform(X_test)
```

Other transforms:

```python
np.log1p(x)                                       # tame right-skewed positives
np.digitize(x, np.percentile(x, [25, 50, 75]))    # quantile bins -> categories
np.eye(k)[labels]                                 # one-hot

from itertools import combinations_with_replacement
def poly_features(X, degree=2):
    cols = [np.ones(len(X))]
    for d in range(1, degree + 1):
        for combo in combinations_with_replacement(range(X.shape[1]), d):
            cols.append(np.prod(X[:, combo], axis=1))
    return np.column_stack(cols)
```

### 37.3 Splitting and cross-validation

```python
def train_val_test_split(X, y, val=0.15, test=0.15, seed=0):
    rng = np.random.default_rng(seed)
    idx = rng.permutation(len(X))
    n_test, n_val = int(len(X) * test), int(len(X) * val)
    te, va, tr = idx[:n_test], idx[n_test:n_test + n_val], idx[n_test + n_val:]
    return (X[tr], y[tr]), (X[va], y[va]), (X[te], y[te])

def kfold_indices(n, k, seed=0):
    folds = np.array_split(np.random.default_rng(seed).permutation(n), k)
    for i in range(k):
        tr = np.concatenate([folds[j] for j in range(k) if j != i])
        yield tr, folds[i]

def stratified_split(y, test=0.2, seed=0):
    rng = np.random.default_rng(seed)
    te = []
    for c in np.unique(y):
        ids = rng.permutation(np.flatnonzero(y == c))
        te.append(ids[:int(len(ids) * test)])
    te = np.concatenate(te)
    tr = np.setdiff1d(np.arange(len(y)), te)
    return tr, te
```

### 37.4 Classic models from scratch

**Ridge regression**

```python
def fit_ridge(X, y, lam=1.0):
    Xb = np.c_[np.ones(len(X)), X]
    reg = lam * np.eye(Xb.shape[1]); reg[0, 0] = 0          # do not penalize the bias
    return np.linalg.solve(Xb.T @ Xb + reg, Xb.T @ y)
```

**Softmax (multiclass logistic) regression**

```python
def fit_softmax(X, y, n_classes, lr=0.5, epochs=500, l2=0.0):
    n, d = X.shape
    W, b = np.zeros((d, n_classes)), np.zeros(n_classes)
    Y = np.eye(n_classes)[y]
    for _ in range(epochs):
        G = (softmax(X @ W + b) - Y) / n
        W -= lr * (X.T @ G + l2 * W)
        b -= lr * G.sum(0)
    return W, b

predict = lambda X, W, b: (X @ W + b).argmax(1)
```

**k-Nearest Neighbors**

```python
def knn_predict(Xtr, ytr, Xte, k=5):
    d = ((Xte[:, None, :] - Xtr[None, :, :]) ** 2).sum(-1)       # (n_test, n_train)
    idx = np.argpartition(d, k - 1, axis=1)[:, :k]
    return np.array([np.bincount(r).argmax() for r in ytr[idx]])
```

**Gaussian Naive Bayes**

```python
class GaussianNB:
    def fit(self, X, y):
        self.classes_ = np.unique(y)
        self.mu_ = np.array([X[y == c].mean(0) for c in self.classes_])
        self.var_ = np.array([X[y == c].var(0) for c in self.classes_]) + 1e-9
        self.prior_ = np.array([(y == c).mean() for c in self.classes_])
        return self
    def predict(self, X):
        ll = -0.5 * (np.log(2 * np.pi * self.var_)[None]
                     + (X[:, None, :] - self.mu_[None]) ** 2 / self.var_[None]).sum(-1)
        return self.classes_[(ll + np.log(self.prior_)).argmax(1)]
```

**PCA via SVD**

```python
Xc = X - X.mean(0)
U, s, Vt = np.linalg.svd(Xc, full_matrices=False)
Z = Xc @ Vt[:2].T                     # 2D projection
explained = s ** 2 / (s ** 2).sum()   # explained variance ratio
X_back = Z @ Vt[:2] + X.mean(0)       # reconstruction from 2 components
```

K-means is in Section 26.4, linear and logistic regression in 26.1 to 26.3.

### 37.5 A trainable neural network (MLP + dropout + Adam)

Activations and derivatives:

| Name | f(z) | f'(z) |
|---|---|---|
| ReLU | `np.maximum(0, z)` | `(z > 0)` |
| Leaky ReLU | `np.where(z > 0, z, .01*z)` | `np.where(z > 0, 1, .01)` |
| Sigmoid | `1/(1+np.exp(-z))` | `s*(1-s)` |
| Tanh | `np.tanh(z)` | `1 - np.tanh(z)**2` |
| Softplus | `np.log1p(np.exp(z))` | `sigmoid(z)` |

```python
class MLP:
    def __init__(self, sizes, dropout=0.0, seed=0):
        self.rng = np.random.default_rng(seed)
        self.W = [self.rng.normal(0, np.sqrt(2 / i), (i, o)) for i, o in zip(sizes[:-1], sizes[1:])]
        self.b = [np.zeros(o) for o in sizes[1:]]
        self.dropout = dropout

    def forward(self, X, train=False):
        acts, self.masks = [X], []
        for l, (W, b) in enumerate(zip(self.W, self.b)):
            z = acts[-1] @ W + b
            if l < len(self.W) - 1:
                a = np.maximum(0, z)
                m = None
                if train and self.dropout > 0:
                    m = (self.rng.random(a.shape) > self.dropout) / (1 - self.dropout)
                    a = a * m
                self.masks.append(m)
                acts.append(a)
            else:
                acts.append(softmax(z))
        return acts

    def backward(self, acts, Y):
        n = len(Y)
        gW, gb = [None] * len(self.W), [None] * len(self.b)
        d = (acts[-1] - Y) / n                          # softmax + cross-entropy gradient
        for l in reversed(range(len(self.W))):
            gW[l], gb[l] = acts[l].T @ d, d.sum(0)
            if l > 0:
                d = d @ self.W[l].T
                if self.masks[l - 1] is not None:
                    d = d * self.masks[l - 1]
                d = d * (acts[l] > 0)
        return gW, gb

class Adam:
    def __init__(self, params, lr=1e-2, b1=0.9, b2=0.999, eps=1e-8):
        self.p, self.lr, self.b1, self.b2, self.eps, self.t = params, lr, b1, b2, eps, 0
        self.m = [np.zeros_like(p) for p in params]
        self.v = [np.zeros_like(p) for p in params]
    def step(self, grads):
        self.t += 1
        for p, g, m, v in zip(self.p, grads, self.m, self.v):
            m *= self.b1; m += (1 - self.b1) * g
            v *= self.b2; v += (1 - self.b2) * g * g
            p -= self.lr * (m / (1 - self.b1 ** self.t)) / (np.sqrt(v / (1 - self.b2 ** self.t)) + self.eps)

def make_spirals(n=200, noise=0.02, seed=0):
    rng = np.random.default_rng(seed)
    t = np.linspace(0, 4 * np.pi, n); r = t / (4 * np.pi)
    s1 = np.c_[r * np.cos(t), r * np.sin(t)]
    s2 = np.c_[r * np.cos(t + np.pi), r * np.sin(t + np.pi)]
    X = np.vstack([s1, s2]) + rng.normal(0, noise, (2 * n, 2))
    return X, np.r_[np.zeros(n, int), np.ones(n, int)]

X, y = make_spirals(); Y = np.eye(2)[y]
net = MLP([2, 64, 64, 2], dropout=0.0)
opt = Adam(net.W + net.b, lr=0.01)         # same array objects -> updates modify the network
for epoch in range(2000):
    acts = net.forward(X, train=True)
    gW, gb = net.backward(acts, Y)
    opt.step(gW + gb)
loss = -np.mean(np.log(net.forward(X)[-1][np.arange(len(y)), y] + 1e-12))
acc = (net.forward(X)[-1].argmax(1) == y).mean()
```

Verify the backward pass with the numerical gradient from Section 36.7:

```python
f = lambda: -np.mean(np.log(net.forward(X)[-1][np.arange(len(y)), y] + 1e-12))
acts = net.forward(X); gW, gb = net.backward(acts, Y)
g_num = numerical_grad(f, net.W[0])
rel = np.linalg.norm(g_num - gW[0]) / (np.linalg.norm(g_num) + np.linalg.norm(gW[0]))
```

### 37.6 Metrics beyond accuracy

```python
def confusion(y_true, y_pred, k):
    C = np.zeros((k, k), int); np.add.at(C, (y_true, y_pred), 1); return C

C = confusion(y_true, y_pred, k)
precision = np.diag(C) / np.maximum(C.sum(0), 1)
recall    = np.diag(C) / np.maximum(C.sum(1), 1)
f1        = 2 * precision * recall / np.maximum(precision + recall, 1e-12)

def roc_auc(y, score):                       # rank-based AUC (ignores tie handling)
    order = np.argsort(score)
    ranks = np.empty(len(score)); ranks[order] = np.arange(1, len(score) + 1)
    n1 = y.sum(); n0 = len(y) - n1
    return (ranks[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0)

rmse = np.sqrt(np.mean((y - y_hat) ** 2))
mae = np.mean(np.abs(y - y_hat))
```

### 37.7 Time series

```python
from numpy.lib.stride_tricks import sliding_window_view

def rolling_mean(x, k): return sliding_window_view(x, k).mean(axis=1)
def rolling_std(x, k):  return sliding_window_view(x, k).std(axis=1)

def ema(x, alpha):                           # recursive, so a loop (or Numba) is natural
    out = np.empty(len(x)); out[0] = x[0]
    for i in range(1, len(x)):
        out[i] = alpha * x[i] + (1 - alpha) * out[i - 1]
    return out

def acf(x, nlags):                           # autocorrelation
    x = x - x.mean(); denom = x @ x
    return np.array([x[:len(x) - k] @ x[k:] / denom for k in range(nlags + 1)])

d1 = np.diff(x)                              # differencing for stationarity
lags = np.c_[x[2:], x[1:-1], x[:-2]]         # lag features: [x_t, x_{t-1}, x_{t-2}]
# Supervised framing: predict x[3:] from windows
W = sliding_window_view(x, 3)[:-1]; target = x[3:]
```

### 37.8 Text features (bag of words and TF-IDF)

```python
docs = ["the cat sat", "the dog sat", "the cat ran"]
vocab = sorted({w for d in docs for w in d.split()})
w2i = {w: i for i, w in enumerate(vocab)}

tf = np.zeros((len(docs), len(vocab)))
for i, d in enumerate(docs):
    for w in d.split():
        tf[i, w2i[w]] += 1

df = (tf > 0).sum(0)
idf = np.log((1 + len(docs)) / (1 + df)) + 1
tfidf = tf * idf
tfidf /= np.linalg.norm(tfidf, axis=1, keepdims=True)
sim = tfidf @ tfidf.T                        # cosine similarity between documents
```

### 37.9 Images as arrays

```python
img = np.random.randint(0, 256, (64, 64), dtype=np.uint8)

def maxpool2(a):                             # 2x2 max pooling via reshape trick
    H, W = (a.shape[0] // 2) * 2, (a.shape[1] // 2) * 2
    return a[:H, :W].reshape(H // 2, 2, W // 2, 2).max(axis=(1, 3))

def equalize(a):                             # histogram equalization (uint8 grayscale)
    hist = np.bincount(a.ravel(), minlength=256)
    cdf = hist.cumsum(); cdf_min = cdf[cdf > 0][0]
    lut = np.round((cdf - cdf_min) / (cdf[-1] - cdf_min) * 255).clip(0, 255).astype(np.uint8)
    return lut[a]

def conv2d(a, k):                            # valid convolution (cross-correlation) via im2col
    kh, kw = k.shape
    patches = sliding_window_view(a, (kh, kw))        # (H-kh+1, W-kw+1, kh, kw)
    return np.einsum('ijkl,kl->ij', patches, k)

blur = conv2d(img.astype(float), np.ones((3, 3)) / 9)
edges = conv2d(img.astype(float), np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]]))
```

### 37.10 Monte Carlo and simulation

```python
rng = np.random.default_rng(1)

# Option-pricing style Monte Carlo (geometric Brownian motion)
S0, mu, sigma, T, steps, paths = 100, 0.05, 0.2, 1.0, 252, 10_000
dt = T / steps
Z = rng.standard_normal((paths, steps))
S = S0 * np.exp(np.cumsum((mu - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * Z, axis=1))
payoff = np.maximum(S[:, -1] - 100, 0)
price = np.exp(-mu * T) * payoff.mean()

# Particle simulation: vectorized update of all particles at once
pos = rng.random((1000, 2)); vel = rng.normal(0, 0.1, (1000, 2))
for _ in range(100):
    pos += vel * 0.01
    hit = (pos < 0) | (pos > 1)
    vel[hit] *= -1                           # bounce off walls
    pos = np.clip(pos, 0, 1)
```

### 37.11 Bridge to scikit-learn and PyTorch

```python
# scikit-learn: same shapes your NumPy code already uses: X (n_samples, n_features), y (n_samples,)
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(max_iter=1000).fit(X_train, y_train)
clf.predict(X_test)

# PyTorch: tensors share memory with arrays
import torch
Xt = torch.from_numpy(X.astype(np.float32))
yt = torch.from_numpy(y.astype(np.int64))
```

Your from-scratch implementations are the best way to understand what these libraries do. Compare your NumPy results against them to confirm correctness (`np.testing.assert_allclose`).

### 37.12 End-to-end project checklist

1. **Load** data (`loadtxt` / `genfromtxt` / Pandas to `to_numpy()`), check `shape` and `dtype`.
2. **Clean**: NaN handling, outliers, type fixes.
3. **Explore**: summary stats, correlations, class balance (`bincount`).
4. **Split** train/val/test (or k-fold), fixed seed.
5. **Engineer features** with fit/transform scalers, fit on train only.
6. **Baseline** (mean predictor, majority class), then a model.
7. **Train** with vectorized code, track loss each epoch.
8. **Evaluate** on validation: accuracy, precision/recall/F1, RMSE, AUC as relevant.
9. **Debug** with gradient checks and shape asserts.
10. **Report** final test metrics once; save arrays with `np.savez_compressed`.

Suggested portfolio projects: linear/logistic regression from scratch, k-means image color quantization, PCA on a face or digit dataset, a NumPy MLP on spirals or MNIST, Monte Carlo option pricing, a small physics or particle simulation, TF-IDF document search.

### Checkpoint 8

1. Why fit a scaler only on training data? *(Prevents test information leaking into training.)*
2. How can a pooling layer be written with only `reshape` and `max`? *(Reshape to `(H/2, 2, W/2, 2)`, take max over axes 1 and 3.)*
3. How can you confirm backprop is correct? *(Compare to finite-difference gradients; relative error below about 1e-6.)*
4. What is the shape contract for most ML libraries? *(`X: (n_samples, n_features)`, `y: (n_samples,)`.)*


---

## 38. String and Character Arrays

NumPy arrays are not only numeric. Text arrays use the same indexing, slicing, broadcasting, and sorting you already know. Typical uses: labels, class names, categorical columns, tokens, and "puzzle" arrays of letters.

### 38.1 Creating string arrays and the `<U` dtype

```python
names = np.array(["hello", "numpy", "array"])
names.dtype                    # <U5   -> Unicode, max 5 characters per element
names.itemsize                 # 20    -> 5 chars * 4 bytes (UTF-32)

np.array("A")                  # 0-d string array: shape (), ndim 0, dtype <U1
np.array(["A", "B", "C"])      # 1D
np.array([["A", "B"], ["C", "D"]])      # 2D, dtype <U1
```

The width is fixed by the **longest** string at creation. Assigning something longer **truncates silently**:

```python
a = np.array(["cat", "dog"])             # <U3
a[0] = "elephant"
a                                        # ['ele' 'dog']   <- truncated!
np.array(["abcdef"], dtype="U3")         # ['abc']
a = a.astype("U10")                      # widen first, then assign
```

Elements you pull out are `np.str_` (a subclass of Python `str`), so `+` on two elements concatenates:

```python
x = np.array(["A", "B", "C"])
x[1] + x[0]                              # 'BA'
type(x[1])                               # numpy.str_
```

### 38.2 Vectorized string functions: `np.strings` (NumPy 2.x)

`np.strings` applies string operations to every element at once (the older `np.char` still works and is the only place with `split`).

```python
s = np.array(["hello world", "numpy", "Array"])

np.strings.upper(s); np.strings.lower(s); np.strings.title(s)
np.strings.capitalize(s); np.strings.swapcase(s)
np.strings.str_len(s)                       # [11  5  5]
np.strings.add(s, "!")                      # concatenation; in NumPy 2.x s + "!" also works
np.strings.multiply("ab", 3)                # 'ababab'
np.strings.replace(s, "o", "0")
np.strings.find(s, "o")                     # index or -1
np.strings.count(s, "a")
np.strings.startswith(s, "n"); np.strings.endswith(s, "y")
np.strings.strip(np.array(["  hi  "]))      # also lstrip, rstrip
np.strings.center(np.array(["ab"]), 6, "*") # ['**ab**']  (ljust, rjust too)
np.strings.zfill(np.array(["7", "42"]), 4)  # ['0007' '0042']
np.strings.partition(np.array(["a=b"]), "=")   # three arrays: before, sep, after
np.strings.isalpha(s); np.strings.isdigit(s); np.strings.isupper(s)

np.char.split(np.array(["a b c"]))          # object array of lists (no np.strings.split)
np.char.add(["a", "b"], ["c", "d"])         # works in all NumPy versions
```

In NumPy 1.x, use `np.char.*` for all of these (and `np.char.add` instead of `+`).

### 38.3 Comparing, sorting, searching text

```python
w = np.array(["pear", "Apple", "apple", "fig"])

w == "fig"                       # [False False False  True]
np.sort(w)                       # ['Apple' 'apple' 'fig' 'pear']   (uppercase sorts first)
np.sort(np.strings.lower(w))     # case-insensitive order
w[np.argsort(np.strings.str_len(w))]       # sort by length
np.isin(w, ["fig", "pear"])      # membership mask
w[np.strings.startswith(w, "a")] # boolean filtering works as usual
```

Word frequency (bag of words) with `unique`:

```python
words = np.array("the cat and the dog and the bird".split())
vals, counts = np.unique(words, return_counts=True)
vals[counts.argmax()]                      # 'the'
vals[np.argsort(-counts)][:3]              # top 3 words
```

### 38.4 Converting between text and numbers

```python
np.array([1.5, 2]).astype(str)             # ['1.5' '2.0']
np.array(["1", "2", "3"]).astype(int)      # [1 2 3]
np.array(["1.5", "2"]).astype(float)       # [1.5 2. ]
"".join(np.array(["h", "i"]))              # 'hi'  (join letters back into one string)
arr.tolist()                               # back to Python lists
```

### 38.5 Character codes and vectorized ciphers

A `U1` array can be viewed as its Unicode code points, so character math is just integer math:

```python
text = np.array(list("hello"))
codes = text.view(np.uint32)               # [104 101 108 108 111]
shifted = (codes.astype(np.int64) - 97 + 3) % 26 + 97       # Caesar shift by 3
"".join(shifted.astype(np.uint32).view("U1"))               # 'khoor'

np.frombuffer("hello".encode(), dtype=np.uint8)             # bytes: [104 101 108 108 111]
```

### 38.6 Picking letters out of an N-d array (coordinate indexing)

Instead of adding many `array[i, j, k]` terms by hand, store the coordinates and index once with fancy indexing:

```python
grid = np.array([
    [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]],
    [["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R"]],
    [["S", "T", "U"], ["V", "W", "X"], ["Y", "Z", " "]],
])
coords = np.array([(1, 2, 0), (1, 2, 2), (0, 2, 2)])        # (n, 3) list of (i, j, k)
letters = grid[tuple(coords.T)]            # same as grid[coords[:,0], coords[:,1], coords[:,2]]
"".join(letters)                           # 'PRI'
```

### 38.7 `StringDType`: variable-length strings (NumPy 2.x)

```python
sd = np.array(["a", "a much longer string"], dtype=np.dtypes.StringDType())
sd.dtype                                   # StringDType()   no truncation, no fixed width

sd = np.array(["x", None, "z"], dtype=np.dtypes.StringDType(na_object=None))   # missing values
```

Use `StringDType` when strings vary a lot in length or you need a missing-value marker. Use `<U` for small fixed vocabularies. For heavy text analysis or many text columns, move to **Pandas** (`str` accessor) or dedicated NLP libraries.

### Checkpoint 38

1. What is the dtype of `np.array(["a", "bcd"])`, and why? *(`<U3`; width of the longest string.)*
2. What happens if you assign `"hello"` into a `<U3` array? *(Silently truncated to `'hel'`; widen with `astype('U10')` first.)*
3. Which function counts words in a string array? *(`np.unique(..., return_counts=True)`.)*
4. How do you read the first letter of every string at once? *(`np.strings.slice` in newer NumPy, or `arr.astype('U1')`, which truncates to one character.)*


---

## 39. Cheat Sheet

### Create
```
np.array  zeros  ones  full  empty  eye  diag  arange  linspace  logspace
meshgrid  random.default_rng  *_like  fromfunction  tile  repeat
```

### Inspect
```
.shape  .ndim  .size  .dtype  .itemsize  .nbytes  .strides  .T  .flags  .base
```

### Index
```
a[i]  a[i:j:k]  a[i, j]  a[..., 0]  a[:, None]  a[mask]  a[[i, j]]  np.ix_  np.take
np.where  np.nonzero  np.argwhere  np.unravel_index
```

### Shape
```
reshape  ravel  flatten  T  transpose  swapaxes  moveaxis  expand_dims  squeeze
concatenate  stack  vstack  hstack  dstack  split  array_split  pad  flip  roll
```

### Math
```
+ - * / // % **   sqrt exp log sin cos tan abs sign floor ceil round clip
maximum minimum  isnan isinf isclose allclose  add.reduce  add.accumulate  add.at
```

### Stats
```
sum mean median std var min max argmin argmax prod cumsum cumprod diff
percentile quantile corrcoef cov histogram bincount digitize unique
(axis=, keepdims=, nan* variants)
```

### Linear algebra
```
@  matmul  dot  outer  inner  cross  einsum  tensordot  kron
linalg: inv pinv solve lstsq det eig eigh svd qr cholesky norm matrix_rank cond
```

### Sort / search / sets
```
sort argsort lexsort partition argpartition searchsorted
unique intersect1d union1d setdiff1d isin
```

### Random (Generator)
```
rng = np.random.default_rng(seed)
rng.random  rng.integers  rng.normal  rng.uniform  rng.choice  rng.permutation
rng.shuffle  rng.binomial  rng.poisson  rng.multivariate_normal
```

### I/O
```
save load savez savez_compressed savetxt loadtxt genfromtxt tofile fromfile memmap
```

### Added in the deep dives
```
take_along_axis put_along_axis compress ndindex nditer r_ c_ apply_along_axis
argpartition lexsort digitize searchsorted bincount(weights=) maximum.at
errstate seterr logical_and/or/xor bitwise ops fmod divmod
Generator(PCG64) bit_generator.state spawn  dirichlet multinomial lognormal
linalg: eigvalsh vector_norm matrix_norm LinAlgError  svd low-rank  ridge closed form
nanmean nanmedian ma.masked_invalid interp(NaN fill) memmap open_memmap threadpoolctl
np.testing.assert_allclose  numerical gradient check
strings: <U dtype (truncates!)  np.strings.upper/replace/find/str_len/add  StringDType  np.unique(return_counts)
```

### Golden rules
1. Think in **shapes**; print `.shape` constantly.
2. **Vectorize**; no Python loops over elements.
3. Know **view vs copy**.
4. Master **broadcasting** and **axis**.
5. Use `keepdims=True` to avoid shape bugs.
6. Use `@`, `solve`, `lstsq`, not `inv`.
7. Use `default_rng(seed)` for reproducibility.
8. Pick dtypes deliberately (watch overflow, `float32` vs `float64`).

---

### Recommended next steps

- Practice: *100 NumPy exercises* (rougier/numpy-100 on GitHub).
- Official docs: https://numpy.org/doc/stable/ (User Guide and API reference).
- Implement from scratch: linear regression, k-NN, k-means, PCA, a small MLP, then move on to PyTorch (its tensor API mirrors NumPy).
- Companion libraries: **Pandas** (tabular), **Matplotlib** (plotting), **SciPy** (scientific algorithms), **Numba** (JIT speedups).

---

## Appendix A: Review of My Practice Scripts (`numpy/` folder)

This appendix analyzes the 14 scripts in `numpy.zip`: what each one covers, where it sits in the roadmap, what is missing, corrections to a few details, and the next scripts to write. All 14 scripts run without errors on NumPy 2.5.

### A.1 Inventory: script to guide section

| Script | What it practices | Guide section |
|---|---|---|
| `single-dim-arr.py` | 1D vs 2D arrays, `ndim`, scalar multiply, `type()` | 3, 6 |
| `zero-dim-arr.py` | 0-d array (a string), `ndim` | 30.4, 38 |
| `multi-dim-arr.py` | 3D string array, `ndim`, `shape` | 3, 6 |
| `multi-dim-indexing.py` | indexing a 3D array with `[i, j, k]` | 7, 38.6 |
| `slicing.py` | `start:stop:step`, rows, columns, negative index, reverse | 7 |
| `filtering.py` | boolean masks, `&`, `np.where` | 8, 16 |
| `comp-operator.py` | `==`, `>=`, `<` produce boolean arrays | 12.1 |
| `arthimetic-scalar.py` | array and scalar arithmetic | 12.1 |
| `element-wise-arthimetic.py` | array and array arithmetic | 12.1 |
| `arthimetic-vectorized-math-func.py` | `sqrt`, `round`, `floor`, `ceil`, `pi` | 12.2 |
| `broadcasting.py` | `(1, n) * (n, 1)` outer table | 13 |
| `aggregate-function.py` | `sum`, `mean`, `std`, `var`, `min`, `max`, `argmin`, `argmax`, `axis` | 14 |
| `rand-num.py` | `rng.integers`, `np.random.randint`, `np.random.rand` | 18 |
| `uniform_rng.py` | seeded `default_rng(...).uniform()` | 18 |

### A.2 Progress by roadmap phase

| Phase | Status | Covered by your scripts | Still to practice |
|---|---|---|---|
| 1 Foundations | Partial | `ndim`/`shape` for 0D to 3D, scalar math | `dtype`, `size`, list vs array speed, `shape` vs `size` |
| 2 Creating/inspecting | Barely started | `np.array(...)` only | `zeros`, `ones`, `full`, `arange`, `linspace`, `eye`, `dtype`, `astype`, attributes |
| 3 Indexing/manipulation | Mostly done | slicing, 3D indexing, boolean filtering | assignment, fancy indexing, `reshape`, `flatten`, transpose, `newaxis`, views vs copies |
| 4 Operations/broadcasting | Mostly done | scalar and element-wise math, ufuncs, comparison, aggregates, broadcasting | `keepdims`, `cumsum`, `clip`, `abs`/`exp`/`log`, `\|` and `~`, a broadcasting **error** case |
| 5 Array processing | Not started | (`np.where` only) | `concatenate`, `stack`, `split`, `sort`, `argsort`, `unique`, `searchsorted` |
| 6 Random + linear algebra | Partial | `integers`, `randint`, `rand`, `uniform` | `normal`, `choice`, `shuffle`, `permutation`, reproducible seeds, **all** of linear algebra |
| 7 Advanced | Not started | none | NaN handling, files, views/strides, performance, einsum |
| 8 Data science/ML | Not started | none | scaling, regression, k-means, PCA, a small network |

You have solid Phase 3 and Phase 4 basics. The biggest holes are Phase 2 (creation and dtype), Phase 5, and everything from linear algebra onward.

### A.3 Review notes with fixes

**1. `filtering.py`: the "teenagers" group includes children.**
`ages[ages < 21]` returns `[11 15 9 12 18]`, so 9, 11, and 12 are labeled teenagers, and age 20 falls in no group. Define explicit ranges, or label everything in one pass with `np.select`:

```python
children = ages[ages < 13]
teenagers = ages[(ages >= 13) & (ages <= 19)]      # [15 18]
adults = ages[(ages >= 20) & (ages <= 45)]         # [21 37 45 36 25]
seniors = ages[ages > 45]                          # [58 99]

labels = np.select([ages < 13, ages < 20, ages <= 45],
                   ["child", "teen", "adult"], default="senior")   # same shape as ages
```

Also, boolean indexing on a 2D array **flattens** the result to 1D. Use `np.where(mask, ages, 0)` (or `labels` above) to keep the shape. The variable name `sigma` usually means standard deviation; `only_18` would be clearer.

**2. `rand-num.py`: the upper bound is exclusive, and the labels mislead.**

```python
rng = np.random.default_rng()
rng.integers(low=1, high=6)                  # returns 1..5, never 6
rng.integers(low=1, high=6, endpoint=True)   # 1..6 (a real dice roll)
rng.integers(low=1, high=7)                  # also 1..6
```

`np.random.randint(1, 100, size=(5, 1))` gives values from 1 to **99**. The print label says "this is the random number generator" but prints a number, not the generator. The comment on seeds is right, but no seed is passed, so results differ on every run. Also, the script mixes the legacy API (`np.random.randint`, `np.random.rand`) with the modern one. Pick one:

```python
rng = np.random.default_rng(seed=42)           # reproducible
dice = rng.integers(1, 6, endpoint=True)
numbers = rng.integers(1, 100, size=(5, 1))    # 1..99
floats = rng.random(5)                         # [0, 1)
```

**3. `uniform_rng.py`: the comment describes a different function.**
The comment explains `np.random.seed()`, but the code uses `np.random.default_rng(seed=1)`, which is a separate, newer API (`seed()` sets hidden global state; `default_rng(seed)` makes a local generator). The result is the same every run (`0.5118...`), which is the point of seeding. `uniform()` returns a value in `[0, 1)` by default; give it a range and size to make the example more useful:

```python
rng = np.random.default_rng(seed=1)
rng.uniform()                              # 0.5118216247002567 (always, with seed=1)
rng.uniform(low=10, high=20, size=3)       # three floats in [10, 20)
```

**4. `aggregate-function.py`: three details worth recording.**
- `np.argmax(array)` on a 2D array returns the **flattened** index (`9`), not the position `(1, 4)`. Convert with `np.unravel_index(array.argmax(), array.shape)`.
- `np.std` and `np.var` default to the **population** formula (`ddof=0`): `std = 2.872`. The sample version is `np.std(array, ddof=1)` = `3.028`.
- Add the per-axis versions, which you will use constantly:

```python
array.max(axis=1)                    # [ 5 10]   max of each row
array.mean(axis=0)                   # [3.5 4.5 5.5 6.5 7.5]   mean of each column
array.sum(axis=1, keepdims=True)     # shape (2, 1), keeps the axis for broadcasting
np.argmax(array, axis=1)             # [4 4]   column of the max in each row
np.cumsum(array, axis=1)             # running totals along each row
```

**5. `arthimetic-vectorized-math-func.py`: `round` is not "round half up".**
`np.round([1.2, 2.5, 3.7])` gives `[1. 2. 4.]`. The `2.5 -> 2` result is correct: NumPy rounds halves to the nearest **even** number (`0.5 -> 0`, `1.5 -> 2`, `2.5 -> 2`, `3.5 -> 4`). The comment "rounded to the nearest integer" is fine for most values, but add a note so `2.5 -> 2` does not look like a bug. The result stays `float`; use `.astype(int)` for integers.

**6. `broadcasting.py`: show the failure and the rules.**
The two examples are valid and produce a multiplication table. Add the error case so the rule sticks:

```python
a = np.array([1, 2, 3])        # shape (3,)
b = np.array([1, 2])           # shape (2,)
a + b                          # ValueError: operands could not be broadcast together (3,) (2,)

# Rule: compare shapes from the right; each pair must be equal or one must be 1.
# (1, 4) * (4, 1) -> (4, 4)   OK
# (3,)   + (2,)   -> error
# Fix by reshaping: a[:, None] + b[None, :]  -> shape (3, 2)
```

**7. `multi-dim-indexing.py`: replace 16 hand-typed terms with coordinates.**
Your version works (it prints the full message). A shorter and less error-prone version stores the coordinates in a list:

```python
coords = [(1, 2, 0), (1, 2, 2), (0, 2, 2), (2, 0, 0)]       # and so on
word = "".join(array[c] for c in coords)                    # one index per tuple
# or vectorized fancy indexing:
idx = np.array(coords).T
word = "".join(array[tuple(idx)])
```

See Section 38.6.

**8. `zero-dim-arr.py`: it only prints `0`.** Also show what makes a 0-d array different from a plain value:

```python
a = np.array("A")
a.ndim, a.shape, a.dtype       # (0, (), dtype('<U1'))
a.item()                       # 'A'  (plain Python str)
np.array(5).shape              # ()   numbers can be 0-d too
```

**9. File naming and layout.**
- `arthimetic` is a typo for `arithmetic` (it appears in two filenames).
- Hyphens in filenames (`multi-dim-arr.py`) mean the file cannot be imported (`import multi-dim-arr` is a syntax error). Use `snake_case` everywhere; you already used it once in `uniform_rng.py`.
- Group by phase so the folder mirrors the roadmap (see A.4).

**10. Comment style.**
Your formatter wraps long `print(...)` lines so the explanatory comment lands after the closing parenthesis, which is hard to read. Put the comment **above** the statement and keep the expected output in a short `# Output:` line, as you already do in some files:

```python
# sum of every element in the 2D array
print("Sum of all elements:", np.sum(array))
# Output: 55
```

### A.4 Suggested folder layout and script template

```
numpy/
  README.md                      # roadmap checklist, tick off each script
  phase1_foundations/
  phase2_creating_inspecting/
  phase3_indexing_manipulation/   <- move slicing.py, multi_dim_indexing.py, filtering.py here
  phase4_operations_broadcasting/ <- arithmetic_*.py, comparison_operators.py, broadcasting.py, aggregate_functions.py
  phase5_array_processing/
  phase6_random_linalg/           <- rand_num.py, uniform_rng.py
  phase7_advanced/
  phase8_ml_applications/
```

Template for every new script (concept, code, expected output, one "try it" exercise):

```python
"""Topic: <one line>.  Phase <n>.  Guide section <n>."""
import numpy as np

# 1. concept in one sentence
arr = np.array([1, 2, 3])

# 2. demonstrate
print("shape:", arr.shape, "dtype:", arr.dtype)
# Output: shape: (3,) dtype: int64

# 3. edge case or common mistake
# ...

# 4. try it: <one exercise for next time>
```

### A.5 Next scripts to write (in suggested order)

Names follow your one-concept-per-file style.

| Phase | Script | Goal | Guide § |
|---|---|---|---|
| 1 | `list_vs_array_speed.py` | time a list comprehension against an array operation | 1 |
| 1 | `array_attributes.py` | `shape`, `size`, `ndim`, `dtype`, `itemsize`, `nbytes` | 6 |
| 2 | `create_zeros_ones_full.py` | `zeros`, `ones`, `full`, `empty`, `*_like` | 4 |
| 2 | `create_arange_linspace.py` | `arange` vs `linspace`, float step trap | 4 |
| 2 | `create_identity_diag.py` | `eye`, `diag`, `tri`, `meshgrid` | 4 |
| 2 | `dtypes_astype.py` | `dtype`, `astype`, overflow in `uint8` | 5 |
| 3 | `assign_with_slices.py` | change values via slices and masks | 7 |
| 3 | `fancy_indexing.py` | index with lists, paired vs `np.ix_` | 8 |
| 3 | `reshape_flatten.py` | `reshape`, `-1`, `ravel`, `flatten` | 10 |
| 3 | `transpose_axes.py` | `.T`, `swapaxes`, `moveaxis` | 10 |
| 3 | `views_vs_copies.py` | slice changes the original, `.copy()` does not | 9 |
| 3 | `newaxis_expand_dims.py` | `None`, `expand_dims`, `squeeze` | 10 |
| 4 | `aggregate_axis_keepdims.py` | per-row, per-column, `keepdims` | 14 |
| 4 | `cumulative_ops.py` | `cumsum`, `cumprod`, `diff` | 14 |
| 4 | `math_exp_log_abs_clip.py` | `exp`, `log`, `abs`, `clip` | 12 |
| 4 | `logical_operators.py` | `&`, `\|`, `~`, `any`, `all` | 8, 33 |
| 4 | `broadcasting_error_and_fix.py` | the failing shape and its fix | 13 |
| 4 | `broadcasting_normalize.py` | subtract column means, divide by std | 13 |
| 5 | `concatenate_stack.py` | `concatenate`, `vstack`, `hstack`, `stack` | 11 |
| 5 | `split_array.py` | `split`, `array_split` | 11 |
| 5 | `sort_argsort.py` | `sort`, `argsort`, sort rows by a column | 15 |
| 5 | `unique_counts.py` | `unique` with `return_counts` | 15 |
| 5 | `searchsorted_digitize.py` | binning values | 34 |
| 5 | `filter_rows_2d.py` | keep rows where all/any condition holds | 34 |
| 6 | `random_normal_choice.py` | `normal`, `choice`, `shuffle`, `permutation` | 18 |
| 6 | `random_reproducible.py` | same seed gives same numbers | 18, 35 |
| 6 | `matmul_dot.py` | `@`, `dot`, `outer`, `*` vs `@` | 17 |
| 6 | `linalg_solve_inv.py` | `solve` vs `inv`, `det`, `norm` | 17 |
| 6 | `linalg_eig_svd.py` | `eigh`, `svd`, reconstruct the matrix | 17, 35 |
| 7 | `missing_nan.py` | `isnan`, `nanmean`, imputation | 19, 36 |
| 7 | `save_load_files.py` | `save`, `load`, `savetxt`, `loadtxt` | 21, 36 |
| 7 | `memory_strides.py` | `strides`, views, `nbytes` | 24, 36 |
| 7 | `vectorize_vs_loop.py` | benchmark a loop against vectorized code | 24, 25 |
| 7 | `einsum_basics.py` | matmul, trace, batched dot with `einsum` | 22 |
| 8 | `standardize_features.py` | z-score scaler class | 37 |
| 8 | `linear_regression_scratch.py` | normal equation and gradient descent | 26, 37 |
| 8 | `kmeans_scratch.py` | k-means with broadcasting | 26 |
| 8 | `pca_svd.py` | PCA via SVD | 26, 37 |
| 8 | `mlp_scratch.py` | forward and backward pass, Adam | 37 |

### A.6 Corrected versions of the scripts that had issues

`filtering.py` (fixed):

```python
import numpy as np

ages = np.array([[11, 21, 37, 58, 45, 99], [15, 36, 9, 12, 18, 25]])

children = ages[ages < 13]
teenagers = ages[(ages >= 13) & (ages <= 19)]
adults = ages[(ages >= 20) & (ages <= 45)]
seniors = ages[ages > 45]
even_ages = ages[ages % 2 == 0]
odd_ages = ages[ages % 2 != 0]

print("Original array:\n", ages)
print("Children:", children)        # [11  9 12]
print("Teenagers:", teenagers)      # [15 18]
print("Adults:", adults)            # [21 37 45 36 25]
print("Seniors:", seniors)          # [58 99]

# keep the shape: replace everything except 18 with 0
only_18 = np.where(ages == 18, ages, 0)
print(only_18)

# label every element in one pass (same shape as ages)
group = np.select([ages < 13, ages < 20, ages <= 45], ["child", "teen", "adult"], default="senior")
print(group)
```

`rand_num.py` and `uniform_rng.py` (combined and fixed):

```python
import numpy as np

rng = np.random.default_rng(seed=42)       # one modern generator, reproducible

print("Dice roll (1-6):", rng.integers(1, 6, endpoint=True))
print("Five integers in [1, 99]:\n", rng.integers(1, 100, size=(5, 1)))
print("Five floats in [0, 1):", rng.random(5))
print("Three floats in [10, 20):", rng.uniform(low=10, high=20, size=3))
```

`aggregate_functions.py` (additions to append):

```python
print("Position of max (row, col):", np.unravel_index(array.argmax(), array.shape))   # (1, 4)
print("Sample std (ddof=1):", np.std(array, ddof=1))        # 3.0277
print("Max of each row:", array.max(axis=1))                # [ 5 10]
print("Mean of each column:", array.mean(axis=0))           # [3.5 4.5 5.5 6.5 7.5]
print("Row sums, kept 2D:\n", array.sum(axis=1, keepdims=True))
```

### A.7 What was missing from the guide itself

Comparing your scripts to the guide, one real gap showed up: **string and character arrays** (your `zero-dim-arr.py`, `multi-dim-arr.py`, and `multi-dim-indexing.py` all use them). That is now **Section 38**. Everything else in your scripts was already covered; the rest of this appendix is the review and the plan for what to practice next.


---

*End of guide.*
