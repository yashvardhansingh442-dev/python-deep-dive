# Module 2, Phase A: Solving and Measuring

> **Part of:** SciPy Course, Module 2 (Linear Algebra, `scipy.linalg`)
> **Level:** Beginner to Advanced
> **Time:** about 2 to 3 days
> **Prerequisites:** Module 0 (NumPy arrays, broadcasting, vectorization)

---

## What this phase is about

Almost every numerical problem in engineering ends up as a **linear system**:

**A x = b**

- Finite element analysis, circuits, structures, heat flow, control, robotics, regression, machine learning: all of them solve `A x = b` somewhere inside.
- Solving it is not enough. You must also **measure** how much to trust the answer.

By the end of this phase you will be able to:

1. Explain what a linear system is, geometrically and algebraically.
2. Solve systems with `scipy.linalg.solve` and know how it works inside.
3. Write Gaussian elimination from scratch.
4. Understand floating-point error, residuals, forward error and backward error.
5. Compute and interpret the **condition number**.
6. Scale and prepare badly posed problems.
7. Write fast, memory-aware solver code.
8. Use advanced tricks: Schur complement and Sherman-Morrison updates.

## Roadmap

| Lesson | Topic | Level |
|---|---|---|
| A1 | Linear systems from scratch: geometry and vocabulary | Beginner |
| A2 | The matrix toolkit: determinant, inverse, norms | Beginner |
| A3 | How `solve` works: elimination, pivoting, from-scratch code | Beginner to Intermediate |
| A4 | Floating-point numbers and the three kinds of error | Intermediate |
| A5 | Conditioning: can I trust this answer? | Intermediate |
| A6 | Scaling, equilibration and unit hygiene | Intermediate |
| A7 | Performance and memory | Intermediate to Advanced |
| A8 | Advanced tricks: Schur complement, Sherman-Morrison | Advanced |
| Labs | Spring-mass chain, resistor network, polynomial conditioning, solver report tool | Practical |

**How to use this file:** type and run every code block yourself. Predict the output before you run it. Do the exercises before reading the hints.

Setup for every code block:

```python
import numpy as np
from scipy import linalg
```

---

# Lesson A1: Linear Systems from Scratch

## 1.1 What is a linear system?

A **linear equation** has unknowns that appear only to the first power, multiplied by constants and added together.

```
x + y = 3
x - y = 1
```

Two equations, two unknowns. A **system** of equations means all of them must hold at the same time.

Matrix form: collect the coefficients into a matrix `A`, the unknowns into a vector `x`, the right-hand sides into a vector `b`.

```
[1  1] [x]   [3]
[1 -1] [y] = [1]
```

or `A x = b`, with

```python
A = np.array([[1.,  1.],
              [1., -1.]])
b = np.array([3., 1.])
x = linalg.solve(A, b)
print(x)          # [2. 1.]   -> x = 2, y = 1
```

## 1.2 Two ways to picture it

**Row picture:** each equation is a line (in 2D), plane (in 3D) or hyperplane. The solution is where they all meet.

**Column picture:** write `A x = b` as

```
x * (column 1) + y * (column 2) = b
```

Solving the system means finding the weights that build `b` from the columns of `A`. This second view is the most useful one for the rest of linear algebra: `A x` is always **a combination of the columns of A**.

```python
col1, col2 = A[:, 0], A[:, 1]
print(2 * col1 + 1 * col2)       # [3. 1.]  equals b
```

## 1.3 Three possible outcomes

| Outcome | Row picture (2D) | Example |
|---|---|---|
| Exactly one solution | Lines cross at one point | `x + y = 3`, `x - y = 1` |
| No solution | Parallel lines, never meet | `x + y = 3`, `x + y = 5` |
| Infinitely many solutions | Same line twice | `x + y = 3`, `2x + 2y = 6` |

Which case you are in depends on the **rank** (the number of independent rows) of `A` and of the augmented matrix `[A | b]`.

**Rouche-Capelli rule:**

- `rank(A) < rank([A|b])` means **no solution** (inconsistent).
- `rank(A) = rank([A|b]) = n` (number of unknowns) means **unique solution**.
- `rank(A) = rank([A|b]) < n` means **infinitely many solutions**.

```python
def classify(A, b):
    A = np.atleast_2d(np.asarray(A, dtype=float))
    b = np.asarray(b, dtype=float).reshape(-1, 1)
    n = A.shape[1]
    r_A = np.linalg.matrix_rank(A)
    r_Ab = np.linalg.matrix_rank(np.hstack([A, b]))
    if r_A < r_Ab:
        return "no solution (inconsistent)"
    if r_A == n:
        return "unique solution"
    return "infinitely many solutions"

print(classify([[1, 1], [1, -1]], [3, 1]))   # unique solution
print(classify([[1, 2], [2, 4]], [3, 6]))    # infinitely many solutions
print(classify([[1, 2], [2, 4]], [3, 7]))    # no solution (inconsistent)
```

## 1.4 Shapes of systems

| Shape of A (rows x columns) | Name | Typical situation | Tool |
|---|---|---|---|
| n x n | Square | Exactly as many equations as unknowns | `solve` (this phase) |
| m x n with m > n | Tall / overdetermined | More measurements than unknowns, noisy data | `lstsq` (Phase C) |
| m x n with m < n | Wide / underdetermined | Fewer equations than unknowns | `lstsq`, `pinv` (Phase C) |

This phase focuses on **square** systems with a unique solution.

## 1.5 Vocabulary you must know

| Term | Meaning |
|---|---|
| Coefficient matrix | `A` |
| Right-hand side (RHS) | `b` |
| Solution vector | `x` |
| Singular matrix | No inverse; `det(A) = 0`; columns are dependent |
| Non-singular (invertible) | Has an inverse; unique solution for every `b` |
| Residual | `r = b - A x_computed`, how badly the equations are missed |
| Homogeneous system | `A x = 0` |

## Lesson A1 Exercises

1. Write the system `2x + 3y = 8`, `x - y = -1` as `A x = b`, solve it, and check the answer by hand.
2. Use the column picture: write `b` as a combination of the columns of `A` using the solution you found.
3. Use `classify` on a 3x3 system with two identical rows. What do you expect, and does the code agree?
4. Draw (with Matplotlib) the two lines of exercise 1 and mark the solution point.

---

# Lesson A2: The Matrix Toolkit

## 2.1 Creating and manipulating matrices

