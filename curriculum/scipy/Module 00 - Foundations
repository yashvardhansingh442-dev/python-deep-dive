# Module 0: Foundations

> Part of the SciPy Course. Prerequisites: basic Python (variables, functions, loops, lists).

## Module Overview

| Lesson | Topic |
|---|---|
| 0.1 | What SciPy is, how it relates to NumPy, and its submodule map |
| 0.2 | Installation, environment setup, and the NumPy refresher (arrays, broadcasting, vectorization) |
| 0.3 | Reading the SciPy docs, and constants and units (`scipy.constants`) |

---

## Lesson 0.1: What SciPy Is, NumPy, and the Submodule Map

### 1. The scientific Python stack

Python by itself is slow for number crunching and has no built-in matrices. The scientific community built a stack of libraries on top of it:

| Library | Role |
|---|---|
| **NumPy** | Fast N-dimensional arrays and basic math on them |
| **SciPy** | Scientific algorithms built on NumPy arrays (optimization, integration, statistics, signals...) |
| **Matplotlib** | Plotting |
| **pandas** | Tables and data analysis |
| **scikit-learn** | Machine learning (uses SciPy internally) |

Think of it like this:

- NumPy gives you the **data container** (the array) and the basic operations.
- SciPy gives you the **algorithms** that work on that container.

### 2. NumPy vs SciPy: where is the line?

| | NumPy | SciPy |
|---|---|---|
| Purpose | Array object, indexing, basic math, basic linear algebra, basic FFT | Advanced, specialized algorithms |
| Example | `np.sum`, `np.dot`, `np.linalg.solve` | `optimize.minimize`, `integrate.solve_ivp`, `stats.ttest_ind` |
| Depends on | Nothing (C core) | NumPy |

Some things exist in both (`numpy.linalg` and `scipy.linalg`, `numpy.fft` and `scipy.fft`). The SciPy versions are usually more complete and faster, because SciPy is always compiled with LAPACK and BLAS (the standard numerical libraries).

### 3. Under the hood

SciPy is mostly a friendly Python layer over battle-tested compiled code written in **Fortran, C and C++** (LAPACK, BLAS, ARPACK, QUADPACK, ODEPACK and others). When you call `scipy.optimize.minimize`, the heavy lifting runs in compiled code. That is why SciPy is fast while still being easy to write.

### 4. The submodule map

SciPy is organized into **submodules**. Each one covers one area.

| Submodule | What it does | Our module |
|---|---|---|
| `scipy.special` | Special functions (gamma, erf, Bessel) | Module 1 |
| `scipy.linalg` | Linear algebra | Module 2 |
| `scipy.sparse` | Sparse matrices, sparse solvers, graphs | Module 3 |
| `scipy.optimize` | Minimization, root finding, curve fitting | Module 4 |
| `scipy.integrate` | Integration and ODE solvers | Module 5 |
| `scipy.interpolate` | Interpolation and splines | Module 6 |
| `scipy.stats` | Distributions and statistical tests | Module 7 |
| `scipy.signal` | Signal processing and filters | Module 8 |
| `scipy.fft` | Fourier transforms | Module 9 |
| `scipy.ndimage` | Image processing | Module 10 |
| `scipy.spatial` | Distances, KD-trees, hulls, rotations | Module 11 |
| `scipy.cluster` | K-means and hierarchical clustering | Module 12 |
| `scipy.io` | Reading and writing files (MATLAB, WAV) | Module 13 |
| `scipy.constants` | Physical constants and unit conversions | Lesson 0.3 |

### 5. How to import

Import the submodule you need, not just `import scipy`:

```python
from scipy import optimize
from scipy import stats
import scipy.linalg as sla     # alias style

# or import single functions
from scipy.optimize import minimize
```

Good habit: import explicitly so your code works on every SciPy version and your readers can see what you use.

### 6. A tiny taste

```python
from scipy import optimize

# find the minimum of f(x) = (x - 3)^2 + 1
result = optimize.minimize_scalar(lambda x: (x - 3)**2 + 1)
print(result.x)     # about 3.0
print(result.fun)   # about 1.0
```

One line to minimize a function. That is the SciPy philosophy: you describe the problem, and SciPy brings the algorithm.

### Lesson 0.1 Exercises

