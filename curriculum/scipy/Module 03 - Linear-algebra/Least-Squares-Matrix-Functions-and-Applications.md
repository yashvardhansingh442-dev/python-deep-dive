# Module 2, Phase C: Least Squares, Matrix Functions and Applications

> **Part of:** SciPy Course, Module 2 (Linear Algebra, `scipy.linalg`)
> **Level:** Beginner to Advanced
> **Time:** about 4 days
> **Prerequisites:** Phase A (solving, conditioning) and Phase B (LU, QR, Cholesky, eigen, SVD)

---

## What this phase is about

Phases A and B gave you the machinery. Phase C is where it becomes **useful**:

- **Data never fits exactly.** Real measurements have noise, so you fit models by **least squares**.
- **Robots, circuits and structures evolve in time.** The **matrix exponential** solves linear dynamics exactly and builds rotations.
- **Control and estimation** rest on special matrix equations (Lyapunov, Riccati).
- **Real problems are huge but structured.** Banded, Toeplitz and circulant systems are solved in a fraction of the time.
- **Applications:** image compression, PCA, plane fitting for 3D scans, rigid registration (Kabsch), system identification.

By the end of this phase you will be able to:

1. Derive and solve least squares problems three ways, and judge fit quality with residuals and error bars.
2. Prevent overfitting and ill-conditioning (orthogonal bases, ridge, truncated SVD, robust fitting).
3. Solve underdetermined problems, equality-constrained fits and robot inverse kinematics.
4. Compute and apply `expm`, `logm`, `sqrtm` for ODEs, discretization and rotation interpolation.
5. Solve Sylvester, Lyapunov and Riccati equations and design an LQR controller.
6. Solve banded, Toeplitz, circulant and Kronecker-structured systems efficiently.
7. Build five complete applications with validation.

## Roadmap

| Lesson | Topic | Level |
|---|---|---|
| C1 | Least squares foundations | Beginner to Intermediate |
| C2 | Fitting in practice: bases, weights, regularization, robust fits | Intermediate to Advanced |
| C3 | Underdetermined systems, pseudo-inverse, constraints, inverse kinematics | Intermediate to Advanced |
| C4 | Matrix functions: `expm`, `logm`, `sqrtm`, rotations, ODEs | Intermediate to Advanced |
| C5 | Matrix equations: Sylvester, Lyapunov, Riccati (LQR) | Advanced |
| C6 | Structured and banded systems | Intermediate to Advanced |
| C7 | Applications lab (five projects) | Practical |
| Capstone | Linear Algebra Lab | Practical |

Setup for every code block:

```python
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
```

---

# Lesson C1: Least Squares Foundations

## 1.1 The problem

You measured `m` data points but your model has only `n < m` unknowns. The equations `A x = b` are **overdetermined**: no exact solution exists because of noise. Instead, find the `x` that makes the **error as small as possible**:

**minimize ‖A x − b‖₂²**

Why squares? They are smooth (calculus works), they punish large errors, and they give a unique, easily computed answer. If errors are Gaussian, the least squares solution is also the **maximum likelihood** estimate.

## 1.2 The geometry

`A x` can only produce vectors in the **column space** of `A`. The measurement vector `b` usually sits outside it. The best we can do is the **orthogonal projection** of `b` onto the column space.

- The projection `b̂ = A x̂` is the closest reachable point.
- The **residual** `r = b − A x̂` points straight out of the column space, so it is **perpendicular to every column of A**:

**Aᵀ r = 0**

Substitute `r = b − A x̂`:

**AᵀA x̂ = Aᵀ b**   (the *normal equations*)

## 1.3 A worked example: fit a straight line

Data: `y ≈ c₀ + c₁ t`.

```python
t = np.array([0., 1., 2., 3., 4.])
y = np.array([1.1, 2.9, 5.2, 7.1, 8.8])

A = np.column_stack([np.ones_like(t), t])      # columns: constant and t
print(A)
```

Each row says: `c₀ · 1 + c₁ · t_i ≈ y_i`.

### Three ways to solve it

```python
# (1) normal equations: simple but squares the condition number
c_normal = linalg.solve(A.T @ A, A.T @ y, assume_a="pos")

# (2) QR: accurate and cheap
Q, R = linalg.qr(A, mode="economic")
c_qr = linalg.solve_triangular(R, Q.T @ y)

# (3) lstsq: SVD-based, handles rank deficiency
c_lstsq, residues, rank, sv = linalg.lstsq(A, y)

print(c_normal, c_qr, c_lstsq)       # all about [1.1  1.96]
print(residues)                       # [0.092]   sum of squared residuals
print(rank)                           # 2
print(sv)                             # singular values of A
```

Result: `y ≈ 1.10 + 1.96 t`.

### What `lstsq` returns

| Output | Meaning |
|---|---|
| `x` | the solution |
| `residues` | sum of squared residuals (empty array if `A` is rank-deficient or `m <= n`) |
| `rank` | effective rank of `A` |
| `s` | singular values of `A` |

### Check the geometry

```python
r = y - A @ c_lstsq
print(r)                              # [ 0.   -0.16  0.18  0.12 -0.14]
print(A.T @ r)                        # about [0, 0]: residual is perpendicular to columns
```

The residual sums to zero (because the model has a constant term) and is orthogonal to `t`. If your numbers do not satisfy `Aᵀ r ≈ 0`, something is wrong.

## 1.4 Three methods, one comparison

| Method | Idea | Cost | Accuracy | Use when |
|---|---|---|---|---|
| Normal equations | Solve `AᵀA x = Aᵀb` | Cheapest | Squares `cond(A)`, loses digits | Well-conditioned, quick tools |
| QR | `R x = Qᵀ b` | Moderate | Good | Default for full-rank problems |
| SVD (`lstsq`, `pinv`) | `x = V Σ⁻¹ Uᵀ b` | Most expensive | Best, handles rank deficiency | Ill-conditioned or unsure about rank |

`lstsq` can use different LAPACK drivers:

```python
x = linalg.lstsq(A, y, lapack_driver="gelsd")[0]     # default: SVD, divide and conquer
x = linalg.lstsq(A, y, lapack_driver="gelsy")[0]     # QR with pivoting: often fastest
x = linalg.lstsq(A, y, lapack_driver="gelss")[0]     # classic SVD
```

`lstsq` also has a small-singular-value cutoff argument (named `cond` in many versions, check your docs) that decides which singular values count as zero.

## 1.5 How good is the fit?

### Coefficient of determination R²

```python
fit = A @ c_lstsq
ss_res = np.sum((y - fit) ** 2)               # 0.092
ss_tot = np.sum((y - y.mean()) ** 2)          # 38.508
r2 = 1 - ss_res / ss_tot
print(r2)                                      # about 0.9976
```

`R² = 1` is a perfect fit and `0` is no better than guessing the mean. But `R²` **always increases** as you add parameters, so it cannot tell you whether the model is *right*.

### Residual analysis

Plot the residuals against `t`:

```python
plt.stem(t, r)
plt.axhline(0, color="gray")
plt.xlabel("t")
plt.ylabel("residual")
plt.show()
```

- **Random scatter around zero:** the model captures the structure.
- **A curve or trend:** the model is missing something (try adding a `t²` term).
- **Spread growing with `t`:** noise is not constant (use weighted least squares, Lesson C2).

### Uncertainty of the coefficients

If errors are independent with variance `σ²`, then `cov(x̂) = σ² (AᵀA)⁻¹`, where `σ² ≈ ss_res / (m − n)`. Compute `(AᵀA)⁻¹ = R⁻¹ R⁻ᵀ` from QR instead of forming `AᵀA`:

```python
m, n = A.shape
sigma2 = ss_res / (m - n)
Q, R = linalg.qr(A, mode="economic")
Rinv = linalg.solve_triangular(R, np.eye(n))
cov = sigma2 * (Rinv @ Rinv.T)
se = np.sqrt(np.diag(cov))
print("coefficients :", c_lstsq)              # [1.1  1.96]
print("std errors   :", se)                    # about [0.268 0.124]
```

Report fits as `c₁ = 1.96 ± 0.12`, never as a bare number. A coefficient whose standard error is larger than the coefficient itself is not distinguishable from zero.

## 1.6 When the equations are not independent

If columns of `A` are (nearly) dependent, `AᵀA` is (nearly) singular and the normal equations break. `lstsq` and SVD still return a sensible answer: the **minimum-norm** solution. More in Lesson C3.

## Lesson C1 Exercises

1. Fit `y = c₀ + c₁ t` to your own data (at least 8 points, add noise yourself). Solve it with all three methods and check they agree to `1e-10`.
2. Verify numerically that `Aᵀ r ≈ 0` and that the residual vector is shorter than the residual of any other line you try (try 20 random slopes and intercepts).
3. Fit a **line through the origin** (`y = c₁ t`, a one-column `A`). Derive the closed-form `c₁ = Σ t y / Σ t²` and check it.
4. Fit a **quadratic** `y = c₀ + c₁ t + c₂ t²` to data generated from `2 + 0.5 t − 0.1 t²` plus noise. Report coefficients with standard errors and check whether the true values fall inside about two standard errors.
5. Show with a small example that `R²` goes up when you add a useless random column to `A`.