```python
A = np.array([[1., 2.],
              [3., 4.]])
B = np.array([[0., 1.],
              [1., 0.]])

A @ B             # matrix product
A * B             # element-by-element product (a different operation!)
A.T               # transpose
np.eye(2)         # identity matrix
np.diag([1, 2, 3])        # diagonal matrix
np.triu(A)        # upper triangle
np.tril(A)        # lower triangle
np.trace(A)       # sum of the diagonal: 5.0
```

Symmetric check:

```python
S = np.array([[2., 1.], [1., 3.]])
print(np.allclose(S, S.T))     # True
```

Key product facts:

- `A @ B` is generally **not equal** to `B @ A`.
- `(A @ B).T = B.T @ A.T`.
- `(A @ B)^-1 = B^-1 @ A^-1` (order reverses).

## 2.2 Determinant

```python
linalg.det(A)       # -2.0
```

Meaning: `|det(A)|` is the factor by which `A` scales **area** (2D) or **volume** (3D). The sign tells whether orientation flips.

- `det(A) = 0` means the matrix squashes space onto a lower dimension, so it is singular.
- Two properties: `det(A @ B) = det(A) det(B)` and `det(A.T) = det(A)`.

Warning (more in Lesson A5): the determinant is **not** a reliable test of "nearly singular". Use the condition number instead.

For big matrices, `det` can overflow or underflow. Use the log-determinant:

```python
sign, logdet = np.linalg.slogdet(A)
```

## 2.3 Inverse

```python
A_inv = linalg.inv(A)
print(A_inv)                            # [[-2. ,  1. ], [ 1.5, -0.5]]
print(np.allclose(A @ A_inv, np.eye(2)))   # True
```

`inv` exists only for non-singular matrices. For a singular one, SciPy raises `LinAlgError`.

You should rarely need the inverse. Lesson A3 explains why `solve(A, b)` replaces `inv(A) @ b` almost everywhere.

## 2.4 Norms: one number for "how big"

A **norm** turns a vector or matrix into a single non-negative number measuring its size.

**Vector norms**

| Name | Formula | Code |
|---|---|---|
| 2-norm (Euclidean length) | sqrt(sum of squares) | `linalg.norm(x)` |
| 1-norm | sum of absolute values | `linalg.norm(x, 1)` |
| infinity-norm | largest absolute value | `linalg.norm(x, np.inf)` |

```python
x = np.array([3., 4.])
print(linalg.norm(x))             # 5.0
print(linalg.norm(x, 1))          # 7.0
print(linalg.norm(x, np.inf))     # 4.0
```

**Matrix norms**

| Name | Meaning | Code |
|---|---|---|
| Frobenius | sqrt of the sum of all squared entries | `linalg.norm(A)` or `linalg.norm(A, "fro")` |
| 1-norm | largest absolute column sum | `linalg.norm(A, 1)` |
| infinity-norm | largest absolute row sum | `linalg.norm(A, np.inf)` |
| 2-norm (spectral) | largest stretch the matrix applies to a unit vector (largest singular value) | `linalg.norm(A, 2)` |
| Nuclear | sum of singular values | `linalg.norm(A, "nuc")` |

```python
print(linalg.norm(A, 1))         # 6.0  (columns: 1+3=4, 2+4=6)
print(linalg.norm(A, np.inf))    # 7.0  (rows: 1+2=3, 3+4=7)
print(linalg.norm(A))            # 5.477..., sqrt(1+4+9+16)=sqrt(30)
```

Norms of a matrix satisfy `||A x|| <= ||A|| ||x||`. This one inequality drives all the error analysis later in this phase.

**Relative size** is usually what matters: an error of 0.001 is large if `x` has size 0.002, and tiny if `x` has size 1000. So we use **relative** quantities such as `||error|| / ||x||`.

## Lesson A2 Exercises

1. Verify numerically that `(A @ B).T == B.T @ A.T` and `inv(A @ B) == inv(B) @ inv(A)` for two random 3x3 matrices.
2. Check `det(A @ B) == det(A) * det(B)`.
3. Compute all three vector norms of `[1, -2, 2]` by hand and in code.
4. Verify `||A x||_2 <= ||A||_2 ||x||_2` for 1000 random vectors `x`. How close does it come to equality for the best one?

---

# Lesson A3: How `solve` Works

## 3.1 The idea: elimination

Consider

```
 2x +  y +  z =  5
 4x + 3y + 3z = 13
 8x + 7y + 9z = 33
```

**Step 1:** use equation 1 to remove `x` from equations 2 and 3.

- Equation 2 minus 2 times equation 1: `y + z = 3`
- Equation 3 minus 4 times equation 1: `3y + 5z = 13`

**Step 2:** use the new equation 2 to remove `y` from equation 3.

- Equation 3 minus 3 times equation 2: `2z = 4`

Now the system is **upper triangular**:

```
2x + y + z = 5
    y + z = 3
        2z = 4
```

**Step 3: back substitution.** From the bottom up: `z = 2`, then `y = 1`, then `x = 1`.

That is **Gaussian elimination**. Everything else (LU, Cholesky, ...) is a refinement of this idea.

## 3.2 Partial pivoting

At each step the element used for elimination (the **pivot**) should be large in absolute value. If a pivot is tiny, dividing by it creates enormous multipliers and wrecks accuracy. So at each step we **swap rows** to bring the largest available entry (in that column) to the pivot position. This is **partial pivoting**, and it is why SciPy's LU returns a permutation matrix `P`. Lesson B2 demonstrates the disaster that pivoting prevents.

## 3.3 Gaussian elimination from scratch

```python
def gauss_solve(A, b):
    """Solve A x = b by Gaussian elimination with partial pivoting."""
    A = np.array(A, dtype=float)      # copies, so inputs are not modified
    b = np.array(b, dtype=float)
    n = len(b)

    # forward elimination
    for k in range(n - 1):
        p = k + np.argmax(np.abs(A[k:, k]))      # pivot row
        if A[p, k] == 0.0:
            raise ValueError("matrix is singular")
        if p != k:                                # swap rows
            A[[k, p]] = A[[p, k]]
            b[[k, p]] = b[[p, k]]
        for i in range(k + 1, n):
            m = A[i, k] / A[k, k]                 # multiplier
            A[i, k:] -= m * A[k, k:]
            b[i] -= m * b[k]

    if A[n - 1, n - 1] == 0.0:
        raise ValueError("matrix is singular")

    # back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - A[i, i + 1:] @ x[i + 1:]) / A[i, i]
    return x


A = np.array([[2., 1., 1.],
              [4., 3., 3.],
              [8., 7., 9.]])
b = np.array([5., 13., 33.])

print(gauss_solve(A, b))          # [1. 1. 2.]
print(linalg.solve(A, b))         # [1. 1. 2.]
```

