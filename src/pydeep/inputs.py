"""Validated console input helpers.

Extracted from projects/numpy/SpendSense.py. Each helper keeps asking until
the input is valid. ``input_fn`` and ``output_fn`` can be replaced, which is
what makes these functions testable without a real keyboard.
"""

import math
from collections.abc import Callable

InputFn = Callable[[str], str]
OutputFn = Callable[[str], None]


def read_days(input_fn: InputFn = input, output_fn: OutputFn = print) -> int:
    """Ask for a number of days until a positive whole number is given."""
    while True:
        raw = input_fn("How many days of expenses will you enter? ").strip()
        # isascii() matters: str.isdigit() is True for characters such as "²"
        # that int() cannot convert.
        if raw.isascii() and raw.isdigit() and int(raw) > 0:
            return int(raw)
        output_fn("Please enter a whole number greater than 0.")


def read_numbers(
    prompt: str,
    expected: int,
    input_fn: InputFn = input,
    output_fn: OutputFn = print,
) -> list[float]:
    """Read numbers separated by commas and/or spaces, e.g. '80, 90 100'.

    Keeps asking until the input is valid: exactly ``expected`` finite,
    non-negative numbers.
    """
    while True:
        parts = input_fn(prompt).replace(",", " ").split()
        try:
            values = [float(p) for p in parts]
        except ValueError:
            output_fn("Please enter numbers only, separated by commas or spaces.")
            continue
        if not all(math.isfinite(v) for v in values):
            output_fn("'nan' and 'inf' are not valid amounts.")
            continue
        if len(values) != expected:
            output_fn(f"You entered {len(values)} values, but need exactly {expected}.")
            continue
        if any(v < 0 for v in values):
            output_fn("Expenses cannot be negative.")
            continue
        return values


def read_income(input_fn: InputFn = input, output_fn: OutputFn = print) -> float:
    """Ask for a monthly income until a finite, non-negative number is given."""
    while True:
        try:
            income = float(input_fn("Enter your monthly income: ").strip())
        except ValueError:
            output_fn("Please enter a number.")
            continue
        if not math.isfinite(income):
            output_fn("'nan' and 'inf' are not valid amounts.")
            continue
        if income < 0:
            output_fn("Income cannot be negative.")
            continue
        return income