---

# Lesson C2: Fitting in Practice

## 2.1 Any model that is linear in its coefficients

The model need not be a straight line. It only needs to be **linear in the unknown coefficients**; the basis functions may be anything.

```python
# y ≈ c0 + c1 sin(t) + c2 exp(-t)
A = np.column_stack([np.ones_like(t), np.sin(t), np.exp(-t)])
coef = linalg.lstsq(A, y)[0]
```

| Model | Columns of `A` |
|---|---|
| Polynomial of degree d | `1, t, t², ..., tᵈ` |
| Sinusoid with known frequency ω | `1, sin(ωt), cos(ωt)` |
| Exponential-decay mix with known rates | `exp(−λ₁t), exp(−λ₂t), ...` |
| Sensor calibration with temperature drift | `1, v, T, vT` |
| Plane `z = a x + b y + c` | `x, y, 1` |

A model like `y = a exp(b t)` is nonlinear in `b`. Take logs (`ln y = ln a + b t`, with caveats about noise) or use nonlinear fitting (`scipy.optimize`, Module 4).

## 2.2 The Vandermonde trap

For polynomial fitting, the obvious basis `1, t, t², ...` creates a **Vandermonde matrix**. Its columns look more and more alike for high degrees, so conditioning explodes.

```python
x = np.linspace(0, 1, 50)
for deg in (3, 6, 9, 12, 15):
    V = np.vander(x, deg + 1)
    print(deg, f"{np.linalg.cond(V):.1e}")
```

The condition number grows exponentially. Use an **orthogonal polynomial basis** (Chebyshev, Legendre) on a rescaled interval:

```python
deg = 15
V = np.vander(x, deg + 1)
C = np.polynomial.chebyshev.chebvander(2 * x - 1, deg)     # map [0,1] to [-1,1]
print(f"monomial: {np.linalg.cond(V):.1e}    Chebyshev: {np.linalg.cond(C):.1e}")
```

The Chebyshev basis stays well conditioned (single or double digits) at the same degree. Same model space, vastly better numerics. **Always rescale `x` to about `[-1, 1]` before polynomial fitting.**

## 2.3 Overfitting and model selection

More parameters always reduce the **training** error but may make predictions on new data worse.

```python
rng = np.random.default_rng(0)
x = np.sort(rng.uniform(0, 1, 60))
y = np.sin(2 * np.pi * x) + 0.2 * rng.standard_normal(60)

idx = rng.permutation(60)
train, test = idx[:40], idx[40:]

for deg in range(1, 16):
    A = np.polynomial.chebyshev.chebvander(2 * x - 1, deg)
    c = linalg.lstsq(A[train], y[train])[0]
    rmse = lambda i: np.sqrt(np.mean((A[i] @ c - y[i]) ** 2))
    print(f"degree {deg:2d}   train {rmse(train):.3f}   test {rmse(test):.3f}")
```

Pattern: the training error falls steadily; the test error falls, flattens near the noise level (0.2), and then rises. **Choose the degree where test error is lowest** (or use cross-validation). This train/test split idea is the foundation of all machine learning.

## 2.4 Weighted least squares

If some measurements are more reliable (smaller noise), they should count more. Multiply each row of `A` and `b` by the square root of its weight (weight is typically `1 / variance`):

```python
rng = np.random.default_rng(1)
t = np.linspace(0, 10, 40)
sigma = 0.1 + 0.1 * t                       # noise grows with t
y = 2.0 + 0.5 * t + sigma * rng.standard_normal(t.size)

A = np.column_stack([np.ones_like(t), t])
w = 1.0 / sigma**2
sw = np.sqrt(w)

c_ols = linalg.lstsq(A, y)[0]                          # ordinary
c_wls = linalg.lstsq(A * sw[:, None], y * sw)[0]       # weighted
print(c_ols, c_wls)                                    # both near [2.0 0.5], WLS usually closer
```

`A * sw[:, None]` scales row `i` by `sw[i]` (broadcasting from Module 0).

## 2.5 Regularization: taming ill-conditioned fits

When the problem is nearly rank-deficient (many correlated features, high-degree fits, few data points), coefficients become huge and wildly unstable, fitting the noise. **Regularization** adds a penalty on the size of the solution.

### Ridge regression (Tikhonov regularization)

**minimize ‖A x − b‖² + λ ‖x‖²**

Solve it as an ordinary least squares problem on an **augmented system**:

```python
def ridge(A, b, lam):
    n = A.shape[1]
    A_aug = np.vstack([A, np.sqrt(lam) * np.eye(n)])
    b_aug = np.concatenate([b, np.zeros(n)])
    return linalg.lstsq(A_aug, b_aug)[0]
```

Demonstration on an ill-conditioned fit:

```python
rng = np.random.default_rng(2)
x = np.linspace(0, 1, 25)
A = np.vander(x, 13)                                    # deliberately bad basis, degree 12
c_true = np.zeros(13); c_true[-3:] = [2.0, -1.0, 0.5]   # simple true polynomial
y = A @ c_true + 1e-3 * rng.standard_normal(25)

c_plain = linalg.lstsq(A, y)[0]
c_ridge = ridge(A, y, lam=1e-6)

print("cond(A)                :", f"{np.linalg.cond(A):.1e}")
print("‖coeffs‖ plain least sq:", np.linalg.norm(c_plain))     # large and unstable
print("‖coeffs‖ ridge         :", np.linalg.norm(c_ridge))     # modest
```

### What ridge does to singular values

With the SVD `A = U Σ Vᵀ`, the ridge solution is

**x_λ = Σᵢ [σᵢ / (σᵢ² + λ)] (uᵢᵀ b) vᵢ**

Compare with plain least squares, which uses `1/σᵢ`. Ridge multiplies each term by the **filter factor** `σᵢ² / (σᵢ² + λ)`: it leaves large singular values untouched (filter ≈ 1) and **suppresses small ones** (filter ≈ 0), which are the directions dominated by noise.

```python
def ridge_svd(A, b, lam):
    U, s, Vh = linalg.svd(A, full_matrices=False)
    return Vh.T @ ((s / (s**2 + lam)) * (U.T @ b))

print(np.allclose(ridge(A, y, 1e-6), ridge_svd(A, y, 1e-6)))     # True (to numerical tolerance)
```

This SVD form lets you try many `λ` values cheaply (the SVD is computed once).

### Truncated SVD

Instead of smoothly shrinking, simply **throw away** the small singular values:

```python
def tsvd_solve(A, b, k):
    U, s, Vh = linalg.svd(A, full_matrices=False)
    return Vh[:k].T @ ((U[:, :k].T @ b) / s[:k])
```

Choose `k` by looking at the gap in the singular value spectrum (Phase B7).

### Choosing λ

- **L-curve:** plot `‖x_λ‖` against the residual norm on log axes; pick the corner.
- **Cross-validation:** hold out data, choose the `λ` with the best prediction.
- **Discrepancy principle:** choose `λ` so the residual norm matches the known noise level.

Ridge, truncated SVD and Tikhonov regularization are the core of inverse problems, tomography, deblurring and nearly every machine-learning regression model.

## 2.6 Robust fitting: outliers

Ordinary least squares is **very sensitive to outliers**, because squaring a large error makes it dominate. Iteratively reweighted least squares (IRLS) down-weights points with large residuals:

```python
def robust_fit(A, y, iters=30, eps=1e-6):
    w = np.ones(len(y))
    for _ in range(iters):
        sw = np.sqrt(w)
        c = linalg.lstsq(A * sw[:, None], y * sw)[0]
        r = y - A @ c
        w = 1.0 / np.maximum(np.abs(r), eps)      # approximates least absolute deviations
    return c

rng = np.random.default_rng(3)
t = np.linspace(0, 10, 30)
y = 1.0 + 2.0 * t + 0.2 * rng.standard_normal(30)
y[[5, 20]] += 15.0                                  # two gross outliers
A = np.column_stack([np.ones_like(t), t])

print("ordinary:", linalg.lstsq(A, y)[0])           # pulled away from [1, 2]
print("robust  :", robust_fit(A, y))                # close to [1, 2]
```

For production use, look at `scipy.optimize.least_squares` with `loss="huber"` or `"soft_l1"` (Module 4).

## 2.7 Total least squares (advanced)

Ordinary least squares assumes only `b` is noisy. If the columns of `A` are noisy as well (errors-in-variables), **total least squares** minimizes the perpendicular-style error. The solution comes from the SVD of the augmented matrix `[A | b]`:

```python
def tls(A, b):
    Z = np.column_stack([A, b])
    _, _, Vh = linalg.svd(Z, full_matrices=False)
    v = Vh[-1]                                    # right singular vector of the smallest singular value
    return -v[:-1] / v[-1]

rng = np.random.default_rng(4)
x_true = np.linspace(0, 10, 50)
x_noisy = x_true + 0.3 * rng.standard_normal(50)      # noise in the input variable too
y_noisy = 2.0 * x_true + 0.3 * rng.standard_normal(50)

A = x_noisy.reshape(-1, 1)
print("OLS slope:", linalg.lstsq(A, y_noisy)[0])      # biased low (regression dilution)
print("TLS slope:", tls(A, y_noisy))                   # closer to 2
```

## Lesson C2 Exercises

1. Fit sensor data `V(T)` with the model `a + b T + c T²`. Rescale `T` first. Compare the condition number before and after scaling.
2. Plot train and test error versus polynomial degree for your own noisy dataset. Mark the best degree.
3. Reproduce the ridge demo and plot the coefficient norm against `λ` for `λ` from `1e-12` to `1`.
4. Implement the L-curve: for 40 values of `λ`, plot `‖A x_λ − b‖` against `‖x_λ‖` (log-log).
5. Add 10 percent outliers to a line-fit dataset. Compare ordinary, robust (IRLS) and weighted fits.
6. Fit `y = a sin(ωt) + b cos(ωt) + c` to a noisy sine of known frequency and recover the amplitude `sqrt(a² + b²)` and phase.
7. Show that TLS and OLS agree when there is no noise in `A`.

---

# Lesson C3: Underdetermined Systems, Pseudo-Inverse, Constraints and Inverse Kinematics

## 3.1 Fewer equations than unknowns

Now `A` is wide (`m < n`): infinitely many solutions fit exactly. Which one do we pick? The natural choice is the **minimum-norm** solution, the smallest `‖x‖` that satisfies `A x = b`.

```python
A = np.array([[1., 1., 1.]])
b = np.array([3.])

x = linalg.lstsq(A, b)[0]
print(x)                                    # [1. 1. 1.]
print(linalg.pinv(A) @ b)                   # [1. 1. 1.]
```

## 3.2 The pseudo-inverse

The **Moore-Penrose pseudo-inverse** `A⁺` generalizes the inverse to any matrix, using the SVD:

**A⁺ = V Σ⁺ Uᵀ**, where `Σ⁺` takes `1/σ` for non-zero singular values and `0` for the rest.

| Case | `A⁺ b` gives |
|---|---|
| Square, invertible | The ordinary solution |
| Tall, full column rank | The least squares solution (equals `(AᵀA)⁻¹ Aᵀ b`) |
| Wide, full row rank | The minimum-norm exact solution (equals `Aᵀ (A Aᵀ)⁻¹ b`) |
| Rank-deficient | The minimum-norm least squares solution |

Properties you can verify numerically:

```python
A = np.array([[1., 2.], [3., 4.], [5., 6.]])
Ap = linalg.pinv(A)
print(np.allclose(A @ Ap @ A, A))              # True
print(np.allclose(Ap @ A @ Ap, Ap))            # True
print(np.allclose((A @ Ap).T, A @ Ap))         # True: A A⁺ is a projection (symmetric)
print(np.allclose((Ap @ A).T, Ap @ A))         # True
```

These four equations uniquely define `A⁺`.

`pinv` treats tiny singular values as zero (the cutoff argument is named `rcond`, `cond` or `rtol` depending on your SciPy version, so check your docs). Choosing the cutoff is a modelling decision: set it relative to your data noise.

## 3.3 All solutions of an underdetermined system

Every solution is the minimum-norm solution **plus anything from the null space**:

**x = x_min + N z**   (any `z`)

```python
A = np.array([[1., 1.,  1.],
              [1., -1., 0.]])
b = np.array([3., 0.])

x_min = linalg.lstsq(A, b)[0]
N = linalg.null_space(A)

print(x_min)                                   # [1. 1. 1.]
print(N.ravel())                               # direction proportional to [1, 1, -2]
for z in (-1.0, 0.0, 2.0):
    x = x_min + N.ravel() * z
    print(np.allclose(A @ x, b), np.linalg.norm(x))     # always True; norm smallest at z = 0
```

The null space is the set of **free choices**. In engineering these are redundant degrees of freedom you can exploit (Section 3.6).

## 3.4 Equality-constrained least squares

Fit the data, but **force** some conditions to hold exactly (`C x = d`). Parametrize every feasible `x` through the null space of `C`:

```python
def constrained_lstsq(A, b, C, d):
    x0 = linalg.lstsq(C, d)[0]                # any particular solution of C x = d
    N = linalg.null_space(C)                  # free directions that keep C x = d
    z = linalg.lstsq(A @ N, b - A @ x0)[0]    # optimize over the free directions
    return x0 + N @ z

# fit y = c0 + c1 t, but force the line through the origin (c0 = 0)
t = np.array([1., 2., 3., 4.])
y = np.array([2.1, 3.9, 6.2, 7.8])
A = np.column_stack([np.ones_like(t), t])
C = np.array([[1., 0.]])
d = np.array([0.])

c = constrained_lstsq(A, y, C, d)
print(c)                                       # [0.   1.99]   (closed form: sum(t*y) / sum(t*t) = 59.7 / 30)
print(C @ c)                                    # [0.]: constraint satisfied exactly
```

Use cases: calibration with known anchor points, fits that must pass through a known origin, force-balance constraints, curve fitting with fixed end tangents.

## 3.5 Rank-deficient problems

Redundant measurements make `A` rank-deficient: the solution is not unique, but `lstsq` still returns one.

```python
A = np.array([[1., 2., 3.],
              [4., 5., 6.],
              [7., 8., 9.],
              [10., 11., 12.]])               # rank 2, even though 3 columns
b = np.array([1., 2., 3., 4.])

x, res, rank, s = linalg.lstsq(A, b)
print(rank)                                    # 2
print(s)                                       # last singular value about 0
```

Check `rank` before interpreting the coefficients: when rank is lower than the number of unknowns, some parameters simply cannot be determined from your data, and that is information, not a bug.

## 3.6 Robotics application: inverse kinematics with the Jacobian

A planar two-link arm has forward kinematics (joint angles to end-effector position):

```python
def fk(th, l1=1.0, l2=1.0):
    return np.array([l1 * np.cos(th[0]) + l2 * np.cos(th[0] + th[1]),
                     l1 * np.sin(th[0]) + l2 * np.sin(th[0] + th[1])])

def jac(th, l1=1.0, l2=1.0):
    s1, c1 = np.sin(th[0]), np.cos(th[0])
    s12, c12 = np.sin(th[0] + th[1]), np.cos(th[0] + th[1])
    return np.array([[-l1 * s1 - l2 * s12, -l2 * s12],
                     [ l1 * c1 + l2 * c12,  l2 * c12]])
```

The **Jacobian** `J` relates small joint changes to small end-effector motions: `dx ≈ J dθ`. **Inverse kinematics** asks for the joint angles that reach a target, solved by repeated linearization:

**Δθ = J⁺ e**, where `e = target − fk(θ)`

Near **singularities** (arm fully stretched or folded), `J` loses rank and `J⁺` explodes. **Damped least squares** fixes this by regularizing, which is ridge regression again:

**Δθ = Jᵀ (J Jᵀ + λ² I)⁻¹ e**

```python
def ik_dls(target, th0, lam=0.1, iters=300, tol=1e-6):
    th = np.array(th0, dtype=float)
    for k in range(iters):
        e = target - fk(th)
        if np.linalg.norm(e) < tol:
            break
        J = jac(th)
        dth = J.T @ linalg.solve(J @ J.T + lam**2 * np.eye(2), e)
        th = th + dth
    return th, np.linalg.norm(target - fk(th)), k

target = np.array([1.2, 0.8])
th, err, steps = ik_dls(target, th0=[0.3, 0.5])
print("angles:", th, "error:", err, "iterations:", steps)
print(fk(th))                                        # close to [1.2, 0.8]
```

Experiment: set `lam = 0` and start near a straight arm (`th0 = [0.3, 0.001]`). The steps become erratic or enormous: that is the singularity. A small `lam` tames it.

### Redundant robots and the null space

For a robot with more joints than task dimensions (`J` is wide), the null space of `J` contains **self-motions** that do not move the end effector. Use them for secondary goals (avoid joint limits, avoid obstacles):

**Δθ = J⁺ e + (I − J⁺ J) z**

The second term lives in the null space of `J`, so it never disturbs the primary task.

```python
rng = np.random.default_rng(0)
J = rng.standard_normal((2, 4))                # 4-joint arm, 2D task: redundant
e = np.array([0.1, -0.05])
z = rng.standard_normal(4)                      # secondary objective direction

Jp = linalg.pinv(J)
dth = Jp @ e + (np.eye(4) - Jp @ J) @ z
print(np.allclose(J @ dth, e))                  # True: secondary motion does not affect the task
```