Check against the hand calculation: `z = 2`, then `y = 3 - z = 1`, then `2x = 5 - y - z = 2` so `x = 1`. The solution vector `[x, y, z] = [1, 1, 2]` is exactly what both functions print.

Test on random matrices:

```python
rng = np.random.default_rng(0)
for n in (3, 10, 50):
    A = rng.standard_normal((n, n))
    b = rng.standard_normal(n)
    err = linalg.norm(gauss_solve(A, b) - linalg.solve(A, b))
    print(n, err)             # tiny, around 1e-14 or smaller
```

## 3.4 What it costs

For an n x n matrix, elimination takes about `(2/3) n^3` floating-point operations (flops). Back substitution only about `n^2`.

Doubling `n` makes the work about **8 times** bigger. Check it:

```python
import time

def timeit(f):
    t0 = time.perf_counter()
    f()
    return time.perf_counter() - t0

rng = np.random.default_rng(0)
for n in (200, 400, 800, 1600):
    A = rng.standard_normal((n, n))
    b = rng.standard_normal(n)
    print(n, f"{timeit(lambda: linalg.solve(A, b)):.4f} s")
```

The times will not show an exact factor of 8 on small sizes (the library is highly optimized and multi-threaded), but the trend is clear.

## 3.5 Using `scipy.linalg.solve`

```python
x = linalg.solve(A, b)
```

Full signature (important parts):

```python
linalg.solve(a, b, lower=False, overwrite_a=False, overwrite_b=False,
             check_finite=True, assume_a=None, transposed=False)
```

### Always check the answer

```python
A = np.array([[3.,  2., 0.],
              [1., -1., 0.],
              [0.,  5., 1.]])
b = np.array([2., 4., -1.])

x = linalg.solve(A, b)
print(x)                              # [ 2. -2.  9.]
r = b - A @ x                         # residual
print(linalg.norm(r))                 # tiny
print(np.allclose(A @ x, b))          # True
```

### Why never `inv(A) @ b`

```python
x_bad  = linalg.inv(A) @ b            # builds all n^2 entries of the inverse first
x_good = linalg.solve(A, b)           # solves directly
```

1. `inv` costs about 3 times more work than `solve`.
2. The extra operations add rounding error, so `inv(A) @ b` is usually less accurate.
3. The inverse of a sparse or banded matrix is dense, wasting memory and time.

Compute the explicit inverse only when you really need the inverse matrix itself (for example to examine a flexibility matrix).

### Multiple right-hand sides

Pass `b` as a matrix. Each column is a separate right-hand side, solved in one call:

```python
B = np.array([[2., 1.],
              [4., 0.],
              [-1., 3.]])
X = linalg.solve(A, B)
print(np.allclose(A @ X, B))          # True
```

### Telling SciPy about structure: `assume_a`

| `assume_a` | Meaning | Method used |
|---|---|---|
| `"gen"` | General matrix (default) | LU with pivoting |
| `"sym"` | Symmetric | LDL^T-type |
| `"her"` | Hermitian (complex symmetric) | LDL^H-type |
| `"pos"` | Symmetric positive definite | Cholesky, fastest |

Newer SciPy versions also accept longer words like `"positive definite"` or `"symmetric"`. Use whichever your version documents.

```python
K = np.array([[ 2., -1.,  0.],
              [-1.,  2., -1.],
              [ 0., -1.,  2.]])
f = np.array([0., 0., 1.])
x = linalg.solve(K, f, assume_a="pos")
```

If you promise `"pos"` and the matrix is not positive definite, SciPy raises `LinAlgError`. If you promise symmetry but the matrix is not symmetric, the result will silently be wrong. **Never claim a property you have not verified.**

### Solving with the transpose

`transposed=True` solves `A^T x = b` without forming `A.T`:

```python
x = linalg.solve(A, b, transposed=True)
print(np.allclose(A.T @ x, b))        # True
```

### Triangular systems

If `A` is already triangular, use `solve_triangular`. This is the cheapest solve (about `n^2` flops) and the final stage of every other solver.

```python
U = np.array([[2., 1., 1.],
              [0., 3., 2.],
              [0., 0., 4.]])
b = np.array([4., 5., 8.])
x = linalg.solve_triangular(U, b, lower=False)
print(np.allclose(U @ x, b))          # True

# lower triangular: lower=True
# solve with transpose: trans="T"
```

### Singular matrices

```python
S = np.array([[1., 2.],
              [2., 4.]])
try:
    linalg.solve(S, np.array([1., 2.]))
except linalg.LinAlgError as e:
    print("LinAlgError:", e)
```

For **exactly** singular matrices SciPy raises `LinAlgError`. For **nearly** singular matrices it may only issue a `LinAlgWarning` ("Ill-conditioned matrix"). Treat that warning as a serious sign (Lesson A5).

## Lesson A3 Exercises

1. Solve `x + 2y + 3z = 14`, `2x + 5y + 2z = 18`, `3x + y + 5z = 20` with both `gauss_solve` and `linalg.solve`.
2. Modify `gauss_solve` to also return the number of row swaps it performed. What is the connection between that count and the sign of the determinant?
3. For a random 800x800 matrix, time `linalg.solve(A, b)` and `linalg.inv(A) @ b`. Compute the residual norm of each. Which is faster, which is more accurate?
4. Use `transposed=True` to solve `A^T x = b`, then verify without forming `A.T`.
5. Create a symmetric positive definite matrix as `B.T @ B + np.eye(n)` and time `assume_a="gen"` against `assume_a="pos"` for n = 2000.

---

# Lesson A4: Floating-Point Numbers and the Three Kinds of Error

## 4.1 Computers do not store real numbers exactly

A `float64` has about **16 significant decimal digits**. Most decimals cannot be stored exactly.

```python
print(0.1 + 0.2)                  # 0.30000000000000004
print(0.1 + 0.2 == 0.3)           # False
print(np.isclose(0.1 + 0.2, 0.3)) # True
```

**Machine epsilon** is the smallest relative gap:

```python
eps = np.finfo(float).eps
print(eps)                        # 2.220446049250313e-16
```