1. Without looking, list five SciPy submodules and one job each does.
2. Which submodule would you use for: (a) fitting a curve to experimental data, (b) solving a differential equation, (c) running a t-test, (d) filtering noise from a sensor signal?
3. Run `import scipy; print(scipy.__version__)` and note your version.

---

## Lesson 0.2: Installation, Environment Setup and the NumPy Refresher

### 1. Installing

Always use a **virtual environment** so each project has its own packages.

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
pip install numpy scipy matplotlib
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install numpy scipy matplotlib
```

Optional but recommended for this course:

```bash
pip install jupyter
```

Verify it worked:

```python
import numpy as np
import scipy
import matplotlib
print(np.__version__, scipy.__version__, matplotlib.__version__)
```

Tip: save your dependencies for the repo.

```bash
pip freeze > requirements.txt
```

### 2. Suggested repo setup

```
scipy-course/
├── README.md
├── requirements.txt
├── 00-foundations/
├── 01-special-functions/
└── ...
```

Add a `.gitignore` containing `.venv/`, `__pycache__/` and `.ipynb_checkpoints/` so you never commit them.

### 3. NumPy refresher: the array

A NumPy array holds numbers of one type in a fixed-size grid, stored compactly in memory.

```python
import numpy as np

a = np.array([1, 2, 3, 4])
print(a.shape)    # (4,)
print(a.dtype)    # int64 (platform dependent)
print(a.ndim)     # 1

M = np.array([[1, 2, 3],
              [4, 5, 6]])
print(M.shape)    # (2, 3)  -> 2 rows, 3 columns
```

Handy creators:

```python
np.zeros((2, 3))          # 2x3 of zeros
np.ones(4)                # [1. 1. 1. 1.]
np.arange(0, 10, 2)       # [0 2 4 6 8]
np.linspace(0, 1, 5)      # [0.   0.25 0.5  0.75 1.  ]
np.eye(3)                 # 3x3 identity matrix
np.random.default_rng(0).random(3)   # reproducible random numbers
```

`arange` steps by a size, `linspace` gives an exact number of points. You will use `linspace` constantly for plotting and solving.

### 4. Indexing and slicing

```python
a = np.array([10, 20, 30, 40, 50])
a[0]        # 10
a[-1]       # 50
a[1:4]      # [20 30 40]
a[::2]      # [10 30 50]

M = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
M[0, 1]     # 2        (row 0, column 1)
M[1]        # [4 5 6]  (row 1)
M[:, 2]     # [3 6 9]  (column 2)
M[0:2, 1:]  # [[2 3] [5 6]]
```

**Boolean masks** select elements by condition:

```python
a = np.array([3, 8, 1, 9, 4])
a[a > 3]            # [8 9 4]
a[(a > 2) & (a < 9)]  # [3 8 4]   (use & and |, with brackets)
```

Warning: slices are **views**, not copies. Changing a slice changes the original. Use `.copy()` when you need an independent array.

### 5. Axes

For a 2D array, `axis=0` runs **down the rows** (one result per column) and `axis=1` runs **across the columns** (one result per row).

```python
M = np.array([[1, 2, 3],
              [4, 5, 6]])
M.sum()          # 21
M.sum(axis=0)    # [5 7 9]   (column sums)
M.sum(axis=1)    # [ 6 15]   (row sums)
M.mean(axis=0)   # [2.5 3.5 4.5]
```

This same `axis` idea appears all over SciPy (`logsumexp`, `stats.zscore`, `fft` and many others).

### 6. Vectorization

**Vectorization** means doing an operation on a whole array at once, instead of looping in Python.

```python
import numpy as np

x = np.linspace(0, 10, 1_000_000)

# slow way
y_slow = [xi**2 + 1 for xi in x]

# fast way (vectorized)
y_fast = x**2 + 1
```

The vectorized version runs in compiled code and is typically 10 to 100 times faster. Rule: **if you are writing a `for` loop over array elements, look for a vectorized alternative first.**

Math functions work element by element:

```python
np.sin(x)
np.exp(-x)
np.sqrt(x)
```

### 7. Broadcasting

Broadcasting lets NumPy combine arrays of **different shapes** without copying data.

```python
a = np.array([1, 2, 3])
a + 10            # [11 12 13]   scalar stretched to match
```

Rules (compare shapes from the right):

1. Dimensions are compatible if they are equal, or one of them is 1.
2. A dimension of 1 is stretched to match the other.

```python
col = np.array([[0], [10], [20]])    # shape (3, 1)
row = np.array([1, 2, 3, 4])         # shape (4,)