## Lesson C3 Exercises

1. Solve `x + y + z = 6` and `x - y = 0` for the minimum-norm solution and for the general solution. Plot the solution line in 3D.
2. Verify the four Moore-Penrose conditions for a random wide matrix.
3. Fit a line to 6 data points with the constraint that it passes through the point `(2, 5)`.
4. Make a 5x4 matrix of rank 3. Find the solution with `lstsq`, then add null-space vectors and show the residual stays the same.
5. Move the IK target to `(2.0, 0.0)` (exactly at full stretch) and then to `(2.5, 0.0)` (unreachable). Describe what damped least squares does in each case.
6. Extend the IK code to a 3-link arm. Use the null-space term to keep joint 3 near 0.

---

# Lesson C4: Matrix Functions

## 4.1 Functions of matrices

Just as `eˣ = 1 + x + x²/2! + ...` for numbers, you can define it for square matrices:

**eᴬ = I + A + A²/2! + A³/3! + ...**

This is **not** the element-by-element exponential. `np.exp(A)` exponentiates each entry separately, which is a different (and usually useless) operation.

```python
A = np.array([[0., 1.],
              [-4., 0.]])
print(linalg.expm(A))
print(np.exp(A))              # NOT the matrix exponential
```

Properties you can check:

```python
rng = np.random.default_rng(0)
A = rng.standard_normal((4, 4))
B = rng.standard_normal((4, 4))

print(np.isclose(linalg.det(linalg.expm(A)), np.exp(np.trace(A))))          # True: det(e^A) = e^{tr A}
print(np.allclose(linalg.expm(A) @ linalg.expm(-A), np.eye(4)))             # True
print(np.allclose(linalg.expm(A + B), linalg.expm(A) @ linalg.expm(B)))     # False in general!
```

`e^(A+B) = e^A e^B` only if `A` and `B` **commute**. For rotations in 3D this is why the order of rotations matters.

## 4.2 How `expm` is computed

SciPy uses **scaling and squaring** with Padé approximants: scale `A` down by a power of 2 so its norm is small, approximate the exponential accurately, then square the result repeatedly. It is far more robust than summing the series. For a diagonalizable matrix, `expm(A) = V diag(exp(w)) V⁻¹` (via `eig`), which is fine for symmetric `A` but risky for non-normal ones, so use `expm` directly.

```python
A = np.array([[2., 1.], [1., 2.]])
w, V = linalg.eigh(A)
print(np.allclose(V @ np.diag(np.exp(w)) @ V.T, linalg.expm(A)))    # True (symmetric case)
```

## 4.3 Solving linear ODEs exactly

The system **x'(t) = A x(t)** with `x(0) = x₀` has the exact solution:

**x(t) = expm(A t) @ x₀**

Example: an undamped oscillator `x'' = −ω² x` written as a first-order system with state `[position, velocity]`.

```python
omega = 2.0
A = np.array([[0., 1.],
              [-omega**2, 0.]])
x0 = np.array([1., 0.])

t = 1.0
x_t = linalg.expm(A * t) @ x0
print(x_t)                                       # [-0.4161 -1.8186]
print(np.cos(omega * t), -omega * np.sin(omega * t))     # exact: same
```

Evaluate many times and plot:

```python
ts = np.linspace(0, 6, 300)
traj = np.array([linalg.expm(A * t) @ x0 for t in ts])
plt.plot(ts, traj[:, 0], label="position")
plt.plot(ts, traj[:, 1], label="velocity")
plt.legend(); plt.xlabel("t"); plt.show()
```

Add damping to see decay: use `A = [[0, 1], [-4, -0.5]]`.

When to prefer `expm` over `scipy.integrate.solve_ivp` (Module 5): **linear, time-invariant** systems where you want exact answers at any time. Use `solve_ivp` for nonlinear or time-varying problems.

## 4.4 Constant forcing: the augmented-matrix trick

For `x' = A x + b` with constant `b`, build the bigger matrix

```
M = [[A, b],
     [0, 0]]
```

and the extended state `[x; 1]`. Then `expm(M t) @ [x₀; 1]` gives `[x(t); 1]`.

```python
# scalar test: x' = -x + 1, x(0) = 0  ->  x(t) = 1 - e^{-t}
M = np.array([[-1., 1.],
              [ 0., 0.]])
print((linalg.expm(M * 1.0) @ np.array([0., 1.]))[0])       # 0.6321 = 1 - e^{-1}
```

## 4.5 Discretizing a continuous system (control and simulation)

A controlled system `x' = A x + B u` with input `u` held constant over each step `dt` (**zero-order hold**) becomes the exact discrete system

**x[k+1] = A_d x[k] + B_d u[k]**

with `A_d` and `B_d` read off a single exponential:

```python
def discretize(A, B, dt):
    n, m = A.shape[0], B.shape[1]
    M = np.zeros((n + m, n + m))
    M[:n, :n] = A
    M[:n, n:] = B
    E = linalg.expm(M * dt)
    return E[:n, :n], E[:n, n:]          # A_d, B_d
```

Example: mass-spring-damper `m x'' + c x' + k x = F` with `m = 1`, `c = 0.5`, `k = 4`, step force `F = 1`.

```python
A = np.array([[0., 1.],
              [-4., -0.5]])
B = np.array([[0.],
              [1.]])
Ad, Bd = discretize(A, B, dt=0.01)

x = np.zeros(2)
xs = []
for _ in range(2000):                      # 20 seconds
    x = Ad @ x + Bd.ravel() * 1.0
    xs.append(x[0])
print(xs[-1])                               # approaches F/k = 0.25
```

This is exactly how simulators, Kalman filters and model predictive controllers are built from continuous models, with **no time-stepping error** for the linear part.

## 4.6 Rotations: the exponential of a skew-symmetric matrix

A matrix `S` is **skew-symmetric** if `Sᵀ = −S`. Its exponential is always a **rotation matrix** (orthogonal, determinant +1).

### 2D

```python
theta = np.pi / 3
S = theta * np.array([[0., -1.],
                      [1.,  0.]])
R = linalg.expm(S)
print(R)                         # [[ 0.5   -0.866]
                                 #  [ 0.866  0.5  ]]
```

### 3D: the hat map and Rodrigues' formula

Rotating by angle `θ` about a unit axis `n` is `expm(θ · hat(n))`, where `hat(w)` is the skew-symmetric matrix with `hat(w) @ v = cross(w, v)`.

```python
def hat(w):
    return np.array([[0.,   -w[2],  w[1]],
                     [w[2],  0.,   -w[0]],
                     [-w[1], w[0],  0.]])

axis = np.array([0., 0., 1.])
theta = np.pi / 2
R = linalg.expm(theta * hat(axis))

print(np.round(R @ np.array([1., 0., 0.]), 6))       # [0. 1. 0.]
print(np.allclose(R.T @ R, np.eye(3)))               # True: orthogonal
print(np.isclose(linalg.det(R), 1.0))                # True: proper rotation

# cross-check with SciPy's rotation class (Module 11)
from scipy.spatial.transform import Rotation as Rot
print(np.allclose(R, Rot.from_rotvec(theta * axis).as_matrix()))   # True
```

Rotation vector `w = θ n` (axis times angle) is the compact "axis-angle" form used in robotics and graphics.

### The logarithm goes back

```python
S_back = linalg.logm(R).real            # skew-symmetric matrix; .real removes tiny imaginary dust
print(np.round(S_back, 6))
w_back = np.array([S_back[2, 1], S_back[0, 2], S_back[1, 0]])
print(w_back)                            # [0. 0. 1.57...] = theta * axis
```

`logm` is ill-defined when the rotation angle equals exactly π (the axis becomes ambiguous), so avoid that edge case.

### Smooth interpolation between two orientations

Animation and robot trajectories need a **smooth path between two rotations**. Interpolating matrix entries directly breaks orthogonality. Instead interpolate in the log domain:

**R(t) = R₀ · expm( t · logm(R₀ᵀ R₁) )**,   `t` from 0 to 1

```python
def rot_interp(R0, R1, t):
    return R0 @ linalg.expm(t * linalg.logm(R0.T @ R1).real)

axis = np.array([0., 0., 1.])
R0 = linalg.expm(0.2 * hat(axis))
R1 = linalg.expm(1.4 * hat(axis))

Rhalf = rot_interp(R0, R1, 0.5)
print(np.allclose(Rhalf, linalg.expm(0.8 * hat(axis))))     # True: 0.8 rad is halfway
print(np.allclose(rot_interp(R0, R1, 0.0), R0), np.allclose(rot_interp(R0, R1, 1.0), R1))   # True True
```

This is the matrix version of spherical interpolation (SLERP). It keeps the speed constant and every frame a valid rotation, and it works for rotations about **different** axes as well.

## 4.7 Square roots, logarithms and general functions