Every arithmetic operation introduces a relative error of up to about `eps / 2`. Over millions of operations, errors can pile up or get amplified. Numerical linear algebra is mostly the study of controlling that amplification.

## 4.2 Catastrophic cancellation

Subtracting two nearly equal numbers destroys significant digits.

```python
print((1e16 + 1) - 1e16)          # 0.0, but the exact answer is 1
x = 1e-8
print((1 + x) - 1)                # 9.99999993922529e-09, only about 8 correct digits
```

Rule: avoid subtracting nearly equal quantities. In linear algebra this appears when a pivot is close to zero or when rows are almost dependent.

## 4.3 Three ways to measure error in a solved system

Suppose the true answer is `x`, and your computer gives `x_hat`.

| Measure | Formula | Meaning |
|---|---|---|
| **Forward error** | `||x_hat - x|| / ||x||` | How far is my answer from the true answer? You usually cannot compute this because you do not know `x`. |
| **Residual** | `r = b - A x_hat` | How badly does my answer fail the equations? Always computable. |
| **Backward error** | smallest relative change to `A` and `b` that makes `x_hat` an exact solution | Is my answer the exact answer to a nearby problem? |

For the normwise backward error there is a formula:

```python
def backward_error(A, x_hat, b):
    r = b - A @ x_hat
    return linalg.norm(r) / (linalg.norm(A, np.inf) * linalg.norm(x_hat, np.inf)
                             + linalg.norm(b, np.inf))
```

(This version uses the infinity norm throughout, which is a standard choice.)

## 4.4 The key fact about `solve`

Gaussian elimination with partial pivoting (what `solve` uses) is **backward stable** in practice: the computed `x_hat` is the *exact* solution of a problem whose `A` and `b` differ from yours by only a few multiples of `eps`.

```python
rng = np.random.default_rng(0)
A = rng.standard_normal((200, 200))
x_true = rng.standard_normal(200)
b = A @ x_true
x_hat = linalg.solve(A, b)

print("backward error:", backward_error(A, x_hat, b))   # around 1e-16
print("forward error :", linalg.norm(x_hat - x_true) / linalg.norm(x_true))
```

So the backward error is always tiny. Then why can the forward error be large? Because of the next lesson: conditioning.

**Master relation:**

> forward error is roughly at most (condition number) times (backward error)

Backward error is controlled by the algorithm (small for `solve`). The condition number belongs to the **problem**, and no algorithm can remove it.

## 4.5 A residual can lie to you

Small residual does **not** mean small forward error. Lesson A5 shows an example where the residual is around `1e-16` but the answer is wrong in the 4th digit.

## Lesson A4 Exercises

1. Start with `x = 1.0` and keep halving it until `1 + x == 1` becomes true. What value of `x` do you stop at, and how does it compare to `eps`?
2. Compute `(1 + 1e-15) - 1` and explain the number of correct digits.
3. Compute the quadratic roots of `x^2 - 1e8 x + 1 = 0` using the textbook formula, then using the stable form for the small root `c / (a x_large)`. Compare the small root. (Hint: cancellation.)
4. Compute the backward error of `solve` for 20 random matrices of size 100. Is it ever above `1e-13`?

---

# Lesson A5: Conditioning, Can I Trust This Answer?

## 5.1 The core idea

Some problems are **sensitive**: a tiny change in the input (due to rounding or measurement noise) causes a huge change in the output. These are called **ill-conditioned**.

Example. Two nearly parallel lines:

```python
A = np.array([[1., 1.],
              [1., 1.0001]])

b1 = np.array([2., 2.0001])
b2 = np.array([2., 2.0002])      # b changed by about 0.005 percent

print(linalg.solve(A, b1))        # [1. 1.]
print(linalg.solve(A, b2))        # [0. 2.]
```

A change of `0.0001` in one entry of `b` flips the solution from `(1, 1)` to `(0, 2)`. The lines meet at a very shallow angle, so tiny shifts slide the crossing point far.

## 5.2 The condition number

**cond(A) = ||A|| · ||A^-1||**

(2-norm version: `cond(A) = sigma_max / sigma_min`, the ratio of largest to smallest singular value.)

```python
print(np.linalg.cond(A))          # about 40002, so a perturbation can be amplified about 40000 times
```

**Fundamental bound.** If `A x = b` and we perturb `b` to `b + db`, then

```
||dx|| / ||x||   <=   cond(A) * ||db|| / ||b||
```

The relative change in the answer can be up to `cond(A)` times the relative change in the data. A similar bound holds for perturbations of `A`.

**Rule of thumb for digits lost:** about `log10(cond(A))` digits.

| cond(A) | Digits lost (of about 16) | Verdict |
|---|---|---|
| 1 to 100 | about 0 to 2 | Excellent |
| 1e3 to 1e6 | 3 to 6 | Fine, be aware |
| 1e8 to 1e12 | 8 to 12 | Suspicious |
| 1e13 and above | 13 or more | Probably meaningless |
| about 1e16 and above | all | Numerically singular |

`np.linalg.cond(A)` computes it with the SVD. For big matrices there are cheaper estimates, but this is the exact tool for medium sizes.

Special values:

- `cond(A) >= 1` always.
- `cond(Q) = 1` for any orthogonal matrix `Q` (rotations are perfectly conditioned).
- `cond(A) = infinity` for singular matrices.

## 5.3 Hilbert matrices: a famous bad example

The Hilbert matrix `H[i, j] = 1 / (i + j + 1)` is a classic ill-conditioned test.

```python
for n in range(2, 13, 2):
    H = linalg.hilbert(n)
    print(n, f"{np.linalg.cond(H):.2e}")
```

The condition number grows exponentially with `n`. For `n = 10` it is about `1.6e13`.

Now watch it hurt:

```python
n = 10
H = linalg.hilbert(n)
x_true = np.ones(n)
b = H @ x_true
x_hat = linalg.solve(H, b)

print("residual norm :", linalg.norm(b - H @ x_hat))              # tiny, near 1e-16
print("forward error :", linalg.norm(x_hat - x_true) / linalg.norm(x_true))   # large
print("bound         :", np.linalg.cond(H) * np.finfo(float).eps)
```

The residual is around `1e-16`. The answer is wrong in several digits. **This is the most important lesson in the phase:**

> **A tiny residual proves the answer solves a nearby problem. It does not prove the answer is close to the true solution. If the matrix is ill-conditioned, the nearby problem has a different answer.**

## 5.4 Determinant is NOT a conditioning test

Newcomers often think "determinant near zero means nearly singular". Wrong:

