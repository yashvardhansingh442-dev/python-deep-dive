# Module 1: Special Functions (`scipy.special`)

> Part of the SciPy Course. Prerequisites: basic Python and NumPy.

```python
import numpy as np
from scipy import special
```

## Module Overview

| Lesson | Topic |
|---|---|
| 1.1 | Gamma, beta, factorial and combinatorics |
| 1.2 | Error function and Bessel functions |
| 1.3 | Numerically stable helpers (`logsumexp`, `expit`, `softmax`) |

---

## Lesson 1.1: Gamma, Beta, Factorial and Combinatorics

### 1. Why special functions exist

Some functions appear again and again in physics, engineering and statistics, but have no simple closed form using `+ - × ÷ sin exp`. People gave them names and wrote very accurate, fast, tested code for them. `scipy.special` is that collection.

### 2. The gamma function

The factorial only works for whole numbers (5! = 120). The **gamma function** extends it to all real (and complex) numbers:

**Γ(n) = (n − 1)!** for positive integers n.

```python
special.gamma(5)     # 24.0   -> this is 4!
special.gamma(6)     # 120.0  -> this is 5!
special.gamma(0.5)   # 1.7724538509055159 -> this is sqrt(pi)
special.gamma(4.5)   # 11.63172839656745 -> "3.5 factorial"
```

Key facts:

- Γ(x + 1) = x · Γ(x), the same rule as n! = n · (n−1)!
- Γ(1/2) = √π, which shows up in the normal distribution
- Γ has poles (blows up) at 0, −1, −2, ..., so `special.gamma(0)` returns `inf`

### 3. Factorial, permutations and combinations

```python
special.factorial(5)              # 120.0
special.factorial(5, exact=True)  # 120  (exact Python integer)
special.factorial([3, 4, 5])      # array([  6.,  24., 120.])

special.comb(10, 3)               # 120.0  -> "10 choose 3"
special.comb(10, 3, exact=True)   # 120
special.perm(5, 2)                # 20.0   -> 5 x 4
```

- `comb(n, k)` = n! / (k!(n−k)!), the number of ways to choose k items from n when order does not matter.
- `perm(n, k)` = n! / (n−k)!, the number of ways when order matters.
- Use `exact=True` when you need exact big integers. Without it you get floats, which lose precision for large values.

### 4. The overflow problem and `gammaln`

Factorials grow incredibly fast.

```python
special.gamma(171)   # 7.257415615307994e+306  (near the float limit)
special.gamma(172)   # inf  (overflow!)
```

In probability and statistics you often need Γ of big numbers. The fix is to work with logarithms:

```python
special.gammaln(1000)   # 5905.220423209181  = ln(Γ(1000))
```

`gammaln` computes ln|Γ(x)| directly without ever forming the huge number. `loggamma` does the same but supports complex input and keeps the sign information.

**Rule of thumb:** if numbers might get huge, compute in log space and only exponentiate at the end.

### 5. The beta function

**B(a, b) = Γ(a) Γ(b) / Γ(a + b)**

```python
special.beta(2, 3)     # 0.08333333333333333  (= 1/12)
special.betaln(2, 3)   # log version, for large inputs
```

It appears in the Beta distribution, Bayesian statistics and integrals of the form ∫ tᵃ⁻¹ (1−t)ᵇ⁻¹ dt from 0 to 1.

### 6. The digamma function

The derivative of ln Γ(x):

```python
special.digamma(1)   # -0.5772156649015329  (negative Euler–Mascheroni constant)
```

Used in maximum-likelihood estimation for gamma and Dirichlet distributions.

### Lesson 1.1 Exercises

1. Verify `special.gamma(7) == special.factorial(6)`.
2. How many 5-card hands exist in a 52-card deck? (Use `comb` with `exact=True`.)
3. Find the smallest integer n where `special.gamma(n)` returns `inf`, then compute `gammaln` of that n.
4. Check numerically that Γ(x+1) = x·Γ(x) for x = 3.7.

---

## Lesson 1.2: Error Function and Bessel Functions

### 1. The error function

**erf(x) = (2/√π) ∫₀ˣ e^(−t²) dt**

It is the area under a bell curve, scaled so that erf(0) = 0 and erf(∞) = 1.

```python
special.erf(0)    # 0.0
special.erf(1)    # 0.8427007929497149
special.erf(3)    # 0.9999779095030014  (almost 1)
```

Related functions:

| Function | Meaning |
|---|---|
| `erf(x)` | error function |
| `erfc(x)` | complementary error function, 1 − erf(x) |
| `erfinv(y)` | inverse: returns x such that erf(x) = y |
| `erfcx(x)` | scaled complementary function, e^(x²) · erfc(x), stable for large x |

```python
special.erfc(1)       # 0.15729920705028513
special.erfinv(0.5)   # 0.4769362762044699
```

**Why `erfc` exists:** for large x, `1 - erf(x)` rounds to exactly 0 because of floating-point limits, but `erfc(x)` still gives the tiny correct value. Use `erfc` for tails.

### 2. Connection to the normal distribution

The standard normal CDF is Φ(x) = ½ [1 + erf(x/√2)].

```python
import numpy as np

x = 1.96
0.5 * (1 + special.erf(x / np.sqrt(2)))   # 0.9750021048517795
special.ndtr(x)                            # 0.9750021048517795  (same, built in)
```

So 97.5% of a normal distribution lies below 1.96 standard deviations, which is the well-known 95% confidence interval.

**Engineering uses:** heat conduction in a semi-infinite solid (the temperature profile involves erfc), diffusion problems, and error-rate calculations in communications.

### 3. Bessel functions

Bessel functions solve the differential equation:

x² y″ + x y′ + (x² − ν²) y = 0

They are like sine and cosine, but for **cylindrical and circular geometry**. Think of them as oscillating waves whose amplitude slowly decays.

| Function | Name | Behaviour |
|---|---|---|
| `jv(v, x)` or `jn(n, x)` | Bessel of the first kind, Jν(x) | oscillates, finite at 0 |
| `yv(v, x)` | Bessel of the second kind, Yν(x) | oscillates, blows up at 0 |
| `iv(v, x)` | modified, first kind, Iν(x) | grows exponentially |
| `kv(v, x)` | modified, second kind, Kν(x) | decays exponentially |

```python
special.jv(0, 0)       # 1.0
special.jv(0, 2.4048)  # ~0  (close to the first zero)
special.j0(1.0)        # 0.7651976865579666  (shortcut for order 0)
special.j1(1.0)        # 0.44005058574493355 (shortcut for order 1)
```

### 4. Zeros of Bessel functions

Often you need the points where Jν(x) = 0.

```python
special.jn_zeros(0, 3)   # array([2.40482556, 5.52007811, 8.65372791])
```

### 5. Worked example: a circular drum

A circular membrane of radius R vibrates at frequencies proportional to the zeros of Bessel functions. The fundamental mode comes from the first zero of J₀ (≈ 2.405).

```python
import numpy as np
from scipy import special

R = 0.2          # radius in meters
c = 100.0        # wave speed in m/s (depends on tension and density)

zeros = special.jn_zeros(0, 4)       # first 4 zeros of J0
freqs = c * zeros / (2 * np.pi * R)  # frequencies in Hz
print(freqs)
```

Each zero gives one vibration mode. This is a real mechanical engineering application. Bessel functions also appear in heat flow in cylinders, vibration of shafts and discs, and electromagnetic waves in circular waveguides.

### 6. Other functions worth knowing

- `special.ellipk`, `special.ellipe`: elliptic integrals (pendulum with large swing angle).
- `special.airy`: Airy functions (quantum mechanics, optics).
- `special.fresnel`: Fresnel integrals (diffraction, road and rail curve design).

### Lesson 1.2 Exercises

1. Plot `erf(x)` and `erfc(x)` for x from −3 to 3 and confirm they add up to 1.
2. Compute `1 - special.erf(8)` and `special.erfc(8)`. Compare them and explain the difference.
3. Plot J₀, J₁ and J₂ on the same graph for x from 0 to 20.
4. Compute the first 5 vibration frequencies of the drum above for R = 0.1 m.

---

## Lesson 1.3: Numerically Stable Helpers (`logsumexp`, `expit`, `softmax`)

### 1. The idea

The math is correct on paper, but computers use finite-precision floats. Large exponentials overflow and tiny ones underflow. These helpers compute the same math without breaking. They matter a lot in machine learning and probability.

### 2. `logsumexp`

Goal: compute **ln(e^a + e^b + e^c + ...)**.

The naive way fails:

```python
import numpy as np

a = np.array([1000, 1000, 1000])
np.log(np.sum(np.exp(a)))   # inf  (exp(1000) overflows)
```

The stable way:

```python
from scipy.special import logsumexp

logsumexp(a)   # 1001.0986122886681
```