| Function | Meaning | Check |
|---|---|---|
| `sqrtm(A)` | Matrix `S` with `S @ S = A` | `np.allclose(S @ S, A)` |
| `logm(A)` | Inverse of `expm` | `expm(logm(A)) = A` |
| `fractional_matrix_power(A, p)` | `A` to a real power `p` | `p = 0.5` matches `sqrtm` |
| `sinm`, `cosm`, `tanm` | Trig functions of matrices | |
| `funm(A, f)` | Apply any scalar function `f` | `funm(A, np.sin)` matches `sinm(A)` |

```python
A = np.array([[4., 1.],
              [1., 3.]])
S = linalg.sqrtm(A)
print(np.allclose(S @ S, A))                                     # True
print(np.allclose(linalg.fractional_matrix_power(A, 0.5), S))    # True
print(np.allclose(linalg.funm(A, np.sin), linalg.sinm(A)))       # True
```

### Whitening data with `sqrtm`

If `Σ` is the covariance matrix of the data, multiplying by `Σ^(-1/2)` produces data with **identity covariance** (uncorrelated, unit variance):

```python
rng = np.random.default_rng(0)
Sigma = np.array([[4.0, 1.5],
                  [1.5, 1.0]])
X = rng.multivariate_normal([0, 0], Sigma, size=50000)

Sigma_hat = np.cov(X.T)
W = linalg.inv(linalg.sqrtm(Sigma_hat).real)
Xw = (X - X.mean(axis=0)) @ W            # W is symmetric
print(np.round(np.cov(Xw.T), 3))          # about the identity matrix
```

Whitening is a standard preprocessing step in signal processing and machine learning.

## Lesson C4 Exercises

1. Compute `expm(A)` for a diagonal `A`. Compare with `np.exp` of the diagonal entries and explain.
2. Simulate a damped oscillator (`c = 0.3`) with `expm` and plot position. Mark the envelope `e^(−c t / 2)`.
3. Discretize the mass-spring-damper with `dt = 0.1` and compare the exact discrete simulation with `scipy.integrate.solve_ivp` (Module 5) once you have it.
4. Compose a rotation of 90 degrees about x followed by 90 degrees about y. Show the result differs from the reverse order, and verify with `Rot`.
5. Interpolate between the identity and a 150-degree rotation about `(1, 1, 0)/√2` at 10 values of `t`, and check that every intermediate matrix is orthogonal with determinant 1.
6. Show `det(expm(A)) = exp(trace(A))` for 10 random matrices and explain why `expm(A)` is always invertible.

---

# Lesson C5: Matrix Equations: Sylvester, Lyapunov, Riccati (Advanced)

These equations appear throughout control theory, vibration analysis and estimation. SciPy solves them with Schur-based algorithms (Phase B6).

## 5.1 Sylvester equation

**A X + X B = Q**

```python
rng = np.random.default_rng(0)
A = rng.standard_normal((3, 3)) + 5 * np.eye(3)
B = rng.standard_normal((2, 2)) + 5 * np.eye(2)
Q = rng.standard_normal((3, 2))

X = linalg.solve_sylvester(A, B, Q)
print(np.allclose(A @ X + X @ B, Q))        # True
```

A solution exists and is unique when `A` and `−B` share no eigenvalues. Never solve it via an enormous Kronecker system for large problems.

## 5.2 Lyapunov equations

**Continuous:** `A X + X Aᴴ = Q`
**Discrete:** `A X Aᴴ − X + Q = 0`

```python
Ac = np.array([[-1., 0.],
               [ 0., -2.]])
Bc = np.array([[1.],
               [1.]])

W = linalg.solve_continuous_lyapunov(Ac, -Bc @ Bc.T)
print(W)                                     # [[0.5    0.3333]
                                             #  [0.3333 0.25  ]]
```

Check by hand: entry `W[0,0]`: `−2 W00 = −1`, so `0.5`; `W[1,1]`: `−4 W11 = −1`, so `0.25`; `W[0,1]`: `−3 W01 = −1`, so `1/3`.

`W` is the **controllability gramian**. It measures how much energy is needed to push the system in each direction. Its eigenvalues reveal which states are hard to control.

```python
print(linalg.solve_discrete_lyapunov(np.array([[0.5]]), np.array([[1.0]])))   # [[1.3333]]
```

(Scalar check: `0.25 X − X + 1 = 0` gives `X = 4/3`.)

### Lyapunov stability test

A matrix `A` is stable (all eigenvalues have negative real part) exactly when `Aᵀ P + P A = −I` has a **symmetric positive definite** solution `P`:

```python
A = np.array([[0., 1.],
              [-4., -0.5]])
P = linalg.solve_continuous_lyapunov(A.T, -np.eye(2))
print(np.linalg.eigvalsh(P))                 # both positive: stable
```

The function `V(x) = xᵀ P x` is then a **Lyapunov function**: it decreases along every trajectory, a certificate of stability that extends to nonlinear systems.

## 5.3 Algebraic Riccati equation and LQR control

**Linear Quadratic Regulator (LQR)**: for the system `x' = A x + B u`, find the feedback `u = −K x` that minimizes the cost

`∫ (xᵀ Q x + uᵀ R u) dt`

(a trade-off between keeping the state small and using little control effort). The answer comes from the **continuous algebraic Riccati equation (CARE)**:

**Aᵀ P + P A − P B R⁻¹ Bᵀ P + Q = 0**,  and then  **K = R⁻¹ Bᵀ P**

```python
# double integrator: position and velocity, force input (a cart with no friction)
A = np.array([[0., 1.],
              [0., 0.]])
B = np.array([[0.],
              [1.]])
Q = np.eye(2)
R = np.array([[1.]])

P = linalg.solve_continuous_are(A, B, Q, R)
K = linalg.solve(R, B.T @ P)

print(P)                                  # [[1.732 1.   ]
                                          #  [1.    1.732]]
print(K)                                  # [[1.    1.732]]
print(linalg.eigvals(A - B @ K))          # -0.866 ± 0.5j: stable and well damped
```

Check by hand: the known closed form for this problem is `P = [[√3, 1], [1, √3]]` and `K = [1, √3]`.

Simulate the closed loop with `expm`:

```python
Acl = A - B @ K
x0 = np.array([1.0, 0.0])                  # start 1 m from the target at rest
ts = np.linspace(0, 10, 200)
traj = np.array([linalg.expm(Acl * t) @ x0 for t in ts])

plt.plot(ts, traj[:, 0], label="position")
plt.plot(ts, traj[:, 1], label="velocity")
plt.plot(ts, [x0[0]] * len(ts), "k:", alpha=0.3)
plt.legend(); plt.xlabel("t"); plt.show()
```

Without control, the open-loop double integrator never settles; with LQR the state decays smoothly. Change `R` to `0.01` (cheap control) and `100` (expensive control) to see the trade-off: aggressive control gives a faster response with larger inputs.

The discrete-time versions are `solve_discrete_are` and, for the Kalman filter, the same equation applies with `A` and `Aᵀ` swapped by duality. This is the mathematical heart of optimal control and optimal state estimation, both essential for humanoid robotics.

## Lesson C5 Exercises

1. Verify the Sylvester solution against a Kronecker-product formulation for a tiny example: `(I ⊗ A + Bᵀ ⊗ I) vec(X) = vec(Q)` (use `np.kron` and column-major `vec`).
2. Compute the controllability gramian for a 3-state system of your choice. Which state needs the most energy to control?
3. Test Lyapunov stability for three matrices: one stable, one unstable, one with imaginary eigenvalues. Interpret `P`.
4. Design an LQR controller for a pendulum linearized about the upright position, `A = [[0, 1], [g/l, 0]]`, `B = [[0], [1/(m l²)]]`. Is `A − B K` stable?
5. Plot closed-loop poles of the double integrator as `R` goes from `0.01` to `100`.

---

# Lesson C6: Structured and Banded Systems

Real large problems are almost always **structured**. Exploiting structure turns impossible computations into trivial ones.

## 6.1 Special matrix builders

```python
linalg.toeplitz([1, 2, 3])            # constant along each diagonal
linalg.circulant([1, 2, 3])           # each row is the previous one shifted cyclically
linalg.hankel([1, 2, 3])              # constant along anti-diagonals
linalg.block_diag(A, B)               # independent blocks on the diagonal
linalg.kron(A, B)                     # Kronecker product
linalg.hilbert(4)                     # classic ill-conditioned matrix
linalg.dft(4)                         # discrete Fourier transform matrix
linalg.companion([1, -6, 11, -6])     # roots of x^3 - 6x^2 + 11x - 6 are its eigenvalues
```

Check the companion matrix idea:

```python
C = linalg.companion([1, -6, 11, -6])
print(np.sort(linalg.eigvals(C).real))        # [1. 2. 3.]
```

`np.roots` does exactly this internally.

Check the DFT matrix against the FFT:

```python
F = linalg.dft(8)
x = np.random.default_rng(0).standard_normal(8)
print(np.allclose(F @ x, np.fft.fft(x)))      # True
```