```python
n = 10
A_small = 1e-10 * np.eye(n)
print(linalg.det(A_small))         # 1e-100, looks "almost zero"
print(np.linalg.cond(A_small))     # 1.0, perfectly conditioned
```

The matrix is just a scaled identity: every system solves trivially and accurately. Determinant depends on scaling; the condition number does not. **Always use `cond`, never `det`, to judge sensitivity.**

## 5.5 Where ill-conditioning comes from in real work

| Source | Example |
|---|---|
| Nearly dependent equations | Two sensors measuring almost the same quantity |
| Nearly parallel geometry | Triangulation with a tiny baseline |
| Polynomial fitting at high degree | Vandermonde matrices (Lab A3) |
| Mixed scales | Metres and nanometres in the same system |
| Long chains and fine meshes | Stiffness matrices: `cond` grows like `N^2` for N unknowns |
| Regression with correlated features | Multicollinearity |

## 5.6 What to do about it

1. **Check:** compute `cond(A)` before trusting `x`.
2. **Rescale** to well-balanced units (Lesson A6).
3. **Reformulate** the model: remove redundant unknowns or use a better basis (orthogonal polynomials, Phase C).
4. **Regularize**: add a small stabilizing term (Phase C, ridge regression).
5. **Use SVD-based tools** (`lstsq`, `pinv`) that handle near-dependence gracefully.
6. **Measure less ambitiously:** report answers only to the number of digits the conditioning allows.

## 5.7 Sensitivity experiment you can run on any system

```python
def sensitivity(A, b, rel_noise=1e-10, trials=20, seed=0):
    """Perturb b slightly many times and report the worst amplification."""
    rng = np.random.default_rng(seed)
    x = linalg.solve(A, b)
    worst = 0.0
    for _ in range(trials):
        db = rng.standard_normal(b.shape)
        db *= rel_noise * linalg.norm(b) / linalg.norm(db)
        dx = linalg.solve(A, b + db) - x
        amp = (linalg.norm(dx) / linalg.norm(x)) / (linalg.norm(db) / linalg.norm(b))
        worst = max(worst, amp)
    return worst

H = linalg.hilbert(8)
b = H @ np.ones(8)
print(sensitivity(H, b))          # large, compare with np.linalg.cond(H)
print(np.linalg.cond(H))
```

The observed amplification is below `cond(A)` and often close to it for unlucky directions. This empirical test works even when you can only call a black-box solver.

## Lesson A5 Exercises

1. Build `A = [[1, 1], [1, 1 + eps]]` for `eps = 1e-2, 1e-4, 1e-6, 1e-8, 1e-10`. Print `cond(A)` for each and check that `cond` is roughly `4 / eps`.
2. For which Hilbert size `n` does the residual stay near `1e-16` while the forward error reaches 1 (no correct digits)?
3. Show that orthogonal matrices have `cond = 1` by building a random orthogonal matrix with `linalg.qr(rng.standard_normal((5, 5)))[0]`.
4. Build a 3x3 matrix with `det` equal to `1e6` but a large `cond`. (Hint: use `diag(1e6, 1, 1e-6)` times a rotation, then compare scaled variants.) What does that tell you about `det` as a quality measure?

---

# Lesson A6: Scaling, Equilibration and Unit Hygiene

## 6.1 Badly scaled problems

Condition numbers can be inflated just because rows or columns have wildly different sizes, even if the underlying problem is perfectly fine.

```python
B = np.array([[1., 2.],
              [3., 4.]])
A = np.diag([1e6, 1.]) @ B          # first equation multiplied by a million
print(np.linalg.cond(B))            # about 14.9
print(np.linalg.cond(A))            # about 2.5e6
```

Equation 1 was simply multiplied by `1e6`. The solution is identical but `cond` got 170,000 times worse.

## 6.2 Equilibration

**Equilibration** rescales rows and columns so that all have similar size.

Row scaling: divide each row (and the corresponding entry of `b`) by that row's norm.

```python
b = np.array([5., 6.])

row_max = np.max(np.abs(A), axis=1)      # largest entry in each row
D = np.diag(1.0 / row_max)
A_scaled = D @ A
b_scaled = D @ b

print(np.linalg.cond(A_scaled))                         # small again
x1 = linalg.solve(A, b)
x2 = linalg.solve(A_scaled, b_scaled)
print(np.allclose(x1, x2))                              # True: same mathematical answer
```

(Note: `scipy.linalg.norm` does not take an `axis` argument in all versions, which is why we compute row maxima with NumPy.)

Rules:

- **Row scaling** `D A x = D b` does not change `x`.
- **Column scaling** `A S y = b` with `x = S y` changes the variable: solve for `y`, then compute `x = S y`.

## 6.3 Unit hygiene

Use **consistent SI units** in every equation. Typical disasters:

| Mistake | Effect |
|---|---|
| Stiffness in N/mm and force in kN | Residual-looking answers off by 1000 |
| Metres and millimetres mixed in a stiffness matrix | Huge cond |
| Probabilities (0 to 1) next to counts (millions) | Bad scaling |

Habit: convert everything to SI at the start (Module 0, `scipy.constants`), compute, then convert results at the end. Also **non-dimensionalize** when you can: divide each variable by a typical size so every unknown is of order 1.

## 6.4 Rank decisions depend on scale too

`np.linalg.matrix_rank` uses a tolerance based on the largest singular value, so a column that is tiny only because of units may look "dependent". Scale first, then ask about rank.

## Lesson A6 Exercises

1. Take any well-conditioned 5x5 matrix and multiply its rows by `[1, 1e3, 1e-3, 1e6, 1e-6]`. Measure `cond` before and after, then equilibrate and measure again.
2. Solve a system with column scaling: define `S = diag(s)` with large `s`, solve `A S y = b`, recover `x = S y`, verify `A x = b`.
3. Write `equilibrate(A, b)` that returns the scaled `A_scaled`, `b_scaled` and the row-scale factors. Test it on exercise 1.

---

# Lesson A7: Performance and Memory

## 7.1 Cost table (square n x n, rough flop counts)

| Operation | Cost | Notes |
|---|---|---|
| Matrix-vector product | `2 n^2` | |
| Matrix-matrix product | `2 n^3` | |
| LU factorization | about `(2/3) n^3` | The core of `solve` |
| Triangular solve | `n^2` | Cheap |
| Cholesky | about `(1/3) n^3` | Half of LU |
| Explicit inverse | about `2 n^3` | About 3 times `solve` |
| Eigenvalues, SVD | roughly 10 to 25 times LU | Phase B |

