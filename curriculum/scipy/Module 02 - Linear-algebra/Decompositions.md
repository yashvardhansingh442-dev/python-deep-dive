# Module 2, Phase B: Decompositions

> **Part of:** SciPy Course, Module 2 (Linear Algebra, `scipy.linalg`)
> **Level:** Beginner to Advanced
> **Time:** about 3 to 4 days
> **Prerequisites:** Phase A (solving systems, residuals, conditioning)

---

## What this phase is about

A **decomposition** (or factorization) writes one complicated matrix as a product of simple matrices, just like writing `60 = 2 × 2 × 3 × 5`.

Why bother?

- Simple pieces (triangular, orthogonal, diagonal) are **easy to work with**: solving, inverting and measuring all become trivial.
- Each decomposition **reveals a property** of the matrix: rank, stretching directions, vibration modes, stability.
- Every serious numerical routine (including `solve`, `lstsq`, `eig`) is built on these.

| Decomposition | Form | Main uses |
|---|---|---|
| LU | `A = P L U` | Fast repeated solves, determinant |
| Cholesky | `A = L Lᵀ` | Fastest solve for symmetric positive definite, sampling, log-determinant |
| LDLᵀ | `A = L D Lᵀ` | Symmetric indefinite systems |
| QR | `A = Q R` | Stable least squares, orthonormal bases |
| Eigen | `A = V Λ V⁻¹` | Modes, stability, principal directions |
| Schur | `A = Z T Zᴴ` | Stable eigen computations, matrix functions |
| SVD | `A = U Σ Vᵀ` | Rank, conditioning, low-rank approximation, pseudo-inverse |

By the end of this phase you will be able to:

1. Build LU and QR from scratch and explain why pivoting and Householder reflections matter.
2. Pick the right decomposition for a given problem, and know its cost.
3. Compute eigenvalues and eigenvectors correctly (`eig` vs `eigh`), including generalized and banded problems.
4. Compute natural frequencies and mode shapes of mechanical systems.
5. Use the SVD for rank, null space, condition, polar decomposition and subspace angles.
6. Analyse stability of linear systems, including the non-normal transient-growth trap.

## Roadmap

| Lesson | Topic | Level |
|---|---|---|
| B1 | Triangular and permutation matrices | Beginner |
| B2 | LU decomposition and pivoting | Beginner to Intermediate |
| B3 | Cholesky and LDLᵀ | Intermediate |
| B4 | QR decomposition | Intermediate |
| B5 | Eigenvalues and eigenvectors | Intermediate to Advanced |
| B6 | Schur and Hessenberg forms | Advanced |
| B7 | Singular Value Decomposition | Intermediate to Advanced |
| B8 | Choosing the right decomposition | All |
| Labs | LU from scratch, showdown, vibration modes, principal stresses, rank detective | Practical |

Setup for every code block:

```python
import numpy as np
from scipy import linalg
import time

def timeit(f):
    t0 = time.perf_counter()
    f()
    return time.perf_counter() - t0
```

---

# Lesson B1: Triangular and Permutation Matrices

These are the building blocks of every other decomposition.

## 1.1 Triangular matrices

- **Lower triangular** `L`: zeros above the diagonal.
- **Upper triangular** `U`: zeros below the diagonal.

```python
U = np.array([[2., 1., 1.],
              [0., 3., 2.],
              [0., 0., 4.]])
L = U.T          # lower triangular
```

Properties:

- The determinant is the **product of the diagonal**.
- The eigenvalues are the diagonal entries.
- The product of two lower (upper) triangular matrices is lower (upper) triangular.
- Systems are solved by **substitution**, with no factorization needed.

## 1.2 Forward and back substitution

**Back substitution** for upper triangular `U x = b`: start from the last row, which has only one unknown.

```python
def back_substitution(U, b):
    n = len(b)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - U[i, i+1:] @ x[i+1:]) / U[i, i]
    return x

def forward_substitution(L, b):
    n = len(b)
    x = np.zeros(n)
    for i in range(n):
        x[i] = (b[i] - L[i, :i] @ x[:i]) / L[i, i]
    return x

b = np.array([4., 5., 8.])
print(back_substitution(U, b))                          # [0.8333, 0.3333, 2.0]
print(linalg.solve_triangular(U, b, lower=False))       # same
```

Cost: about `n²` operations, versus `n³` for a full solve. The whole point of decompositions is to reduce hard problems to triangular ones.

## 1.3 Permutation matrices

A **permutation matrix** `P` reorders rows (or columns). It is the identity with its rows shuffled.

```python
P = np.array([[0, 1, 0],
              [1, 0, 0],
              [0, 0, 1]], dtype=float)

A = np.arange(9.).reshape(3, 3)
print(P @ A)             # rows 0 and 1 swapped
print(P.T @ P)           # identity: P is orthogonal, so P^-1 = P^T
```

Key fact: `P⁻¹ = Pᵀ`, so permutations are free to invert and perfectly conditioned.

## Lesson B1 Exercises

1. Build a random 5x5 upper triangular matrix with `np.triu`, check that `det` equals the product of its diagonal and that `linalg.eigvals` returns the diagonal.
2. Solve `L x = b` with `forward_substitution`, then compare with `solve_triangular(L, b, lower=True)`.
3. Show that multiplying by `P` on the **right** shuffles columns instead of rows.

---

# Lesson B2: LU Decomposition and Pivoting

## 2.1 The idea

Gaussian elimination (Phase A) is secretly a factorization:

**P A = L U**

- `L` is lower triangular with ones on the diagonal. It stores the **multipliers** used during elimination.
- `U` is the upper triangular matrix you end up with.
- `P` records row swaps.

SciPy writes it as **A = P L U** (its `P` is the transpose of the `P` in `P A = L U`, so that `A = P L U` holds).

```python
A = np.array([[2., 1., 1.],
              [4., 3., 3.],
              [8., 7., 9.]])

P, L, U = linalg.lu(A)
print(np.allclose(A, P @ L @ U))      # True
print(L)
print(U)
```

Look at `L`: its entries below the diagonal are exactly the multipliers from elimination, and `U` is the triangular matrix from forward elimination.

## 2.2 LU from scratch

```python
def lu_scratch(A):
    """Return P, L, U with  P @ A = L @ U  (partial pivoting)."""
    A = np.array(A, dtype=float)
    n = A.shape[0]
    P = np.eye(n)
    L = np.zeros((n, n))
    U = A.copy()
    for k in range(n - 1):
        p = k + np.argmax(np.abs(U[k:, k]))        # pivot row
        if p != k:
            U[[k, p], k:] = U[[p, k], k:]
            L[[k, p], :k] = L[[p, k], :k]
            P[[k, p]] = P[[p, k]]
        for i in range(k + 1, n):
            L[i, k] = U[i, k] / U[k, k]
            U[i, k:] -= L[i, k] * U[k, k:]
    L += np.eye(n)
    U = np.triu(U)                                  # clean rounding dust below diagonal
    return P, L, U

rng = np.random.default_rng(0)
A = rng.standard_normal((6, 6))
P, L, U = lu_scratch(A)
print(np.allclose(P @ A, L @ U))                    # True

# compare with SciPy (remember A = P_scipy L U, so P_scipy = P.T)
Ps, Ls, Us = linalg.lu(A)
print(np.allclose(Ps, P.T), np.allclose(Ls, L), np.allclose(Us, U))   # True True True
```