(The FFT computes the same matrix-vector product in `O(n log n)` instead of `O(n²)`: Module 9.)

## 6.2 Banded matrices

A matrix with non-zeros only near the diagonal (within `l` rows below and `u` rows above) is **banded**. Tridiagonal (`l = u = 1`) is the most common: 1D diffusion, beams, chains, splines, implicit time-stepping.

**Banded storage** (compact form `ab`): row `u + i − j` and column `j` of `ab` holds `a[i, j]`. For a tridiagonal matrix:

```
ab[0, 1:]  = upper diagonal
ab[1, :]   = main diagonal
ab[2, :-1] = lower diagonal
```

```python
n = 5
ab = np.zeros((3, n))
ab[0, 1:]  = -1.0
ab[1, :]   =  2.0
ab[2, :-1] = -1.0
b = np.ones(n)

x = linalg.solve_banded((1, 1), ab, b)       # (l, u) = (1, 1)
print(x)                                      # [2.5 4.  4.5 4.  2.5]

# verify against the dense solve
K = 2*np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
print(np.allclose(linalg.solve(K, b), x))     # True
```

Cost: `O(n)` time and memory, versus `O(n³)` and `O(n²)` for dense.

### Speed comparison

```python
import time
n = 3000
ab = np.zeros((3, n)); ab[0, 1:] = -1; ab[1] = 2; ab[2, :-1] = -1
b = np.ones(n)
K = 2*np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)

t0 = time.perf_counter(); linalg.solve(K, b); t_dense = time.perf_counter() - t0
t0 = time.perf_counter(); linalg.solve_banded((1, 1), ab, b); t_band = time.perf_counter() - t0
print(f"dense {t_dense:.3f}s   banded {t_band:.6f}s")
```

Then try `n = 1_000_000` with the banded solver only. A dense matrix of that size would need 8 terabytes.

## 6.3 Symmetric positive definite banded systems

For SPD banded matrices (almost every stiffness matrix) use `solveh_banded`, which stores only the diagonal and one triangle, using Cholesky:

```python
ab_sym = np.zeros((2, n))       # upper form: row 0 = superdiagonal, row 1 = diagonal
ab_sym[0, 1:] = -1.0
ab_sym[1, :] = 2.0
x = linalg.solveh_banded(ab_sym, b)
print(np.allclose(x, linalg.solve_banded((1, 1), ab, b)))      # True
```

Related: `cholesky_banded`, `cho_solve_banded`, `eig_banded`, `eigh_tridiagonal` (Phase B5).

## 6.4 Worked example: heat flow in a rod (finite differences)

Steady heat conduction with a uniform source and both ends held at temperature 0:

**−u''(x) = 1** on (0, 1), `u(0) = u(1) = 0`.

Exact solution: `u(x) = x(1 − x) / 2`.

Discretize with `N` interior points and spacing `h = 1/(N+1)`. The second derivative becomes `(u[i−1] − 2u[i] + u[i+1]) / h²`, giving the system

**(1/h²) K u = f**, with `K` the tridiagonal `[−1, 2, −1]` matrix.

```python
N = 99
h = 1.0 / (N + 1)
xg = np.linspace(h, 1 - h, N)

ab = np.zeros((2, N))
ab[0, 1:] = -1.0
ab[1, :] = 2.0
f = h**2 * np.ones(N)                         # right-hand side scaled by h^2

u = linalg.solveh_banded(ab, f)
exact = xg * (1 - xg) / 2
print(np.max(np.abs(u - exact)))              # about 1e-16: exact at the nodes
```

The finite-difference solution is **exact at the grid points** here because the exact solution is a quadratic (its fourth derivative is zero). For `−u'' = sin(πx)` the error drops like `h²`. Test this: halve `h` and check the error shrinks by about 4. This is called a **convergence study**, the basic validation tool for every numerical method.

## 6.5 Toeplitz and circulant systems

**Toeplitz** matrices have constant diagonals (stationary time series, filtering, deconvolution). Special solvers run in `O(n²)` (Levinson) instead of `O(n³)`:

```python
n = 500
c = 0.5 ** np.arange(n)                       # AR(1) covariance: first column of a symmetric Toeplitz matrix
b = np.random.default_rng(0).standard_normal(n)

x1 = linalg.solve_toeplitz(c, b)
x2 = linalg.solve(linalg.toeplitz(c), b)
print(np.allclose(x1, x2))                    # True
```

**Circulant** matrices are diagonalized by the FFT, so solves cost `O(n log n)`:

```python
c = np.array([4., 1., 0., 0., 0., 1.])        # first column; diagonally dominant, so invertible
b = np.arange(6.)
x1 = linalg.solve_circulant(c, b)
x2 = linalg.solve(linalg.circulant(c), b)
print(np.allclose(x1, x2))                    # True

print(np.allclose(np.sort(linalg.eigvals(linalg.circulant(c)).real),
                  np.sort(np.fft.fft(c).real)))        # True: eigenvalues are the FFT of c
```

Circulant systems arise from periodic boundary conditions and circular convolution.

## 6.6 Kronecker structure: the 2D Poisson problem

Discretizing `−Δu = 1` on a square grid with `n` interior points per side gives `n² ` unknowns and the matrix

**A₂ = I ⊗ T + T ⊗ I**,  where `T` is the 1D tridiagonal matrix.

```python
n = 20
T = 2*np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
I = np.eye(n)
A2 = np.kron(I, T) + np.kron(T, I)                 # (n^2) x (n^2) = 400 x 400
h = 1.0 / (n + 1)
f = h**2 * np.ones(n * n)

u = linalg.solve(A2, f, assume_a="pos").reshape(n, n)
print(u.max())                                      # about 0.07 (center of the square)

plt.imshow(u, origin="lower", extent=[0, 1, 0, 1])
plt.colorbar(label="u")
plt.title("Solution of -Δu = 1 on the unit square")
plt.show()
```

Scale-up warning: `n = 100` gives a 10,000 x 10,000 dense matrix (800 MB) and `n = 1000` gives a 10⁶ x 10⁶ matrix that cannot be stored densely at all. The matrix is almost entirely zeros, so the next module (**scipy.sparse**) is the answer. This lesson is the bridge to it.

## 6.7 Block-diagonal systems

If a system consists of independent subsystems, `block_diag` keeps them separate, and solves/eigenvalue problems split block by block:

```python
A1 = np.array([[2., -1.], [-1., 2.]])
A2_ = np.array([[3., 1.], [1., 3.]])
Abd = linalg.block_diag(A1, A2_)
print(np.sort(linalg.eigvalsh(Abd)))
print(np.sort(np.concatenate([linalg.eigvalsh(A1), linalg.eigvalsh(A2_)])))     # same
```

## Lesson C6 Exercises

1. Time `solve` against `solve_banded` for `n = 500, 1000, 2000, 4000` and fit the growth exponent of each.
2. Solve `−u'' = sin(πx)` with `N = 10, 20, 40, 80` interior points and print the maximum error against `sin(πx)/π²`. Confirm the error shrinks by about 4 each time `N` doubles.
3. Add a convection term (a non-symmetric tridiagonal matrix) and use `solve_banded` with `l = u = 1`.
4. Use `solve_toeplitz` with `n = 5000` and compare memory and time with the dense approach.
5. Verify numerically that the eigenvalues of the 2D Poisson matrix `A₂` are the sums `λᵢ + λⱼ` of the eigenvalues of `T`.
6. Build the circulant matrix for the three-point averaging filter `[0.25, 0.5, 0.25]` (periodic) and compute its eigenvalues. Interpret them as the frequency response of the filter.

---

# Lesson C7: Applications Lab

Five complete mini-projects. Each is one script for your repo. Always include a **validation step**: a known answer you compare against.

## Application 1: Image compression with SVD

```python
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

# synthetic 200 x 200 image: a smooth pattern plus fine noise
x = np.linspace(0, 4 * np.pi, 200)
img = np.outer(np.sin(x), np.cos(0.5 * x)) + 0.5 * np.outer(np.cos(2 * x), np.sin(x))
rng = np.random.default_rng(0)
img = img + 0.02 * rng.standard_normal(img.shape)

U, s, Vh = linalg.svd(img, full_matrices=False)

def rank_k(k):
    return U[:, :k] @ np.diag(s[:k]) @ Vh[:k]

for k in (1, 2, 5, 20, 100):
    approx = rank_k(k)
    err = linalg.norm(img - approx) / linalg.norm(img)
    storage = k * (img.shape[0] + img.shape[1] + 1) / img.size
    print(f"k={k:3d}  relative error={err:.4f}  storage={storage:6.1%}")

plt.semilogy(s, "o-")
plt.title("Singular values: sharp drop means compressible")
plt.xlabel("index"); plt.ylabel("singular value")
plt.show()
```

How to read it:

- The pattern has rank about 2, so error falls to the noise floor at `k = 2`, with about 2 percent of the storage.
- Eckart-Young guarantees no other rank-`k` image does better.
- Validate: `‖img − rank_k‖_F` must equal `sqrt(sum(s[k:]**2))`.

For a **real photo**, load a grayscale image with Matplotlib (`plt.imread`) or Pillow, convert to a float 2D array, and run the same code. For colour images, compress each channel separately.

## Application 2: PCA from scratch

**Principal Component Analysis** finds the directions of greatest variance.

```python
rng = np.random.default_rng(1)
angle = np.deg2rad(30)
Rot2 = np.array([[np.cos(angle), -np.sin(angle)],
                 [np.sin(angle),  np.cos(angle)]])
X = (rng.standard_normal((500, 2)) * [3.0, 0.5]) @ Rot2.T      # stretched and rotated cloud

Xc = X - X.mean(axis=0)                           # 1. center the data
U, s, Vh = linalg.svd(Xc, full_matrices=False)    # 2. SVD of the centered data

explained = s**2 / (len(X) - 1)                   # variance along each principal axis
print("variances:", explained)                     # about [9, 0.25]
print("ratio    :", explained / explained.sum())   # about [0.97, 0.03]
print("axes     :\n", Vh)                          # first row: direction at about 30 degrees

scores = Xc @ Vh.T                                 # coordinates in the principal basis
```

Validate: the eigenvalues of `np.cov(Xc.T)` (via `eigh`) must equal `explained`. Compare the SVD route with the covariance route, and show why the SVD route is more accurate for ill-conditioned data (no `AᵀA`).

Plot the data with the two principal axes drawn as arrows scaled by `sqrt(explained)`. Then reduce dimension: keep only the first column of `scores` and reconstruct with `scores[:, :1] @ Vh[:1] + mean`; the error is the discarded variance.

## Application 3: Fit a plane to a 3D point cloud

For scanning, mapping and robotics (floor detection, wall fitting). The best-fit plane passes through the **centroid**, and its **normal** is the right singular vector with the **smallest** singular value.

```python
rng = np.random.default_rng(2)
xy = rng.uniform(-5, 5, size=(300, 2))
z = 0.3 * xy[:, 0] - 0.2 * xy[:, 1] + 1.0 + 0.05 * rng.standard_normal(300)
P = np.column_stack([xy, z])

centroid = P.mean(axis=0)
_, s, Vh = linalg.svd(P - centroid, full_matrices=False)
normal = Vh[-1]

print("normal:", normal)             # proportional to (-0.3, 0.2, 1), up to sign
print("singular values:", s)         # last one is tiny: only noise is left

dist = (P - centroid) @ normal       # signed distances to the plane
print("RMS distance:", np.sqrt(np.mean(dist**2)))          # about the noise level, 0.05
```

Validate against the true normal: `n_true = np.array([-0.3, 0.2, 1.0]); n_true /= np.linalg.norm(n_true)` and check `abs(normal @ n_true)` is close to 1.

Extend with **RANSAC-style robustness**: repeatedly fit a plane to random 3-point samples, count inliers, keep the best, then refit with the SVD on the inliers. Add 30 percent outliers to see why a plain SVD fit fails and RANSAC succeeds.

## Application 4: Rigid registration (Kabsch algorithm)

Given two sets of corresponding 3D points (for example a 3D scan and a model, or two camera views), find the rotation `R` and translation `t` that best map one onto the other:

**minimize Σ ‖R pᵢ + t − qᵢ‖²**

The solution uses the SVD of the cross-covariance matrix.

```python
def hat(w):
    return np.array([[0., -w[2], w[1]],
                     [w[2], 0., -w[0]],
                     [-w[1], w[0], 0.]])

def kabsch(P, Q):
    """Find R, t such that  Q ≈ P @ R.T + t  (rows are points)."""
    pc, qc = P.mean(axis=0), Q.mean(axis=0)
    H = (P - pc).T @ (Q - qc)                         # 3 x 3 cross-covariance
    U, S, Vt = linalg.svd(H)
    d = np.sign(linalg.det(Vt.T @ U.T))               # fix a possible reflection
    D = np.diag([1.0, 1.0, d])
    R = Vt.T @ D @ U.T
    t = qc - R @ pc
    return R, t

rng = np.random.default_rng(3)
P = rng.standard_normal((100, 3))
R_true = linalg.expm(hat(np.array([0.3, -0.5, 0.8])))
t_true = np.array([1.0, -2.0, 0.5])
Q = P @ R_true.T + t_true + 0.01 * rng.standard_normal((100, 3))

R_est, t_est = kabsch(P, Q)
print("rotation error   :", np.linalg.norm(R_est - R_true))        # about 1e-3
print("translation error:", np.linalg.norm(t_est - t_true))        # about 1e-3

rmsd = np.sqrt(np.mean(np.sum((P @ R_est.T + t_est - Q) ** 2, axis=1)))
print("RMSD:", rmsd)                                                # about the noise level
```

The sign correction `d` is essential: without it the SVD can return a **reflection** (determinant −1) instead of a proper rotation. Test by feeding a mirrored point set.

Cross-check with SciPy's built-in: `scipy.linalg.orthogonal_procrustes` solves the same problem for centred row-point sets (note its convention `P @ R ≈ Q`, which is the transpose of the rotation used above).

This algorithm underlies ICP point-cloud alignment, motion capture alignment and hand-eye calibration.

## Application 5: System identification from data

Learn the dynamics `x[k+1] = A x[k]` of an unknown system directly from measurements, a simple form of **dynamic mode decomposition (DMD)**.

```python
rng = np.random.default_rng(0)
th = 0.1
A_true = 0.95 * np.array([[np.cos(th), -np.sin(th)],
                          [np.sin(th),  np.cos(th)]])      # a slowly decaying spiral

X1 = rng.standard_normal((2, 500))                           # many starting states
X2 = A_true @ X1 + 0.002 * rng.standard_normal((2, 500))     # next states, with measurement noise

# X2 ≈ A X1  ->  X1^T A^T ≈ X2^T  (ordinary least squares)
A_est = linalg.lstsq(X1.T, X2.T)[0].T

print("A_true:\n", A_true)
print("A_est :\n", np.round(A_est, 4))
print("error :", np.linalg.norm(A_est - A_true))                # about 1e-3
print("eigenvalues true:", np.round(linalg.eigvals(A_true), 4))
print("eigenvalues est :", np.round(linalg.eigvals(A_est), 4))
```

Interpret: `|λ| = 0.95` means a 5 percent decay per step, and the angle `0.1 rad` is the rotation per step. Recovering eigenvalues from raw data is exactly how engineers extract **frequencies and damping** from measured vibrations.

Extension: generate a single noisy trajectory instead of independent states, estimate `A`, and see how the estimate degrades when the trajectory decays to the noise floor (poor excitation). Then repeat with a lightly forced system.

## Lesson C7 Exercises

1. For Application 1, plot the reconstructed image (as `imshow`) next to the original for `k = 1, 2, 5, 20` and the error map `|img − approx|`.
2. For Application 2, compare PCA by `svd` and by `eigh(np.cov(...))` on a dataset with 50 highly correlated features. Compare accuracy of the smallest components.
3. Fit a plane to a real-world-like scene: points on two perpendicular planes (floor and wall), fit each, and report the angle between normals using the dot product.
4. For Application 4, add 10 percent random outlier correspondences. How much does the estimate degrade? Implement a trimmed version that discards the worst 15 percent and refits.
5. For Application 5, identify a damped oscillator with known mass-spring-damper parameters, convert the identified `A_d` back to continuous time with `logm(A_est)/dt`, and compare with the true `[[0, 1], [-k/m, -c/m]]`.

---

# Capstone: `linear_algebra_lab`

A small package with a command-line menu (`argparse` or `input()`), a `tests/` folder and a README with example output. It combines everything in Module 2.

| Menu item | Calls on | Must report |
|---|---|---|
| 1. Solve and diagnose | Phase A | solution, residual, backward error, `cond`, digits trusted, verdict |
| 2. Decompose | Phase B | SPD test, LU, Cholesky, QR, eigen, SVD shapes with reconstruction checks |
| 3. Modal analysis | Phase B | natural frequencies, mode shapes plot, mass-orthogonality check |
| 4. Fit a model | Phase C1 to C2 | coefficients with standard errors, R², residual plot, best degree by train/test |
| 5. Ridge and robust fit | Phase C2 | `λ` sweep (L-curve), IRLS result with outliers |
| 6. Inverse kinematics | Phase C3 | joint angles, error, iterations for a given target |
| 7. Simulate linear system | Phase C4 | `expm` trajectory plot, discretization check |
| 8. Rotation tool | Phase C4 | axis-angle to matrix, composition, interpolation, orthogonality check |
| 9. LQR design | Phase C5 | gains, closed-loop poles, response plot |
| 10. Banded solver | Phase C6 | solution with timing against dense solve |
| 11. SVD compression | Phase C7 | error and storage table for several ranks |
| 12. Registration | Phase C7 | rotation, translation, RMSD |

