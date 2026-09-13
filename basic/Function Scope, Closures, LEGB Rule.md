# Function Scope, Closures, LEGB Rule

## Concept: The LEGB Rule

Python resolves variable names by searching four scopes in order: **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in.

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)   # "local" — found in Local scope first

    inner()
    print(x)   # "enclosing" — outer's own local scope

print(x)   # "global"
```

If `inner()` didn't define its own `x`, Python looks up to the Enclosing scope, then Global, then Built-in.

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        print(x)   # no local x -> looks up to enclosing -> "enclosing"

    inner()

outer()
```

---

## `global` and `nonlocal`

```python
count = 0

def increment():
    global count
    count += 1   # without 'global', this raises UnboundLocalError

increment()
print(count)   # 1
```

```python
def outer():
    x = 10

    def inner():
        nonlocal x
        x += 5   # modifies outer's x, not a new local variable

    inner()
    print(x)   # 15

outer()
```

---

## Build Task: Closure-Based Counter Function

A **closure** is a function that "remembers" variables from its enclosing scope even after the outer function has finished running.

```python
def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


if __name__ == "__main__":
    c1 = make_counter()
    c2 = make_counter()   # independent closure — separate 'count'

    print(c1())   # 1
    print(c1())   # 2
    print(c1())   # 3
    print(c2())   # 1  -> c2 has its own count, unaffected by c1
```

Each call to `make_counter()` creates a fresh `count` variable, and `counter()` closes over that specific variable — that's the closure.

---

## LeetCode #9 — Palindrome Number

```python
def is_palindrome(x):
    if x < 0:
        return False
    original = x
    reversed_num = 0
    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10
    return original == reversed_num


if __name__ == "__main__":
    print(is_palindrome(121))    # True
    print(is_palindrome(-121))   # False (negative can't be palindrome)
    print(is_palindrome(10))     # False
    print(is_palindrome(12321))  # True
```

---

## Quick Reference

| Concept | Key takeaway |
|---|---|
| LEGB | Local → Enclosing → Global → Built-in lookup order |
| `global` | Modify a global variable from inside a function |
| `nonlocal` | Modify an enclosing (not global) variable from a nested function |
| Closure | Inner function remembers variables from its enclosing scope after the outer function returns |

---