col + row
# shape (3, 4):
# [[ 1  2  3  4]
#  [11 12 13 14]
#  [21 22 23 24]]
```

Shapes `(3, 1)` and `(4,)` become `(3, 4)`. A shape pair like `(3,)` and `(4,)` fails because neither dimension is 1 and they are not equal.

Common use: subtract each column's mean from a table.

```python
data = np.array([[1., 2.], [3., 4.], [5., 6.]])
centered = data - data.mean(axis=0)
```

### 8. Linear algebra basics in NumPy (needed for Module 2)

```python
A = np.array([[2., 1.], [1., 3.]])
b = np.array([1., 2.])

A @ b                       # matrix-vector product
A.T                         # transpose
np.linalg.solve(A, b)       # solve A x = b
```

`@` is the matrix multiplication operator. `*` is element-by-element multiplication, which is a very common beginner mix-up.

### 9. Plotting basics (used throughout the course)

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 200)
plt.plot(x, np.sin(x), label="sin(x)")
plt.plot(x, np.cos(x), label="cos(x)")
plt.xlabel("x")
plt.ylabel("value")
plt.legend()
plt.grid(True)
plt.show()
```

### Lesson 0.2 Exercises

1. Create a 4x4 array with values 1 to 16, then extract: the second column, the bottom-right 2x2 block, and all elements greater than 10.
2. Compute the row sums and column sums of that array.
3. Time a loop vs a vectorized version of `x**2 + 3*x` for 1 million values (use `time.perf_counter`).
4. Build a multiplication table (1 to 9 by 1 to 9) using broadcasting, with no loops.
5. Explain why shapes `(2, 3)` and `(2,)` fail to broadcast, and what small change would make them work.

---

## Lesson 0.3: Reading the Docs and `scipy.constants`

### 1. How to read SciPy documentation

The official docs are at the SciPy website under "API reference". Every function page has the same layout:

| Section | What to look for |
|---|---|
| **Signature** | The function name and its parameters, with defaults |
| **Parameters** | What each argument means, its type and shape |
| **Returns** | What comes back (often an object with several fields) |
| **Notes** | The algorithm, assumptions, and caveats |
| **References** | Papers behind the method |
| **Examples** | Runnable code you can copy and test |

Reading approach: **Examples first, then Parameters, then Notes.**

### 2. Help inside Python

```python
from scipy import optimize

help(optimize.minimize)      # full docstring in the terminal
optimize.minimize?           # in Jupyter or IPython
dir(optimize)                # list everything in the submodule
```

In VS Code, hover over a function to see its signature and docstring.

### 3. Result objects

Many SciPy functions return a **result object** with named fields rather than a bare number.

```python
from scipy import optimize

res = optimize.minimize_scalar(lambda x: (x - 3)**2 + 1)
print(res.x)         # where the minimum is
print(res.fun)       # the minimum value
print(res.success)   # did it converge?
print(res)           # shows all fields
```

Always check `success` (or `message`) on solvers. A solver can finish without actually finding an answer.

### 4. Physical constants: `scipy.constants`

```python
from scipy import constants

constants.c          # speed of light, 299792458.0 m/s
constants.g          # standard gravity, 9.80665 m/s^2
constants.pi         # 3.141592653589793
constants.h          # Planck constant, 6.62607015e-34 J s
constants.k          # Boltzmann constant, 1.380649e-23 J/K
constants.G          # gravitational constant, about 6.674e-11 N m^2 / kg^2
constants.N_A        # Avogadro constant, about 6.022e23 1/mol
constants.R          # gas constant, about 8.314 J/(mol K)
```

All values are in **SI units**.

### 5. The `physical_constants` dictionary

For hundreds of constants, use the dictionary. Each entry is `(value, unit, uncertainty)`.

```python
from scipy import constants

constants.physical_constants["electron mass"]
# (value, 'kg', uncertainty)

constants.value("electron mass")        # just the value, about 9.109e-31
constants.unit("electron mass")         # 'kg'
constants.precision("electron mass")    # relative uncertainty
```