Quality bar:

1. Every function has a **test with a known answer** (use closed forms from this module).
2. Every numerical result is **validated by a second method** (for example `expm` against modal formulas).
3. Every function handles **bad inputs** (singular matrix, wrong shapes) with a clear message.
4. The README explains each feature with a short example and an image.

---

# Exercise Hints

**C1.**
2. The least squares residual is the shortest of all residuals, and `Aᵀ r` should be about `1e-15`.
3. For a single column `t`, `AᵀA = Σ t²` and `Aᵀ y = Σ t y`.
5. Adding any column to `A` cannot raise the residual, because the old solution (with coefficient 0 on the new column) is still available.

**C2.**
1. After scaling `T` to `[-1, 1]`, `cond` should drop by orders of magnitude.
3. The coefficient norm decreases as `λ` grows; for tiny `λ` it is dominated by noise amplification.
5. IRLS should land much closer to the true line than ordinary least squares.
6. `a sin(ωt) + b cos(ωt) = A sin(ωt + φ)` with `A = sqrt(a² + b²)` and `φ = atan2(b, a)`.

**C3.**
1. The minimum-norm solution is perpendicular to the null space direction.
3. Constraint `c0 + 2 c1 = 5`: use `C = [[1, 2]]`, `d = [5]` in `constrained_lstsq`.
5. At full stretch the Jacobian is singular. Damping makes the arm approach the target slowly instead of blowing up. For an unreachable target, it settles at the closest reachable point.

**C4.**
1. For a diagonal matrix, `expm` equals the element-wise exponential of the diagonal (and zero elsewhere).
4. Rotations about different axes do not commute, so `Ry @ Rx != Rx @ Ry`.
6. `det(expm(A)) = exp(trace(A))` is never zero, so the exponential is always invertible.

**C5.**
1. Use column-major vectorization: `X.flatten(order="F")`.
4. For the inverted pendulum `A` has an eigenvalue `+sqrt(g/l)` (unstable), and LQR moves it to the left half-plane.

**C6.**
1. Dense `solve` slope near 3, banded slope near 1 on a log-log plot.
2. Error ratio near 4 between successive halvings of `h` (second-order accuracy).
5. Eigenvalues of `I ⊗ T + T ⊗ I` are all pairwise sums `λᵢ + λⱼ`.
6. The eigenvalues are `0.5 + 0.5 cos(2πk/n)`: a smoothing (low-pass) filter.

**C7.**
2. Covariance-based PCA squares the condition number, so the tiny components lose accuracy first.
5. `A_c = logm(A_d) / dt`; real parts give damping, imaginary parts give frequency.

---

# Common Mistakes

| Mistake | Fix |
|---|---|
| Normal equations on an ill-conditioned fit | Use `lstsq` or QR |
| Fitting high-degree polynomials in the monomial basis | Rescale `x` and use a Chebyshev basis |
| Judging a fit by `R²` alone | Look at residual plots and held-out error |
| Reporting coefficients without uncertainty | Give standard errors |
| Forgetting weights for unequal noise | Weighted least squares |
| Letting outliers drive the fit | Robust fit (IRLS or `loss="huber"`) |
| Using `np.exp(A)` instead of `expm(A)` | `expm` is the matrix exponential |
| Assuming `expm(A+B) = expm(A) expm(B)` | Only when `A` and `B` commute |
| Interpolating rotation matrices entry by entry | Interpolate in the log domain |
| Ignoring a Kabsch reflection | Include the `det` sign correction |
| Dense matrices for huge structured problems | Banded, Toeplitz or sparse solvers |
| Forgetting that `logm` may return complex dust | Use `.real` after checking the imaginary part is tiny |
| Trusting `pinv` blindly for noisy data | Choose the cutoff from the noise level |

# Cheat Sheet

```python
# least squares
x, res, rank, s = linalg.lstsq(A, b)
x = linalg.pinv(A) @ b
W = np.sqrt(w); x = linalg.lstsq(A * W[:, None], b * W)[0]      # weighted
x = linalg.lstsq(np.vstack([A, np.sqrt(lam)*np.eye(n)]),
                 np.concatenate([b, np.zeros(n)]))[0]            # ridge

# matrix functions
linalg.expm(A * t) @ x0             # x' = A x
linalg.logm(R).real                 # rotation logarithm
linalg.sqrtm(A); linalg.funm(A, f)

# matrix equations
linalg.solve_sylvester(A, B, Q)
linalg.solve_continuous_lyapunov(A, Q)
P = linalg.solve_continuous_are(A, B, Q, R); K = linalg.solve(R, B.T @ P)

# structured systems
linalg.solve_banded((l, u), ab, b)
linalg.solveh_banded(ab, b)
linalg.solve_toeplitz(c, b)
linalg.solve_circulant(c, b)
```

---

# Phase C Checkpoint

You are ready for Module 3 when you can honestly check every box:

- [ ] I can derive the normal equations from the projection picture and explain why the residual is orthogonal to the columns.
- [ ] I solve least squares with QR or `lstsq`, and I know when the normal equations are dangerous.
- [ ] I report fit coefficients with standard errors and judge fits with residual plots and held-out error.
- [ ] I use orthogonal bases for polynomial fits and know why.
- [ ] I can apply weights, ridge, truncated SVD and robust fitting, and explain what each does to the singular values or the outliers.
- [ ] I can compute the minimum-norm solution, parametrize all solutions with the null space, and do equality-constrained least squares.
- [ ] I implemented damped least squares inverse kinematics and understand singularities.
- [ ] I can solve `x' = A x` exactly with `expm`, handle forcing, and discretize with zero-order hold.
- [ ] I can build rotations with `expm`, recover axis-angle with `logm`, and interpolate orientations smoothly.
- [ ] I can solve Lyapunov and Riccati equations and explain LQR.
- [ ] I can solve banded, Toeplitz and circulant systems and explain why Kronecker structure leads to sparse matrices.
- [ ] I built and validated all five applications and the capstone.

## Quick self-quiz (answers at the bottom)

1. In a least squares fit, what is `Aᵀ r` for the optimal residual `r`, and why?
2. Why is fitting a degree-15 polynomial in the monomial basis a bad idea, and what do you do instead?
3. What does ridge regression do to the small singular values of `A`?
4. How do you compute `x(t)` for `x' = A x` and what is the cost compared with simulation by time-stepping?
5. Why must the Kabsch algorithm check the sign of a determinant?
6. A 1D chain with a million unknowns: dense or banded solver?

**Answers:** (1) It is zero: the residual is perpendicular to the column space, since the fitted vector is the orthogonal projection of `b`. (2) Its Vandermonde matrix has an enormous condition number. Rescale `x` to `[-1, 1]` and use a Chebyshev basis. (3) It shrinks their contribution by the filter factor `σ² / (σ² + λ)`, suppressing the noise-dominated directions. (4) `x(t) = expm(A t) @ x0`. It gives the exact answer at any `t` with one matrix exponential, no step-size error. (5) The SVD can return an orthogonal matrix with determinant −1, which is a reflection rather than a rotation. (6) Banded: `O(n)` time and memory versus a dense matrix of 8 terabytes.

---

# Suggested Repo Layout for This Phase

```
02-linear-algebra/phase-C-least-squares-and-applications/
├── README.md
├── lessons/
│   ├── C1-least-squares-foundations.md
│   ├── C2-fitting-in-practice.md
│   ├── C3-underdetermined-and-ik.md
│   ├── C4-matrix-functions.md
│   ├── C5-matrix-equations-lqr.md
│   ├── C6-structured-systems.md
│   └── C7-applications.md
├── code/
│   ├── ridge.py
│   ├── robust_fit.py
│   ├── constrained_lstsq.py
│   ├── ik_dls.py
│   ├── rotations.py
│   ├── discretize.py
│   └── poisson_1d_2d.py
├── apps/
│   ├── app1_svd_compression.py
│   ├── app2_pca.py
│   ├── app3_plane_fit.py
│   ├── app4_kabsch.py
│   └── app5_system_id.py
├── capstone/
│   └── linear_algebra_lab/
├── exercises/
└── tests/
    └── test_phase_C.py
```

---

# Module 2 Complete: What You Can Now Do

- Solve any linear system and say **how much to trust it**.
- Choose the right **factorization** for speed and accuracy.
- Find **modes, frequencies, rank and stability** from eigenvalues and the SVD.
- **Fit data** responsibly: weights, regularization, robustness, error bars.
- Solve **linear dynamics exactly**, build **rotations**, design an **LQR controller**.
- Handle **big structured problems** in linear time.
- Build real tools for **robotics, vibration analysis, 3D data and signal identification**.

**Next:** Module 3, Sparse Matrices (`scipy.sparse`): the same ideas for matrices with millions of rows.