Memory: a dense `float64` matrix of size `n x n` takes `8 n^2` bytes.

| n | Memory |
|---|---|
| 1,000 | 8 MB |
| 10,000 | 800 MB |
| 50,000 | 20 GB |

When `n` reaches the tens of thousands, dense storage is no longer an option. That is when you switch to sparse matrices (Module 3) or banded solvers (Phase C).

## 7.2 Useful keyword arguments

```python
x = linalg.solve(A, b, check_finite=False)       # skip scan for NaN/inf (faster)
x = linalg.solve(A, b, overwrite_a=True)         # allow SciPy to destroy A (saves memory)
```

- `check_finite=False` saves a pass over the data. Safe only if you are sure there are no `nan` or `inf` (otherwise you may get garbage or crashes).
- `overwrite_a=True` and `overwrite_b=True` let LAPACK reuse your arrays. Never use them if you need the original afterwards. They only take effect when the array has the right type and memory layout.

## 7.3 Data types

```python
A32 = A.astype(np.float32)
x32 = linalg.solve(A32, b.astype(np.float32))
print(x32.dtype)                  # float32
print(np.finfo(np.float32).eps)   # about 1.19e-07
```

`float32` halves memory and can be faster on some hardware, but has only about 7 digits. Linear algebra at `float32` loses accuracy fast (a condition number of `1e7` already destroys all digits). Default to `float64` unless you have a strong reason.

Also watch integer inputs: `np.array([[1, 2], [3, 4]])` is `int64`. SciPy converts to float internally, but explicit `dtype=float` makes intent clear and avoids surprises.

## 7.4 Solve once, reuse many times

If the same `A` is used with many right-hand sides, factor once. That is the topic of Lesson B2 (`lu_factor` and `lu_solve`). Never loop over `linalg.solve(A, b_i)` when `A` does not change.

```python
rng = np.random.default_rng(0)
n, m = 1000, 200
A = rng.standard_normal((n, n))
B = rng.standard_normal((n, m))

t_loop = timeit(lambda: [linalg.solve(A, B[:, i]) for i in range(m)])
t_block = timeit(lambda: linalg.solve(A, B))
print(t_loop, t_block)            # the block version is far faster
```

## 7.5 Stacks of small systems

`numpy.linalg.solve` broadcasts over stacks of matrices:

```python
As = rng.standard_normal((1000, 3, 3))      # 1000 separate 3x3 matrices
bs = rng.standard_normal((1000, 3, 1))
xs = np.linalg.solve(As, bs)                 # shape (1000, 3, 1)
```

For many tiny systems (for example one per pixel, per particle, per time step), this is much faster than a Python loop. Whether `scipy.linalg` itself accepts stacks depends on your SciPy version, so check the docs of your installed version.

## 7.6 Timing and profiling habits

- Time with `time.perf_counter()` or in Jupyter with `%timeit`.
- Time the **second** call, not the first (warm-up effects, imports).
- Use realistic sizes. A 10x10 benchmark tells you nothing about a 5000x5000 problem.
- Multi-threading: NumPy and SciPy call BLAS libraries that use several CPU cores, so timings depend on your hardware.

## Lesson A7 Exercises

1. Measure how `solve` time scales for `n = 250, 500, 1000, 2000`. Fit the slope on a log-log plot. Is it close to 3?
2. Measure the speed gap between `check_finite=True` and `False` for a 3000x3000 solve.
3. Create a stack of 100,000 random 2x2 systems and solve them (a) with a Python loop of `linalg.solve`, (b) with `np.linalg.solve` on the stack. Time both.
4. Compute memory in MB for a dense 20000x20000 `float64` matrix. Could your laptop hold it?

---

# Lesson A8: Advanced Tricks

## 8.1 Block systems and the Schur complement

Many problems naturally split into blocks (for example displacements and pressures, or interior and boundary unknowns):

```
[A11 A12] [x1]   [b1]
[A21 A22] [x2] = [b2]
```

Eliminating `x1` gives the **Schur complement**:

**S = A22 - A21 A11^-1 A12**

Procedure:

1. Solve `A11 y = b1` and `A11 Z = A12` (reuse one factorization).
2. Form `S = A22 - A21 Z`.
3. Solve `S x2 = b2 - A21 y`.
4. Recover `x1 = y - Z x2`.

```python
rng = np.random.default_rng(0)
n1, n2 = 4, 3
A11 = rng.standard_normal((n1, n1)) + n1 * np.eye(n1)
A12 = rng.standard_normal((n1, n2))
A21 = rng.standard_normal((n2, n1))
A22 = rng.standard_normal((n2, n2)) + n2 * np.eye(n2)
b1 = rng.standard_normal(n1)
b2 = rng.standard_normal(n2)

lu = linalg.lu_factor(A11)
y = linalg.lu_solve(lu, b1)
Z = linalg.lu_solve(lu, A12)
S = A22 - A21 @ Z
x2 = linalg.solve(S, b2 - A21 @ y)
x1 = y - Z @ x2

# verify against the full solve
A = np.block([[A11, A12], [A21, A22]])
b = np.concatenate([b1, b2])
print(np.allclose(np.concatenate([x1, x2]), linalg.solve(A, b)))   # True
```

Why it matters: substructuring in finite elements, constrained systems (Lagrange multipliers), Kalman filtering, and Gaussian conditional distributions all rely on the Schur complement.

## 8.2 Sherman-Morrison: a cheap rank-one update

Suppose you already know how to solve with `A` and the matrix changes by a rank-one term `u v^T` (one spring added to a structure, one new sensor reading). You do **not** need to refactor.

```
(A + u v^T)^-1 b = A^-1 b  -  (A^-1 u) (v^T A^-1 b) / (1 + v^T A^-1 u)
```

Cost: two solves with the **existing** factorization.

```python
rng = np.random.default_rng(1)
n = 6
A = rng.standard_normal((n, n)) + n * np.eye(n)
u = rng.standard_normal(n)
v = rng.standard_normal(n)
b = rng.standard_normal(n)

lu = linalg.lu_factor(A)
y = linalg.lu_solve(lu, b)         # A^-1 b
z = linalg.lu_solve(lu, u)         # A^-1 u
x = y - z * (v @ y) / (1.0 + v @ z)

print(np.allclose(x, linalg.solve(A + np.outer(u, v), b)))   # True
```