## 2.3 Why pivoting is essential

Without row swaps, a tiny pivot creates a huge multiplier and destroys accuracy.

```python
A = np.array([[1e-20, 1.],
              [1.,    1.]])
b = np.array([1., 2.])

# elimination WITHOUT pivoting
l = A[1, 0] / A[0, 0]                 # 1e20: enormous multiplier
u22 = A[1, 1] - l * A[0, 1]           # about -1e20
y2 = b[1] - l * b[0]                  # about -1e20
x2 = y2 / u22
x1 = (b[0] - A[0, 1] * x2) / A[0, 0]
print(x1, x2)                         # 0.0 1.0     <- x1 is completely wrong

print(linalg.solve(A, b))             # [1. 1.]     <- correct
```

The true answer is `x1 ≈ 1`, `x2 ≈ 1`. The `1` in `1 - 1e20` is swallowed by rounding, so `x1` collapses to 0. **Partial pivoting** (swapping the largest entry into the pivot position) prevents this. It is the default in every library routine.

Even with pivoting, the **growth factor** (how much entries grow during elimination) can theoretically be exponential in contrived cases, but it is tiny in practice, which is why partial pivoting is trusted everywhere.

## 2.4 Factor once, solve many times

```python
lu, piv = linalg.lu_factor(A)               # expensive: about (2/3) n^3
x = linalg.lu_solve((lu, piv), b)           # cheap: about 2 n^2
```

- `lu_factor` returns a compact form: `L` and `U` stored together in one array, plus the pivot indices.
- `lu_solve` accepts one vector or a matrix of right-hand sides.
- `lu_solve((lu, piv), b, trans=1)` solves `Aᵀ x = b` using the **same** factorization.

Speed test:

```python
rng = np.random.default_rng(0)
n, m = 1500, 300
A = rng.standard_normal((n, n))
B = rng.standard_normal((n, m))

t_naive = timeit(lambda: [linalg.solve(A, B[:, i]) for i in range(m)])
lu_piv = linalg.lu_factor(A)
t_lu = timeit(lambda: [linalg.lu_solve(lu_piv, B[:, i]) for i in range(m)])
print(f"naive {t_naive:.2f}s   factor once {t_lu:.2f}s")
```

Real uses: a structure loaded in 1000 different ways, time-stepping simulations with a fixed matrix, Newton iterations with a frozen Jacobian.

## 2.5 Determinant and inverse from LU

The determinant is the product of the diagonal of `U`, times `(-1)^(number of swaps)`.

```python
lu, piv = linalg.lu_factor(A)
swaps = np.sum(piv != np.arange(len(piv)))
det_lu = np.prod(np.diag(lu)) * (-1) ** swaps
print(np.isclose(det_lu, linalg.det(A)))      # True (for moderate n)
```

For large `n` the product overflows. Use the log version:

```python
logdet = np.sum(np.log(np.abs(np.diag(lu))))
```

The inverse is "solve `A X = I`": `linalg.lu_solve((lu, piv), np.eye(n))`. This is what `inv` does.

## 2.6 Useful options

```python
P, L, U = linalg.lu(A)                       # A = P L U
PL, U = linalg.lu(A, permute_l=True)         # A = (P L) U, merges the permutation into L
```

## Lesson B2 Exercises

1. Verify `A = P @ L @ U` for ten random matrices and print the largest reconstruction error.
2. Use `lu_scratch` on a 4x4 matrix with a zero in position `[0, 0]`. Show that pivoting rescues it.
3. Time 500 solves with fixed `A` (n = 2000): naive loop vs `lu_factor` + `lu_solve` vs one block solve.
4. Use the transposed solve `lu_solve(..., trans=1)` to compute `A^T x = b` and verify.
5. For a 6x6 matrix, compute the determinant from LU by hand-count of swaps and confirm.

---

# Lesson B3: Cholesky and LDLᵀ

## 3.1 Symmetric positive definite (SPD) matrices

A symmetric matrix `A` is **positive definite** when `xᵀ A x > 0` for every nonzero `x`. Equivalent statements:

- All eigenvalues are positive.
- It can be written as `A = Bᵀ B` for some `B` with independent columns.
- Cholesky succeeds.

Where they appear: stiffness matrices, covariance matrices, `AᵀA` in least squares, Hessians at a minimum, mass matrices, conductance matrices.

## 3.2 Cholesky factorization

For SPD `A`:

**A = L Lᵀ**, with `L` lower triangular and positive diagonal.

Think of it as a matrix square root: `L` plays the role of `sqrt(A)`.

```python
A = np.array([[4., 2.],
              [2., 3.]])

L = linalg.cholesky(A, lower=True)
print(L)                                  # [[2.     0.    ]
                                          #  [1.     1.4142]]
print(np.allclose(L @ L.T, A))            # True
```

**Careful:** `linalg.cholesky` returns the **upper** factor `U` (with `A = Uᵀ U`) by default. Pass `lower=True` for `L`. This is a very common source of bugs.

Cost: about `n³ / 3`, half of LU, and no pivoting is needed (SPD matrices are always safe).

## 3.3 Solving with Cholesky

```python
c, low = linalg.cho_factor(A)                    # factor once
x = linalg.cho_solve((c, low), np.array([1., 2.]))   # reuse for many b
```

## 3.4 Cholesky as the cheapest SPD test

```python
def is_spd(A):
    if not np.allclose(A, A.T):
        return False
    try:
        linalg.cholesky(A)
        return True
    except linalg.LinAlgError:
        return False

print(is_spd(np.array([[4., 2.], [2., 3.]])))      # True
print(is_spd(np.array([[1., 2.], [2., 1.]])))      # False (eigenvalues 3 and -1)
```

## 3.5 Practical uses

### (a) Log-determinant, safely

For SPD `A`, `det(A) = (product of diag(L))²`, so

```python
L = linalg.cholesky(A, lower=True)
logdet = 2 * np.sum(np.log(np.diag(L)))
print(np.isclose(logdet, np.linalg.slogdet(A)[1]))     # True
```

This avoids overflow/underflow and appears in Gaussian log-likelihoods.

### (b) Generating correlated random data

If `Σ = L Lᵀ` and `z` is a vector of independent standard normals, then `L z` has covariance `Σ`.

```python
rng = np.random.default_rng(0)
Sigma = np.array([[4.0, 1.2],
                  [1.2, 1.0]])
L = linalg.cholesky(Sigma, lower=True)

z = rng.standard_normal((2, 100000))
samples = L @ z
print(np.cov(samples))                       # close to Sigma
```

Used for Monte Carlo simulation, sensor-noise generation and Kalman filter testing.

### (c) Mahalanobis distance (statistical distance)

The squared distance of `x` from mean `mu` in units of the covariance is `(x - mu)ᵀ Σ⁻¹ (x - mu)`. With `Σ = L Lᵀ` this equals `||L⁻¹ (x - mu)||²`, computed by a triangular solve (no explicit inverse):

```python
mu = np.array([1.0, 2.0])
x = np.array([3.0, 3.0])
y = linalg.solve_triangular(L, x - mu, lower=True)
print(y @ y)
```

### (d) Whitening

`L⁻¹ (x - mu)` has identity covariance, so it **decorrelates and normalizes** data.