**The trick it uses:** pull out the maximum m, so ln(Σ eˣⁱ) = m + ln(Σ e^(xᵢ − m)). Now the biggest exponent is 0, and nothing overflows.

Check: 1000 + ln(3) = 1001.0986..., which matches.

It also works along axes:

```python
M = np.array([[1, 2, 3],
              [4, 5, 6]])
logsumexp(M, axis=1)   # one result per row
```

### 3. `expit` and `logit` (the sigmoid pair)

**expit(x) = 1 / (1 + e^(−x))**, the sigmoid used in logistic regression and neural networks.
**logit(p) = ln(p / (1 − p))**, its inverse.

```python
from scipy.special import expit, logit

expit(0)        # 0.5
expit(2)        # 0.8807970779778823
expit(-1000)    # 0.0  (no overflow warning)
logit(0.5)      # 0.0
logit(0.88)     # about 1.9924
```

A hand-written `1/(1+np.exp(-x))` gives an overflow warning for very negative x. `expit` is safe for any input.

### 4. `softmax` and `log_softmax`

Softmax converts a list of raw scores into probabilities that sum to 1:

**softmax(xᵢ) = e^(xᵢ) / Σ e^(xⱼ)**

```python
from scipy.special import softmax, log_softmax

scores = np.array([1.0, 2.0, 3.0])
softmax(scores)       # array([0.09003057, 0.24472847, 0.66524096])
softmax(scores).sum() # 1.0

softmax([1000, 1001, 1002])   # works fine: [0.09003057, 0.24472847, 0.66524096]
```

The same output appears for [1, 2, 3] and [1000, 1001, 1002] because softmax only depends on differences between scores. SciPy subtracts the max internally, so it never overflows.

`log_softmax` gives ln(softmax) directly, which is more accurate for classification losses.

### 5. Other small but valuable helpers

| Function | Purpose |
|---|---|
| `log1p(x)` | ln(1 + x), accurate for tiny x |
| `expm1(x)` | eˣ − 1, accurate for tiny x |
| `xlogy(x, y)` | x · ln(y), returns 0 when x = 0 |
| `entr(x)` | −x ln(x), the entropy term |

```python
np.log(1 + 1e-16)       # 0.0   (wrong!)
np.log1p(1e-16)         # 1e-16 (correct)
```

### 6. Worked example: classification probabilities

```python
import numpy as np
from scipy.special import softmax, logsumexp

logits = np.array([2.0, 1.0, 0.1])   # raw model outputs
probs = softmax(logits)
print(probs)                         # about [0.659, 0.242, 0.099]

# cross-entropy loss if the true class is index 0:
loss = -(logits[0] - logsumexp(logits))
print(loss)                          # about 0.417
```

This is exactly how deep-learning frameworks compute their loss.

### Lesson 1.3 Exercises

1. Compute `logsumexp([-1000, -1000])` and explain why the naive formula returns `-inf`.
2. Plot `expit(x)` from −10 to 10 and mark where it equals 0.5.
3. Verify `logit(expit(x)) == x` for x = 3.2.
4. Compute softmax for [5, 5, 5, 5]. What do you expect, and why?
5. Show that adding a constant to all scores does not change the softmax output.

---

## Module 1 Mini-Project: `special_toolkit.py`

Build a small command-line tool that:

1. Takes n and k and prints n!, `comb(n, k)` and `perm(n, k)`, plus the log-factorial when n is large.
2. Takes x and prints erf, erfc and the normal CDF.
3. Takes a list of scores and prints softmax probabilities and `logsumexp`.
4. Takes a radius and prints the first 5 drum frequencies.

## Suggested Folder Layout

```
01-special-functions/
├── README.md
├── lesson-1.1-gamma-beta-combinatorics.md
├── lesson-1.2-erf-bessel.md
├── lesson-1.3-stable-helpers.md
├── examples/
│   ├── gamma_demo.py
│   ├── drum_frequencies.py
│   └── softmax_demo.py
├── exercises/
│   └── exercises.md
└── project/
    └── special_toolkit.py
```

## Key Takeaways

- Γ(n) = (n−1)!, and `gammaln` prevents overflow for big values.
- Use `comb` and `perm` with `exact=True` for exact integers.
- `erfc` keeps accuracy in the tails where `1 - erf` fails.
- Bessel functions are the "sine and cosine" of circular geometry, and `jn_zeros` gives vibration modes.
- `logsumexp`, `expit` and `softmax` are the stable way to compute exponentials of big numbers.

**Next:** Module 2: Linear Algebra (`scipy.linalg`)