The formula breaks down if `1 + v^T A^-1 u` is close to zero (then `A + u v^T` is nearly singular). The generalization to rank `k` is the Woodbury identity.

## 8.3 Iterative refinement (concept)

After computing `x`, you can improve it:

1. Compute the residual `r = b - A x`, ideally in **higher precision**.
2. Solve `A dx = r` using the existing factorization.
3. Update `x = x + dx`.

With a residual computed in higher precision, this can recover accuracy lost to rounding (but not accuracy lost to bad conditioning of the *data*). Libraries like LAPACK have "expert drivers" that do this automatically. In plain `float64` with a residual in `float64`, the benefit is limited, so treat this as a concept to know, not a default routine.

## 8.4 Failure modes checklist

| Symptom | Likely cause | Action |
|---|---|---|
| `LinAlgError: singular matrix` | Dependent rows or columns, modelling error | Check rank; fix the model or use `lstsq` |
| `LinAlgWarning: ill-conditioned` | Large `cond` | Rescale, reformulate, regularize |
| Tiny residual, wrong answer | Ill-conditioning | Report `cond`, trust fewer digits |
| `nan` or `inf` in answer | Bad inputs (`nan` in `A`) | Keep `check_finite=True` while debugging |
| Slow or out of memory | Dense matrix too large | Banded or sparse (Phase C, Module 3) |
| Results change between machines | Rounding order differs under multithreading | Compare with tolerances, never `==` |

## Lesson A8 Exercises

1. Rebuild the Schur complement example with a 20x20 `A11` and a 5x5 `A22`. Count how many full-size solves you avoid.
2. Use Sherman-Morrison to model adding one extra spring between mass 2 and mass 3 of the three-mass chain (the update is `k * u u^T` with `u = [0, 1, -1]`).
3. Show numerically that Sherman-Morrison fails when `1 + v^T A^-1 u` is almost zero. Construct an example.
4. Look up the Woodbury identity and verify it numerically for a rank-2 update.

---

# Labs

## Lab A1: Spring-mass chain (structures)

Three masses in a row, connected by springs, with both ends fixed to walls. Each spring has stiffness `k = 1000 N/m`. A 10 N force pushes the third mass.

```python
import numpy as np
from scipy import linalg

k = 1000.0
K = k * np.array([[ 2., -1.,  0.],
                  [-1.,  2., -1.],
                  [ 0., -1.,  2.]])
f = np.array([0., 0., 10.])

u = linalg.solve(K, f, assume_a="pos")
print(u)                                   # [0.0025 0.005  0.0075]  (metres)
print("residual:", linalg.norm(K @ u - f))
print("cond(K) :", np.linalg.cond(K))      # about 5.83
```

Check by hand. Row 3: `1000 * (-0.005 + 2*0.0075) = 10` N. Row 1: `1000 * (2*0.0025 - 0.005) = 0`. Good.

**Extensions:**

1. **Superposition:** verify `solve(K, f1 + f2) == solve(K, f1) + solve(K, f2)` for two different load vectors.
2. **Flexibility matrix:** compute `linalg.inv(K)`. Column `j` is the response to a unit force at mass `j`. Check it is symmetric (Maxwell reciprocity: the effect at `i` of a force at `j` equals the effect at `j` of the same force at `i`).
3. **Growing chain:** build `K` for `N = 5, 10, 20, 50, 100` with `np.diag` and print `cond(K)`. It grows roughly like `N^2`. For `N = 50` it is about 1000. Explain physically: a longer chain becomes more flexible overall, so a tiny force pattern can produce a large displacement.
4. **Different boundary:** free one end (remove the wall spring on the right). The matrix becomes `[[2,-1,0],[-1,2,-1],[0,-1,1]]`. Show that if you free **both** ends, the matrix becomes singular (rigid-body motion) and `solve` fails.

## Lab A2: Resistor network (nodal analysis)

Kirchhoff's current law at each node gives `G V = I`, where `G` is the conductance matrix, `V` the node voltages and `I` the injected currents.

Circuit: nodes 1, 2, 3 in a ladder. Resistors: node 1 to ground, 1 to 2, 2 to 3, 3 to ground, all 1 ohm. Inject 1 A into node 1.

```python
import numpy as np
from scipy import linalg

R1 = R2 = R3 = R4 = 1.0
g1, g2, g3, g4 = 1/R1, 1/R2, 1/R3, 1/R4
G = np.array([[g1 + g2, -g2,      0.0],
              [-g2,     g2 + g3, -g3],
              [0.0,    -g3,      g3 + g4]])
I = np.array([1.0, 0.0, 0.0])

V = linalg.solve(G, I, assume_a="pos")
print(V)                                  # [0.75 0.5  0.25]
```

Verify: row 1 gives `2*0.75 - 0.5 = 1` A. Row 2: `-0.75 + 2*0.5 - 0.25 = 0`.

**Extensions:**

1. Change the resistor values to `[10, 100, 1000, 50]` ohms and see how `cond(G)` changes (this is a natural unit/scale problem: conductances span orders of magnitude).
2. Compute the current through each resistor from `V`.
3. Scale the problem to a 1000-node ladder using a banded solver (Phase C) and compare with the dense solve.

## Lab A3: Polynomial fitting and conditioning (preview of Phase C)

Fitting a polynomial of degree `d` to data in `x` leads to a **Vandermonde matrix**, which becomes ill-conditioned fast.

```python
import numpy as np
from scipy import linalg

x = np.linspace(0, 1, 30)
for d in (2, 5, 8, 12, 16, 20):
    V = np.vander(x, d + 1)
    print(d, f"{np.linalg.cond(V):.2e}")
```

Observe the exponential growth of `cond`. Then:

1. Build a smooth target `y = np.exp(x) * np.sin(3 * x)`.
2. Solve the fit using the **normal equations** `solve(V.T @ V, V.T @ y)`. For `d = 12`, check `cond(V.T @ V)` (it is about the square of `cond(V)`) and compare the fitted values against a `linalg.lstsq` fit.
3. Describe in two sentences when and why high-degree monomial fitting fails. (Phase C shows the cure: orthogonal bases and regularization.)

## Lab A4: Build your own solver report tool

Create `linear_system_lab.py` with a function `analyze_system(A, b)` that returns a dictionary (or prints a report):