## 3.6 LDLᵀ for symmetric indefinite matrices

If `A` is symmetric but **not** positive definite (for example saddle-point or KKT systems), Cholesky fails. Use the `LDLᵀ` factorization with pivoting:

```python
A = np.array([[1., 2.],
              [2., 1.]])             # eigenvalues 3 and -1: indefinite
lu, d, perm = linalg.ldl(A)
print(np.allclose(lu @ d @ lu.T, A))          # True
print(d)                                       # block diagonal (1x1 or 2x2 blocks)
```

`lu` may be a permuted lower-triangular factor; `d` is block diagonal. The signs of the entries of `D` tell you how many positive and negative eigenvalues `A` has (Sylvester's law of inertia).

## 3.7 Banded Cholesky (preview)

For banded SPD matrices (tridiagonal stiffness matrices, 1D diffusion) `cholesky_banded` and `solveh_banded` work in `O(n)` time. Phase C covers them.

## Lesson B3 Exercises

1. Build an SPD matrix `A = B.T @ B + 0.1 * np.eye(n)` for `n = 5` and verify `L @ L.T` reproduces it.
2. Produce 50,000 samples of height and weight with means `[170, 70]`, standard deviations `[10, 12]` and correlation `0.6`. Verify the sample correlation.
3. Find three different 2x2 symmetric matrices: one SPD, one indefinite, one negative definite. Test each with `is_spd` and with `eigvalsh`.
4. Compute the log-likelihood of a 3D Gaussian sample at a point using only Cholesky (no `inv`, no `det`).
5. Use `ldl` on a 4x4 symmetric indefinite matrix and count positive and negative entries of `D`. Compare to the eigenvalue signs.

---

# Lesson B4: QR Decomposition

## 4.1 The idea

**A = Q R**

- `Q` has **orthonormal columns**: `Qᵀ Q = I`. (Square `Q` is an orthogonal matrix, a rotation or reflection.)
- `R` is upper triangular.

Why orthogonal matrices are wonderful:

- `Q⁻¹ = Qᵀ`: inverting is free.
- They preserve lengths and angles: `||Q x|| = ||x||`.
- `cond(Q) = 1`: they never amplify errors.

```python
A = np.array([[1., 1.],
              [1., 2.],
              [1., 3.]])                      # tall: 3 x 2

Q, R = linalg.qr(A, mode="economic")
print(Q.shape, R.shape)                        # (3, 2) (2, 2)
print(np.allclose(Q.T @ Q, np.eye(2)))         # True
print(np.allclose(Q @ R, A))                   # True
```

`mode` options:

| mode | Result |
|---|---|
| `"full"` (default) | `Q` is `m x m`, `R` is `m x n` |
| `"economic"` | `Q` is `m x n`, `R` is `n x n` (what you usually want for tall matrices) |
| `"r"` | only `R` |
| `"raw"` | internal LAPACK form |

The columns of `Q` form an **orthonormal basis** for the column space of `A`. QR is Gram-Schmidt, done in a numerically stable way.

## 4.2 Gram-Schmidt, and why it is not enough

**Gram-Schmidt:** take the columns of `A` one at a time, subtract the components along earlier directions, normalize.

```python
def gram_schmidt(A, modified=False):
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    for j in range(n):
        v = A[:, j].copy()
        for i in range(j):
            R[i, j] = Q[:, i] @ (v if modified else A[:, j])
            v -= R[i, j] * Q[:, i]
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j]
    return Q, R
```

On a well-behaved matrix, all versions give the same result. On a **nearly dependent** matrix, they differ massively:

```python
A = linalg.hilbert(12)[:, :8]                 # 12 x 8, columns almost dependent
print("cond:", np.linalg.cond(A))

for name, (Q, R) in {
    "classical GS": gram_schmidt(A, modified=False),
    "modified GS ": gram_schmidt(A, modified=True),
    "Householder ": linalg.qr(A, mode="economic"),
}.items():
    loss = np.linalg.norm(Q.T @ Q - np.eye(8))
    print(f"{name}  orthogonality error: {loss:.2e}")
```

Expect: classical Gram-Schmidt loses orthogonality badly, modified Gram-Schmidt is better but still depends on `cond`, and Householder (what `linalg.qr` uses) stays near `1e-15`.

## 4.3 Householder reflections (how real QR works)

A **Householder reflection** mirrors a vector across a hyperplane. One cleverly chosen reflection can zero out everything below the first entry of a column. Doing this column by column turns `A` into the triangular `R`, and the product of the reflections is `Q`.

Why it is stable: each step is an orthogonal transformation, which never amplifies rounding error. This is why QR is the workhorse of least squares.

## 4.4 QR for least squares (preview of Phase C)

For tall `A` and the problem `min ||A x - b||`: write `A = Q R` (economic). Then the minimizer solves

**R x = Qᵀ b**

```python
A = np.array([[1., 1.],
              [1., 2.],
              [1., 3.]])
b = np.array([1., 2., 2.])

Q, R = linalg.qr(A, mode="economic")
x = linalg.solve_triangular(R, Q.T @ b)
print(x)                                       # [0.6667 0.5]
print(linalg.lstsq(A, b)[0])                   # same
```

Compare with the **normal equations** `AᵀA x = Aᵀ b`: forming `AᵀA` **squares the condition number**, so QR is much more accurate when `A` is ill-conditioned.

```python
A = np.vander(np.linspace(0, 1, 40), 10)
print(np.linalg.cond(A), np.linalg.cond(A.T @ A))       # second is about the square of the first
```

## 4.5 Column pivoting: rank-revealing QR

```python
Q, R, p = linalg.qr(A, mode="economic", pivoting=True)
print(np.abs(np.diag(R)))                      # decreasing
```

With pivoting, columns are reordered (`A[:, p] = Q R`) so that `|R[0,0]| >= |R[1,1]| >= ...`. A sudden drop in the diagonal of `R` signals numerical rank deficiency, and the first `k` pivot columns are the most independent ones. This is used to pick independent sensors or variables.

## 4.6 Other useful routines

| Function | Purpose |
|---|---|
| `qr_multiply(A, c)` | Compute `Q @ c` without forming `Q` |
| `qr_update`, `qr_insert`, `qr_delete` | Update a QR when a row/column changes (online algorithms) |
| `rq(A)` | RQ decomposition (triangular times orthogonal), used in camera calibration |

## Lesson B4 Exercises

1. Verify that the columns of `Q` have length 1 and are mutually perpendicular for a random 10x4 matrix.
2. Solve a random 100x3 least squares problem three ways: normal equations, QR, `lstsq`. Compare residual norms and solution differences.
3. Build a 5x5 matrix whose last column is the sum of the first two. Run QR with pivoting and show the small last diagonal entry.
4. Show that `||Q x|| = ||x||` for random `x` and orthogonal `Q`.
5. Using QR, build an orthonormal basis for the plane spanned by `(1, 1, 0)` and `(0, 1, 1)`, and check orthogonality.

---

# Lesson B5: Eigenvalues and Eigenvectors

## 5.1 The idea

A matrix acts on vectors by rotating and stretching them. Most vectors change direction. **Eigenvectors** are the special directions that do not change: they only get stretched by a factor called the **eigenvalue**.

**A v = λ v**

```python
A = np.array([[2., 1.],
              [1., 2.]])

w, V = linalg.eig(A)
print(w)                     # [3.+0.j  1.+0.j]  (complex type even when values are real)
print(V)                     # eigenvectors as columns

for i in range(2):
    print(np.allclose(A @ V[:, i], w[i] * V[:, i]))       # True, True
```

Geometric view: the eigenvector `(1, 1)/√2` is stretched by 3; `(1, -1)/√2` is stretched by 1. Every other vector is a mix of the two.

## 5.2 Finding eigenvalues by hand (for understanding)

`A v = λ v` means `(A - λ I) v = 0` has a non-zero solution, so `det(A - λ I) = 0` (the **characteristic polynomial**).

For `[[2, 1], [1, 2]]`: `(2 - λ)² - 1 = 0`, so `λ = 1` or `λ = 3`.

**Never compute eigenvalues of large matrices through the polynomial.** It is numerically terrible. Real algorithms use QR iteration (Lesson B6).

Useful identities:

- `sum of eigenvalues = trace(A)`
- `product of eigenvalues = det(A)`

```python
print(np.isclose(np.sum(w).real, np.trace(A)), np.isclose(np.prod(w).real, linalg.det(A)))
```

## 5.3 Diagonalization and matrix powers

If `A` has a full set of independent eigenvectors, then

**A = V Λ V⁻¹**, with `Λ = diag(w)`.

Then `A^k = V Λ^k V⁻¹`: powers become trivial.

Example: the **Fibonacci matrix**.

```python
F = np.array([[1., 1.],
              [1., 0.]])
w, V = linalg.eigh(F)                                   # symmetric, so eigh
print(w)                                                # [-0.618, 1.618]  (golden ratio)
F10 = V @ np.diag(w**10) @ V.T
print(np.round(F10))                                    # [[89 55] [55 34]]
```

The entries are Fibonacci numbers `F11, F10, F9`. The golden ratio `1.618...` is the dominant eigenvalue, and it controls the growth rate.

## 5.4 `eig` versus `eigh`

| | `eig` | `eigh` |
|---|---|---|
| For | General square matrices | Symmetric (or Hermitian) matrices |
| Eigenvalues | May be complex | **Always real**, sorted ascending |
| Eigenvectors | Not necessarily orthogonal | **Orthonormal** |
| Speed and accuracy | Slower | Faster and more accurate |

```python
w, V = linalg.eigh(A)
print(w)                                               # [1. 3.]
print(np.allclose(V.T @ V, np.eye(2)))                 # True: orthonormal
print(np.allclose(V @ np.diag(w) @ V.T, A))            # True: A = V Λ Vᵀ (spectral theorem)
```

**The spectral theorem:** every symmetric real matrix has real eigenvalues and orthonormal eigenvectors. Use `eigh` whenever the matrix is symmetric. If a matrix is only *nearly* symmetric because of rounding, symmetrize it first: `A = (A + A.T) / 2`.

More functions:

| Function | Purpose |
|---|---|
| `eigvals(A)`, `eigvalsh(A)` | Eigenvalues only (faster) |
| `eig(A, left=True)` | Also left eigenvectors (`uᴴ A = λ uᴴ`) |
| `eigh(A, subset_by_index=[0, 2])` | Only the 3 smallest eigenpairs (big speedup) |
| `eigh(A, subset_by_value=[a, b])` | Only eigenvalues in `(a, b]` |
| `eig_banded`, `eigh_tridiagonal` | Banded and tridiagonal problems |

## 5.5 Complex eigenvalues = oscillation

```python
Rot = np.array([[0., -1.],
                [1.,  0.]])            # rotation by 90 degrees
print(linalg.eigvals(Rot))             # [0.+1.j  0.-1.j]
```

A rotation has no real direction that stays fixed, so the eigenvalues are complex. In dynamics, a complex pair `a ± bi` means **oscillation** with frequency `b` and growth/decay rate `a`.

## 5.6 Power iteration: the idea behind eigenvalue algorithms

Repeatedly multiply a random vector by `A` and normalize. It converges to the eigenvector of the **largest** eigenvalue (in absolute value).

```python
def power_iteration(A, iters=200, seed=0):
    rng = np.random.default_rng(seed)
    v = rng.standard_normal(A.shape[0])
    v /= np.linalg.norm(v)
    for _ in range(iters):
        w = A @ v
        v = w / np.linalg.norm(w)
    return v @ A @ v, v                     # Rayleigh quotient, eigenvector

lam, v = power_iteration(np.array([[2., 1.], [1., 2.]]))
print(lam)                                  # 3.0
```

The **Rayleigh quotient** `vᵀ A v / vᵀ v` gives an excellent eigenvalue estimate even from a rough vector. This is the seed of the algorithms used for huge sparse matrices (Module 3) and for Google's PageRank.

## 5.7 Markov chains and steady states

A transition matrix `P` (rows sum to 1) describes probabilities of moving between states. The long-run distribution `π` satisfies `π P = π`: a **left eigenvector** with eigenvalue 1.

```python
P = np.array([[0.9, 0.1],
              [0.5, 0.5]])
w, vl = linalg.eig(P, left=True, right=False)
i = np.argmin(np.abs(w - 1))
pi = np.real(vl[:, i])
pi = pi / pi.sum()
print(pi)                                   # [0.8333 0.1667]
```

The system spends 5/6 of the time in state 0.

## 5.8 Stability of linear dynamical systems

For `x' = A x` (continuous time): stable if **all eigenvalues have negative real part**.
For `x[k+1] = A x[k]` (discrete time): stable if **all eigenvalues satisfy `|λ| < 1`**.

```python
A = np.array([[0., 1.],
              [-4., -0.5]])                 # mass-spring-damper
w = linalg.eigvals(A)
print(w)                                     # -0.25 ± 1.98i: stable and oscillating
print("stable:", np.all(w.real < 0))
```

Frequency: `|Im(λ)| = 1.98 rad/s`; decay rate `0.25 1/s`.

## 5.9 Advanced warning: non-normal matrices

A matrix is **normal** if it commutes with its transpose (symmetric matrices are normal). For non-normal matrices, eigenvalues do **not** tell the whole story. A system can have all eigenvalues in the stable region and still grow hugely before decaying.

```python
A = np.array([[-1., 10.],
              [ 0., -2.]])
print(linalg.eigvals(A))                    # [-1. -2.]: stable

x0 = np.array([0., 1.])
peak = max(np.linalg.norm(linalg.expm(A * t) @ x0) for t in np.linspace(0, 5, 500))
print(peak)                                  # about 2.5, even though the final state is 0
```

The state grows to 2.5 times its initial size before decaying. Real examples: fluid flow transitions, aircraft control, structures with strong coupling. Lessons: check `cond(V)` for the eigenvector matrix, and prefer SVD-based and Schur-based analysis for non-normal problems.

**Defective matrices:** some matrices lack a full set of eigenvectors.

```python
J = np.array([[1., 1.],
              [0., 1.]])
w, V = linalg.eig(J)
print(w)                                     # [1. 1.]
print(V)                                     # two almost parallel columns
print(np.linalg.cond(V))                     # astronomically large
```

Diagonalization `V Λ V⁻¹` fails here. Use the Schur decomposition instead (Lesson B6).

## 5.10 The generalized eigenproblem (vibrations)

Mechanical systems lead to **K v = λ M v**, with `K` the stiffness matrix, `M` the mass matrix, and `λ = ω²`.

```python
w, V = linalg.eigh(K, M)                     # K symmetric, M symmetric positive definite
omega = np.sqrt(w)                            # natural frequencies in rad/s
f = omega / (2 * np.pi)                       # Hz
```

SciPy normalizes the modes so that **`Vᵀ M V = I`** (mass-normalized) and `Vᵀ K V = diag(ω²)`.

### Physical meaning

- Each **mode** is a pattern in which all parts oscillate at the same frequency.
- Any motion is a **sum** of modes (modal superposition).
- The lowest modes dominate most real responses, so engineers often keep only a few.

## 5.11 Practical lab: three-mass chain

```python
k, m = 1000.0, 2.0
K = k * np.array([[ 2., -1.,  0.],
                  [-1.,  2., -1.],
                  [ 0., -1.,  2.]])
M = m * np.eye(3)

w, V = linalg.eigh(K, M)
omega = np.sqrt(w)
print("omega (rad/s):", omega)               # about [17.11 31.62 41.32]
print("freq (Hz)    :", omega / (2*np.pi))   # about [2.72 5.03 6.58]
print(np.allclose(V.T @ M @ V, np.eye(3)))   # True: mass-normalized
print(np.allclose(V.T @ K @ V, np.diag(w)))  # True
```

Mode shapes (signs may flip, which is fine):

- Mode 1: all masses in phase, shape about `(1, √2, 1)`.
- Mode 2: outer masses opposite, middle one still.
- Mode 3: neighbours opposite (fastest, "zig-zag").

### Modal superposition: simulate free vibration

Initial displacement `x0` and zero initial velocity: `x(t) = V diag(cos ωt) Vᵀ M x0`.

```python
x0 = np.array([0.01, 0.0, 0.0])               # pull the first mass 1 cm
t = 0.05
x_modal = V @ (np.cos(omega * t) * (V.T @ M @ x0))

# cross-check with the matrix exponential of the first-order system
N = 3
Minv_K = linalg.solve(M, K)
A_state = np.block([[np.zeros((N, N)), np.eye(N)],
                    [-Minv_K,           np.zeros((N, N))]])
state = linalg.expm(A_state * t) @ np.concatenate([x0, np.zeros(N)])
print(np.allclose(x_modal, state[:N]))        # True
```

Two completely different methods agree: a great validation habit.

## 5.12 Big problems: tridiagonal eigenproblems

For an `N`-mass chain, `K` is tridiagonal. Use `eigh_tridiagonal(d, e)` (main diagonal `d`, off-diagonal `e`):

```python
N = 2000
d = 2.0 * np.ones(N)
e = -1.0 * np.ones(N - 1)
w = linalg.eigh_tridiagonal(d, e, eigvals_only=True)

# exact eigenvalues: 2 - 2 cos(j pi / (N + 1))
j = np.arange(1, N + 1)
exact = 2 - 2 * np.cos(j * np.pi / (N + 1))
print(np.allclose(w, exact))                  # True
```

A dense `eigh` on 2000x2000 is much slower, and 20000x20000 is not even possible in memory.

## Lesson B5 Exercises

1. Verify `A v = λ v` for every eigenpair of a random symmetric 4x4 matrix, and that `V.T @ V = I`.
2. Use `power_iteration` on a random symmetric positive matrix and compare with `eigh`. Why does convergence slow down when the top two eigenvalues are close?
3. Compute `A^20` for `A = [[0.5, 0.5], [0.2, 0.8]]` with eigendecomposition and with `np.linalg.matrix_power`. What does the limit look like?
4. Find the natural frequencies of a 5-mass chain with unequal masses `[1, 2, 1, 3, 1]` kg and identical springs.
5. For which values of the damping `c` does `x'' + c x' + 4 x = 0` oscillate? Use eigenvalues of the first-order system for `c = 0.5, 2, 4, 6`.
6. Show numerically that the Fibonacci number `F30` equals `round(phi^30 / sqrt(5))`.

---

# Lesson B6: Schur and Hessenberg Forms (Advanced)

## 6.1 Why a new decomposition?

Diagonalization fails for defective matrices and is unstable for non-normal ones. The **Schur decomposition** always exists and is always numerically safe:

**A = Z T Zᴴ**

- `Z` is **unitary/orthogonal** (perfectly conditioned).
- `T` is **upper triangular** (complex Schur) or **quasi-triangular** with 1x1 and 2x2 blocks (real Schur).
- The eigenvalues of `A` are the diagonal entries (or eigenvalues of the 2x2 blocks) of `T`.

```python
A = np.array([[1., 2., 3.],
              [4., 5., 6.],
              [7., 8., 10.]])

T, Z = linalg.schur(A)                        # real Schur
print(np.round(T, 3))
print(np.allclose(Z @ T @ Z.T, A))            # True
print(np.allclose(Z.T @ Z, np.eye(3)))        # True

Tc, Zc = linalg.schur(A, output="complex")    # complex Schur: truly triangular
print(np.allclose(Zc @ Tc @ Zc.conj().T, A))  # True
```

For a symmetric matrix, `T` is diagonal, so Schur reduces to the spectral decomposition.

## 6.2 How eigenvalues are really computed

Practical eigenvalue software follows these steps:

1. **Hessenberg reduction:** orthogonally reduce `A` to **upper Hessenberg** form `H` (zeros below the first subdiagonal). `linalg.hessenberg(A)`.
2. **QR iteration:** repeatedly factor `H = Q R` and form `R Q`. This converges to the Schur form `T`.
3. **Eigenvectors** are obtained by back-substitution on `T`.

```python
H, Q = linalg.hessenberg(A, calc_q=True)
print(np.round(H, 3))                          # zeros below the first subdiagonal
print(np.allclose(Q @ H @ Q.T, A))             # True
```

This is why eigenvalue algorithms cost about `O(n³)` with a large constant (10 to 25 times LU).

## 6.3 Where Schur is used

- **Matrix functions** (`expm`, `sqrtm`, `logm`, `funm`) are computed through Schur forms.
- **Control theory:** solving Lyapunov, Sylvester and Riccati equations (Phase C).
- **Stability analysis** of non-normal systems.
- **Generalized problems:** `linalg.qz(A, B)` is the generalized Schur (used for `A v = λ B v` when `B` is not positive definite).

You will rarely call `schur` directly, but understanding it explains why SciPy's high-level functions are reliable.

## Lesson B6 Exercises

1. Compute the real Schur form of a random 5x5 matrix. Identify which blocks are 2x2 and confirm they correspond to complex eigenvalues from `eigvals`.
2. Verify that the diagonal of the complex Schur factor `T` equals the eigenvalues (as sets).
3. Reduce a random 6x6 symmetric matrix to Hessenberg form. What shape does `H` take, and why?

---

# Lesson B7: Singular Value Decomposition (SVD)

The most useful matrix factorization in all of applied mathematics.

## 7.1 The idea

Every matrix, of **any shape**, can be written

**A = U Σ Vᵀ**

- `U` and `V` have orthonormal columns.
- `Σ` is diagonal with **singular values** `σ₁ ≥ σ₂ ≥ ... ≥ 0`.

Geometric meaning: a matrix maps the unit sphere to an ellipsoid. The **semi-axes** of the ellipsoid have lengths `σ₁, σ₂, ...`. The columns of `V` are the input directions that get stretched, and the columns of `U` are the output directions.

```python
A = np.array([[3.,  2.,  2.],
              [2.,  3., -2.]])

U, s, Vh = linalg.svd(A)
print(s)                                      # [5. 3.]
print(U.shape, Vh.shape)                      # (2, 2) (3, 3)
```

`s` is returned as a 1D array. `Vh` is `Vᵀ` (already transposed).

## 7.2 Full vs compact SVD

```python
U, s, Vh = linalg.svd(A, full_matrices=False)       # compact (economy) SVD
print(U.shape, s.shape, Vh.shape)                    # (2, 2) (2,) (2, 3)

print(np.allclose(U @ np.diag(s) @ Vh, A))           # True
```

Always use `full_matrices=False` unless you specifically need the extra basis vectors (they span null spaces). For a tall 10000 x 5 matrix, the full `U` would be 10000 x 10000.

Helpers:

```python
s_only = linalg.svdvals(A)                    # singular values only (faster)
Sigma = linalg.diagsvd(s, 2, 3)               # build the m x n Sigma matrix
```

## 7.3 Where singular values come from

`Aᵀ A = V Σ² Vᵀ`, so the singular values are the **square roots of the eigenvalues of `AᵀA`**:

```python
w = linalg.eigvalsh(A.T @ A)[::-1]            # descending
print(np.sqrt(np.clip(w, 0, None))[:2])       # [5. 3.]
```

Never compute SVD this way for ill-conditioned matrices: forming `AᵀA` squares the condition number and loses small singular values. Use `svd` directly.

## 7.4 What singular values tell you

| Quantity | From the SVD |
|---|---|
| **2-norm** `||A||₂` | `s[0]` |
| **Frobenius norm** | `sqrt(sum(s**2))` |
| **Nuclear norm** | `sum(s)` |
| **Condition number** | `s[0] / s[-1]` |
| **Rank** | number of `s[i] > tol` |
| **Distance to the nearest singular matrix** | `s[-1]` |

Numerical rank tolerance (the same default as `np.linalg.matrix_rank`):

```python
tol = s.max() * max(A.shape) * np.finfo(s.dtype).eps
rank = np.sum(s > tol)
```

```python
print(np.isclose(s[0], linalg.norm(A, 2)))                      # True
print(np.isclose(np.sqrt(np.sum(s**2)), linalg.norm(A)))        # True
```

## 7.5 The four fundamental subspaces

For a matrix of rank `r`:

| Subspace | Basis from SVD |
|---|---|
| Column space (range) | first `r` columns of `U` |
| Left null space | remaining columns of `U` |
| Row space | first `r` rows of `Vᵀ` |
| Null space | remaining rows of `Vᵀ` |

SciPy shortcuts:

```python
A = np.array([[1., 2., 3.],
              [4., 5., 6.],
              [7., 8., 9.]])                  # rank 2

print(np.linalg.matrix_rank(A))               # 2
N = linalg.null_space(A)                      # vectors x with A x = 0
print(N.shape, np.allclose(A @ N, 0))         # (3, 1) True
R = linalg.orth(A)                            # orthonormal basis of the column space
print(R.shape)                                # (3, 2)
```

The null space tells you which input combinations are invisible. For a mechanical model, null-space vectors are **rigid-body motions** (a structure with free supports) or **mechanisms**. For a robot Jacobian, they are the **self-motions** that do not move the end effector.

## 7.6 Low-rank approximation (Eckart-Young theorem)

Keep only the `k` largest singular values:

**A_k = U[:, :k] diag(s[:k]) Vᵀ[:k, :]**

This is the **best** possible rank-`k` approximation, and the error is known exactly:

- `||A - A_k||₂ = s[k]` (the next singular value)
- `||A - A_k||_F = sqrt(s[k]² + s[k+1]² + ...)`

```python
rng = np.random.default_rng(0)
A = rng.standard_normal((50, 30))
U, s, Vh = linalg.svd(A, full_matrices=False)
k = 5
Ak = U[:, :k] @ np.diag(s[:k]) @ Vh[:k]

print(np.isclose(linalg.norm(A - Ak, 2), s[k]))                         # True
print(np.isclose(linalg.norm(A - Ak), np.sqrt(np.sum(s[k:]**2))))       # True
```

This is the mathematical heart of image compression, PCA, recommender systems and noise reduction (Phase C).

## 7.7 The pseudo-inverse

For any matrix, `A⁺ = V Σ⁺ Uᵀ`, where `Σ⁺` inverts the non-zero singular values and leaves zeros alone.

```python
A = np.array([[1., 2.],
              [3., 4.],
              [5., 6.]])
Ap = linalg.pinv(A)
print(Ap.shape)                                # (2, 3)
print(np.allclose(Ap, np.linalg.inv(A.T @ A) @ A.T))     # True for full-column-rank A
```

`pinv` gives the least squares solution (and the minimum-norm one when the system is underdetermined). More in Phase C.

## 7.8 Polar decomposition: nearest rotation

Every square matrix factors as **A = R P**: `R` is orthogonal (a rotation or reflection) and `P` is symmetric positive semi-definite (a pure stretch).

```python
A_square = np.array([[2., 1.],
                     [0., 3.]])
R, P = linalg.polar(A_square)       # A_square = R @ P
print(np.allclose(R @ P, A_square))            # True
print(np.allclose(R.T @ R, np.eye(2)))         # True: R is orthogonal
print(np.allclose(P, P.T))                      # True: P is symmetric
```

Practical use: **cleaning up a rotation matrix** that drifted from orthogonality because of rounding or noise. The nearest orthogonal matrix is the polar factor.

```python
theta = 0.7
R_true = np.array([[np.cos(theta), -np.sin(theta)],
                   [np.sin(theta),  np.cos(theta)]])
rng = np.random.default_rng(0)
R_noisy = R_true + 0.01 * rng.standard_normal((2, 2))

R_clean, _ = linalg.polar(R_noisy)
print(np.linalg.norm(R_noisy.T @ R_noisy - np.eye(2)))          # small but not zero
print(np.linalg.norm(R_clean.T @ R_clean - np.eye(2)))          # about 1e-16
print(np.linalg.norm(R_clean - R_true))                          # close to the true rotation
```

Used constantly in robotics, animation and computer graphics when integrating rotations.

## 7.9 Subspace angles

How far apart are two subspaces? `subspace_angles(A, B)` returns the principal angles (in radians).

```python
xy_plane = np.array([[1., 0.], [0., 1.], [0., 0.]])
xz_plane = np.array([[1., 0.], [0., 0.], [0., 1.]])
print(linalg.subspace_angles(xy_plane, xz_plane))      # [1.5708 0.]  -> 90 degrees and 0 degrees
```

The planes share the x-axis (angle 0) and are perpendicular otherwise (angle 90 degrees). Used to compare PCA subspaces, check sensor alignment and compare mode shapes of different models.

## 7.10 SVD for conditioning, noise and rank decisions

The **singular value spectrum** tells a story. Plot it on a log axis:

```python
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
low_rank = rng.standard_normal((100, 4)) @ rng.standard_normal((4, 60))   # hidden rank 4
noisy = low_rank + 0.05 * rng.standard_normal((100, 60))

s = linalg.svdvals(noisy)
plt.semilogy(s, "o-")
plt.xlabel("index")
plt.ylabel("singular value")
plt.title("A clear gap after index 4 reveals the true rank")
plt.show()
```

A big **gap** separates signal from noise. This is how engineers decide how many modes or components matter.

## 7.11 LAPACK drivers

```python
U, s, Vh = linalg.svd(A, lapack_driver="gesdd")      # default: fast divide and conquer
U, s, Vh = linalg.svd(A, lapack_driver="gesvd")      # slower but sometimes more robust
```

If `gesdd` ever fails to converge, `gesvd` is the fallback.

## Lesson B7 Exercises

1. For a random 6x4 matrix verify `s[0] == linalg.norm(A, 2)`, `s[0]/s[-1] == np.linalg.cond(A)`, and `sqrt(sum(s²)) == linalg.norm(A)`.
2. Build a 5x5 matrix with two identical columns. Predict its rank, then check with SVD, QR with pivoting and `null_space`.
3. For a 40x25 matrix with a hidden rank of 3 plus small noise, find the rank from the gap and reconstruct the noise-free matrix. How close is the rank-3 approximation to the hidden matrix?
4. Show that `pinv(A) @ A` is the identity for a tall full-rank `A` but `A @ pinv(A)` is not.
5. Compute the polar decomposition of `[[2, 0], [0, -3]]`. Is `R` a rotation or a reflection?
6. Compute the angle between two random 2D subspaces of 5D space with `subspace_angles`.

---

# Lesson B8: Choosing the Right Decomposition

## 8.1 Decision table

| Your problem | Best tool | Why |
|---|---|---|
| Solve `A x = b`, general square `A` | `solve`, or `lu_factor` + `lu_solve` | LU is the standard |
| Solve many systems with the same `A` | `lu_factor` + `lu_solve` or `cho_factor` + `cho_solve` | Factor once |
| `A` symmetric positive definite | Cholesky | Twice as fast, stable, no pivoting |
| `A` symmetric indefinite | `ldl` | Handles saddle points |
| Least squares, full rank | QR | Stable, cheap |
| Least squares, possibly rank-deficient | SVD (`lstsq`, `pinv`) | Handles near-dependence |
| Rank, null space, conditioning | SVD | Exact picture |
| Eigenvalues of symmetric `A` | `eigh` | Fast, orthonormal |
| Eigenvalues of general `A` | `eig`, or Schur for non-normal | |
| Vibration modes `K v = λ M v` | `eigh(K, M)` | Mass-normalized modes |
| Tridiagonal or banded eigenproblem | `eigh_tridiagonal`, `eig_banded` | `O(n)` memory |
| Matrix functions | Schur-based (`expm`, `funm`) | Stable |
| Clean up a rotation | `polar` | Nearest orthogonal matrix |

## 8.2 Cost summary (square n x n, with vectors where relevant)

| Method | Rough relative cost | Stability |
|---|---|---|
| Cholesky | 1x | Excellent (SPD only) |
| LU with pivoting | 2x | Very good |
| QR | 4x | Excellent |
| `eigh` | about 10x | Excellent |
| `eig` | about 25x | Good (watch non-normality) |
| SVD | about 20x | Excellent |

(The numbers are rough multiples of the cost of Cholesky. Real timings depend on the library and hardware, so measure.)

## 8.3 Golden rules

1. **Use the structure you know.** Symmetric: `eigh`, `cholesky`. Triangular: `solve_triangular`. Banded: banded routines.
2. **Never form `AᵀA` unless you must.** It squares the condition number.
3. **Prefer orthogonal methods (QR, SVD) when accuracy matters more than speed.**
4. **Factor once, solve many times.**
5. **Verify every decomposition by reconstruction:** `np.allclose(A, P @ L @ U)` and so on.

---

# Labs

## Lab B1: Prove your LU is right

1. Run `lu_scratch` on 100 random matrices of sizes 3 to 50.
2. For each, compute `max|P A - L U|`, and compare your `L`, `U` to SciPy's (remember `P_scipy = P.T`).
3. Test on tricky inputs: a matrix with a zero top-left entry, a Hilbert matrix, a nearly singular matrix. Report which cases make the reconstruction error larger and why.
4. Add the solver: write `solve_via_lu(A, b)` using your own forward and back substitution, and compare with `linalg.solve`.

## Lab B2: Decomposition showdown

Build an SPD matrix `A = B.T @ B + n * np.eye(n)` with `n = 1500` and time:

| Method | Code |
|---|---|
| General solve | `linalg.solve(A, b)` |
| SPD solve | `linalg.solve(A, b, assume_a="pos")` |
| Cholesky | `cho_factor` then `cho_solve` |
| LU | `lu_factor` then `lu_solve` |
| QR | `Q, R = linalg.qr(A); solve_triangular(R, Q.T @ b)` |
| SVD | `U, s, Vh = linalg.svd(A); Vh.T @ ((U.T @ b) / s)` |
| Explicit inverse | `linalg.inv(A) @ b` |

Record time and residual norm in a table. Then repeat the factor-based methods with 200 right-hand sides to see where "factor once" wins big. Write two sentences on what you conclude.

## Lab B3: Vibration modes of a beam-like chain with unequal masses

```python
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

N = 6
k = 5000.0                                         # N/m
masses = np.array([1.0, 2.0, 1.5, 1.0, 3.0, 1.0])  # kg
K = k * (2*np.eye(N) - np.eye(N, k=1) - np.eye(N, k=-1))
M = np.diag(masses)

w, V = linalg.eigh(K, M)
freqs = np.sqrt(w) / (2*np.pi)
print("natural frequencies (Hz):", np.round(freqs, 2))

x = np.arange(1, N + 1)
fig, axes = plt.subplots(2, 3, figsize=(11, 6), sharex=True)
for j, ax in enumerate(axes.ravel()):
    ax.plot(x, V[:, j], "o-")
    ax.axhline(0, color="gray", lw=0.5)
    ax.set_title(f"Mode {j+1}: {freqs[j]:.2f} Hz")
plt.tight_layout()
plt.show()
```

Questions to answer:

1. How many sign changes does mode `j` have? (There is a pattern.)
2. What changes if you double the heaviest mass? Which frequencies move most?
3. Check mass-orthogonality: `V.T @ M @ V = I`.
4. Simulate the response to an initial displacement of the first mass and compare the modal method with `expm`.
5. Keep only the lowest 2 modes and measure the error in the displacement at `t = 0.1 s`.

## Lab B4: Principal stresses (mechanical engineering)

A stress state at a point is a symmetric 3x3 tensor (MPa).

```python
import numpy as np
from scipy import linalg

sigma = np.array([[80., 30., 20.],
                  [30., 20., 10.],
                  [20., 10., 40.]])

vals, vecs = linalg.eigh(sigma)             # ascending
s3, s2, s1 = vals                            # s1 >= s2 >= s3 (principal stresses)
print("principal stresses (MPa):", s1, s2, s3)
print("principal directions (columns of vecs):\n", vecs)

tau_max = (s1 - s3) / 2
von_mises = np.sqrt(0.5 * ((s1 - s2)**2 + (s2 - s3)**2 + (s3 - s1)**2))
print("max shear:", tau_max, "von Mises:", von_mises)

# validation: invariants
print(np.isclose(vals.sum(), np.trace(sigma)))                 # first invariant
print(np.isclose(np.prod(vals), linalg.det(sigma)))            # third invariant
```

Extension: compute the von Mises stress directly from the tensor components and show it agrees with the principal-stress version. Explain why principal stresses are invariant to the choice of axes.

## Lab B5: Rank detective

Generate `X = L @ R + noise` where `L` is 200x5 and `R` is 5x80, noise standard deviation `0.1`.

1. Plot the singular values on a log axis and read off the rank from the gap.
2. Compute the rank-5 approximation and show its error against the noise-free `L @ R` is smaller than the error of the noisy `X`.
3. Repeat with noise `0.5, 1, 2` and find the noise level where the gap becomes unreadable.
4. Compare `np.linalg.matrix_rank(X)` (which has no idea about noise) with your gap-based rank.

---

# Exercise Hints

**B1.** `det` of a triangular matrix is the product of its diagonal. For `X @ P`, columns get shuffled.

**B2.** A zero at `[0, 0]` makes unpivoted elimination divide by zero. `np.argmax` on the column fixes it. For timing, expect the block solve to win clearly over the loop.

**B3.** `1.` Cholesky of an SPD matrix always succeeds. `2.` Build `Sigma` from standard deviations and correlation: `Sigma = D @ Corr @ D`.

**B4.** `2.` Use `qr` for the least squares problem and compare with `lstsq`; residuals should match to about `1e-15`. `3.` The last diagonal entry of `R` should be near zero.

**B5.** `2.` Convergence factor is `|λ₂ / λ₁|`: when close to 1, convergence is slow. `3.` The limit is the stationary distribution repeated in each row. `5.` Characteristic roots are `(-c ± sqrt(c² - 16)) / 2`: oscillation when `c < 4`. `6.` Binet formula with `phi = (1 + sqrt(5)) / 2`.

**B6.** The 2x2 blocks in real Schur form correspond to complex conjugate eigenvalue pairs.

**B7.** `4.` `pinv(A) @ A` is `n x n` identity; `A @ pinv(A)` is the projection onto the column space (rank `n`, size `m x m`). `5.` For a diagonal matrix with a negative entry, `R = diag(1, -1)`, a reflection (determinant `-1`).

---

# Common Mistakes

| Mistake | Fix |
|---|---|
| Forgetting `cholesky` returns the **upper** factor by default | Pass `lower=True`, or write `A = U.T @ U` |
| Using `eig` on a symmetric matrix | Use `eigh` (real, ordered, orthonormal) |
| Treating `Vh` as `V` | `svd` returns `Vᵀ`; `A = U @ diag(s) @ Vh` |
| Using the full SVD on tall matrices | `full_matrices=False` |
| Computing singular values via `eig(AᵀA)` | Use `svd` or `svdvals` directly |
| Comparing eigenvector signs between runs | Signs are arbitrary; compare `|v|` or `v v^T` |
| Assuming eigenvalue order from `eig` | `eig` does not sort; use `np.argsort` |
| Calling `lu` and expecting `P @ A = L @ U` | SciPy gives `A = P @ L @ U` |
| Treating stable eigenvalues as a guarantee for non-normal `A` | Check transient growth and `cond(V)` |
| Using `inv` after factorization | Use `lu_solve`, `cho_solve` instead |

# Cheat Sheet

```python
P, L, U = linalg.lu(A)                      # A = P L U
lu, piv = linalg.lu_factor(A); x = linalg.lu_solve((lu, piv), b)

L = linalg.cholesky(A, lower=True)          # A = L L^T  (SPD)
c, low = linalg.cho_factor(A); x = linalg.cho_solve((c, low), b)
lu_, d, perm = linalg.ldl(A)                # symmetric indefinite

Q, R = linalg.qr(A, mode="economic")
Q, R, p = linalg.qr(A, mode="economic", pivoting=True)

w, V = linalg.eigh(A)                       # symmetric
w, V = linalg.eig(A)                        # general (complex)
w, V = linalg.eigh(K, M)                    # K v = λ M v
w = linalg.eigh_tridiagonal(d, e, eigvals_only=True)

T, Z = linalg.schur(A)                      # A = Z T Z^H
H, Q = linalg.hessenberg(A, calc_q=True)

U, s, Vh = linalg.svd(A, full_matrices=False)
linalg.null_space(A); linalg.orth(A); linalg.pinv(A)
R, P = linalg.polar(A)
linalg.subspace_angles(A, B)
```

---

# Phase B Checkpoint

You are ready for Phase C when you can honestly check every box:

- [ ] I can write LU with partial pivoting from scratch and explain why pivoting matters.
- [ ] I can explain "factor once, solve many" and show the speed gain.
- [ ] I know `cholesky` is upper by default, and I can use it as an SPD test, for log-determinants and for sampling.
- [ ] I understand why Householder QR beats Gram-Schmidt and why QR beats the normal equations.
- [ ] I can compute eigenpairs with `eigh`, `eig` and `eigh(K, M)`, and I know when to use each.
- [ ] I can compute natural frequencies and mode shapes and validate them by two methods.
- [ ] I know the non-normal trap (stable eigenvalues, large transient growth).
- [ ] I can explain the real Schur form and why it is used in practice.
- [ ] I can get rank, null space, condition number, pseudo-inverse and the best low-rank approximation from the SVD.
- [ ] I can clean up a rotation matrix with `polar`.
- [ ] I can choose the right decomposition from the decision table.

## Quick self-quiz (answers at the bottom)

1. Your matrix is symmetric positive definite and you must solve 1000 systems with it. Which factorization and which functions?
2. Why does `np.linalg.cond(A.T @ A)` tend to be about `cond(A)²`?
3. You call `linalg.cholesky(A)` and get a matrix with zeros **below** the diagonal. Why?
4. A matrix has singular values `[10, 3, 0.2, 1e-14]`. What is its numerical rank?
5. Eigenvalues of `x' = A x` are `-1` and `-2`. Can the state still grow temporarily?

**Answers:** (1) Cholesky: `cho_factor` once, `cho_solve` per right-hand side. (2) Because the singular values of `AᵀA` are the squares of those of `A`, so the ratio largest/smallest is squared. (3) It returns the **upper** factor by default (`A = Uᵀ U`); use `lower=True`. (4) 3 (the last value is at the rounding-noise level). (5) Yes, if `A` is non-normal.

---

# Suggested Repo Layout for This Phase

```
02-linear-algebra/phase-B-decompositions/
├── README.md
├── lessons/
│   ├── B1-triangular-and-permutation.md
│   ├── B2-lu.md
│   ├── B3-cholesky-ldl.md
│   ├── B4-qr.md
│   ├── B5-eigen.md
│   ├── B6-schur-hessenberg.md
│   ├── B7-svd.md
│   └── B8-choosing-decompositions.md
├── code/
│   ├── lu_scratch.py
│   ├── gram_schmidt.py
│   ├── power_iteration.py
│   └── is_spd.py
├── labs/
│   ├── lab_B1_lu_proof.py
│   ├── lab_B2_showdown.py
│   ├── lab_B3_vibration_modes.py
│   ├── lab_B4_principal_stresses.py
│   └── lab_B5_rank_detective.py
├── exercises/
└── tests/
    └── test_phase_B.py
```

**Next:** Phase C, Least Squares, Matrix Functions and Applications (`02C-applications.md`).