Search for a name:

```python
constants.find("mass")      # list of all constant names containing "mass"
```

Note: exact digits depend on the CODATA release shipped with your SciPy version, so values may differ in later decimals between versions.

### 6. Unit conversion constants

Every unit constant equals **how many SI base units one of that unit is**.

```python
constants.inch        # 0.0254      (meters)
constants.foot        # 0.3048      (meters)
constants.mile        # 1609.344    (meters)
constants.pound       # 0.45359237  (kilograms)  (mass pound, lb)
constants.atm         # 101325.0    (pascals)
constants.bar         # 100000.0    (pascals)
constants.psi         # 6894.757... (pascals)
constants.hp          # 745.699...  (watts)
constants.hour        # 3600.0      (seconds)
constants.degree      # 0.01745...  (radians, pi/180)
```

So to convert, **multiply to go to SI, divide to come back**:

```python
# 60 mph in m/s
speed_ms = 60 * constants.mile / constants.hour
print(speed_ms)                 # about 26.82

# 3000 psi in MPa
p_pa = 3000 * constants.psi
print(p_pa / constants.mega)    # about 20.68

# 5 horsepower in kW
print(5 * constants.hp / constants.kilo)   # about 3.73
```

### 7. Metric prefixes

```python
constants.kilo    # 1e3
constants.mega    # 1e6
constants.giga    # 1e9
constants.milli   # 1e-3
constants.micro   # 1e-6
constants.nano    # 1e-9
```

### 8. Temperature conversion

Temperature needs an offset, not just a multiplier, so there is a dedicated function:

```python
constants.convert_temperature(100, "Celsius", "Fahrenheit")   # 212.0
constants.convert_temperature(0, "Celsius", "Kelvin")         # 273.15
constants.convert_temperature(300, "Kelvin", "Celsius")       # 26.85
```

### 9. Worked example: ideal gas

How many moles of gas are in a 2.0 litre container at 1 atm and 25 degrees C?

```python
from scipy import constants

P = 1 * constants.atm                                     # Pa
V = 2.0 * constants.liter                                 # m^3
T = constants.convert_temperature(25, "Celsius", "Kelvin")   # K

n = P * V / (constants.R * T)
print(n)     # about 0.0817 mol
```

Notice that units were converted to SI **before** using the formula. This habit prevents most engineering calculation mistakes.

### Lesson 0.3 Exercises

1. Compute the energy in joules of a photon with wavelength 500 nm using `E = h c / wavelength`.
2. Convert 120 km/h to m/s and to mph using `scipy.constants`.
3. Find the weight (in newtons) of a 75 kg person, then express it in pound-force (`constants.pound_force`).
4. Use `constants.find("proton")` and print the value and unit of the proton mass.
5. Convert body temperature 98.6 F to Celsius and Kelvin.

---

## Module 0 Mini-Project: `unit_helper.py`

Build a small command-line tool that:

1. Converts a value between common units (length, pressure, power, speed) using `scipy.constants`.
2. Converts temperatures between Celsius, Fahrenheit and Kelvin.
3. Looks up any physical constant by search text and prints its value, unit and uncertainty.
4. Prints the ideal gas moles for user-supplied pressure, volume and temperature.

## Suggested Folder Layout

```
00-foundations/
├── README.md
├── lesson-0.1-what-is-scipy.md
├── lesson-0.2-setup-and-numpy.md
├── lesson-0.3-docs-and-constants.md
├── examples/
│   ├── first_minimize.py
│   ├── broadcasting_demo.py
│   └── ideal_gas.py
├── exercises/
│   └── exercises.md
└── project/
    └── unit_helper.py
```

## Key Takeaways

- NumPy is the array container, SciPy is the algorithm library built on top of it.
- Import specific submodules (`from scipy import optimize`) rather than relying on `import scipy`.
- Use a virtual environment and a `requirements.txt` for every project.
- Vectorize instead of looping, and use `axis` and broadcasting to work on whole arrays.
- Read docs as Examples, then Parameters, then Notes, and always check `success` on solver results.
- `scipy.constants` gives SI-based constants and unit factors: multiply to convert into SI, divide to convert out.

**Next:** Module 1: Special Functions (`scipy.special`)