| Field | How |
|---|---|
| `shape` | `A.shape` |
| `is_symmetric` | `np.allclose(A, A.T)` |
| `rank` | `np.linalg.matrix_rank(A)` |
| `cond` | `np.linalg.cond(A)` |
| `solution` | `linalg.solve` (with `assume_a="pos"` only if verified SPD by a try/except on `cholesky`) |
| `residual_norm` | `linalg.norm(b - A @ x)` |
| `backward_error` | from Lesson A4 |
| `digits_trusted` | `max(0, 16 - np.log10(cond))` |
| `verdict` | "safe" if `cond < 1e6`, "careful" if `< 1e12`, else "unreliable" |

Test it on: a random matrix, the spring-mass matrix, the resistor matrix, a Hilbert matrix, and an exactly singular matrix (it must catch `LinAlgError` and report instead of crashing).

---

# Exercise Hints

Try everything first. Then check.

**A1.**
1. `A = [[2, 3], [1, -1]]`, `b = [8, -1]`: solution `x = 1, y = 2`.
3. A repeated row makes rank deficient: expect "no solution" or "infinitely many" depending on `b`.

**A2.**
2. Both identities are standard. Use `np.allclose`, never `==`.
4. Equality holds for the unit vector pointing along the top right singular vector.

**A3.**
1. Solution is `x = 1, y = 2, z = 3` for the first system.
2. Each swap flips the sign of the determinant.
3. `solve` should be faster and give a residual that is equal or smaller.

**A4.**
1. You stop at about `1.1e-16`, which is `eps / 2`: anything smaller than half the gap to the next float vanishes when added to 1.
3. The textbook formula loses digits for the small root because `1e8 - sqrt(1e16 - 4)` subtracts two nearly equal numbers. Compute the large root first, then get the small one from `x_small = c / (a * x_large)`.

**A5.**
1. The product `cond * eps` should be close to `4`.
2. Around `n = 12` or so the forward error reaches order 1.
4. `diag(1e6, 1, 1e-6)` has `det = 1` but `cond = 1e12`, while `1e2 * np.eye(3)` has `det = 1e6` but `cond = 1`. Determinant says nothing reliable about conditioning.

**A6.**
1. After row scaling by `1 / max(abs(row))` the cond should drop back to a moderate value.

**A7.**
1. Slope close to 3 for large `n` (lower for small `n` because of overhead).
3. The stacked call is typically tens to hundreds of times faster.
4. `20000^2 * 8` bytes is 3.2 GB.

**A8.**
2. `K_new = K + k * np.outer(u, u)` with `u = [0, 1, -1]`.

---

# Common Mistakes

| Mistake | Fix |
|---|---|
| `A * B` when you meant matrix product | Use `A @ B` |
| `inv(A) @ b` | Use `solve(A, b)` |
| Judging singularity by `det` | Use `cond` or the rank |
| Trusting a small residual alone | Always look at `cond(A)` |
| Comparing floats with `==` | Use `np.allclose` or `np.isclose` |
| Claiming `assume_a="pos"` without checking | Test with `cholesky` first |
| Looping `solve` over many `b` | Pass a matrix or factor once |
| Mixed units | Convert everything to SI first |
| Using `float32` by accident | Make `dtype=float` explicit |
| Forgetting `lower=True` in triangular solves | Check the triangle with `np.triu` or `np.tril` |

# Cheat Sheet

```python
x = linalg.solve(A, b)                        # general
x = linalg.solve(A, b, assume_a="pos")        # symmetric positive definite
x = linalg.solve(A, b, transposed=True)       # A.T x = b
x = linalg.solve_triangular(U, b, lower=False)

np.linalg.cond(A)                              # condition number
np.linalg.matrix_rank(A)                       # rank
linalg.norm(b - A @ x)                         # residual
np.linalg.slogdet(A)                           # log determinant (safe)
linalg.hilbert(n)                              # ill-conditioned test matrix
```

Decision rule: **solve, residual, cond, then report.**

---

# Phase A Checkpoint

You are ready for Phase B when you can honestly check every box:

- [ ] I can explain row picture and column picture of `A x = b`.
- [ ] I can classify a system as unique, none or infinite by rank.
- [ ] I wrote Gaussian elimination with pivoting from scratch.
- [ ] I can explain why `solve` beats `inv(A) @ b` in three ways.
- [ ] I know what residual, forward error and backward error each mean.
- [ ] I can explain why a tiny residual does not prove a good answer.
- [ ] I can compute and interpret `cond(A)` and the digits-lost rule.
- [ ] I know `det` is not a conditioning test, and I can show a counterexample.
- [ ] I can rescale a badly scaled system.
- [ ] I know when to use `assume_a`, `solve_triangular`, `overwrite_a` and `check_finite`.
- [ ] I solved the spring-mass and resistor labs and checked answers by hand.
- [ ] I built `analyze_system`.

## Quick self-quiz (answers at the bottom)

1. A solver returns a residual of `1e-16`. Is the answer necessarily accurate? Why?
2. Your matrix has `cond = 1e10`. About how many digits can you trust in `float64`?
3. Which is more reliable as a "nearly singular" signal: `det` or `cond`?
4. You must solve `A x = b_i` for 500 different `b_i` with the same `A`. What is the efficient approach?
5. `A` is symmetric positive definite and you promise `assume_a="pos"`. What is gained?

**Answers:** (1) No. If `cond` is large, the residual can be tiny while the error is big. (2) About 6 digits (16 - 10). (3) `cond`. (4) Stack the `b_i` as columns and solve once, or factor with `lu_factor` and reuse (Phase B). (5) A Cholesky-based solve that is about twice as fast and does not need pivoting.

---

# Suggested Repo Layout for This Phase

```
02-linear-algebra/phase-A-solving-and-measuring/
├── README.md
├── lessons/
│   ├── A1-linear-systems.md
│   ├── A2-matrix-toolkit.md
│   ├── A3-how-solve-works.md
│   ├── A4-floating-point-errors.md
│   ├── A5-conditioning.md
│   ├── A6-scaling.md
│   ├── A7-performance.md
│   └── A8-advanced-tricks.md
├── code/
│   ├── gauss_solve.py
│   ├── sensitivity.py
│   ├── schur_complement.py
│   └── sherman_morrison.py
├── labs/
│   ├── lab_A1_spring_mass.py
│   ├── lab_A2_resistor_network.py
│   ├── lab_A3_polynomial_conditioning.py
│   └── linear_system_lab.py
├── exercises/
└── tests/
    └── test_phase_A.py
```

**Next:** Phase B, Decompositions (`02B-decompositions.md`): LU, QR, Cholesky, eigenvalues, SVD.
