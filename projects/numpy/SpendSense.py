"""SpendSense: a small spending-analysis script.

Collects daily expenses per category plus a monthly income, and stores them
in a NumPy array. A summary report is planned but not written yet.

The input helpers live in the reusable package (src/pydeep/inputs.py), so run
`make install` first.
"""

import numpy as np

from pydeep.inputs import read_days, read_income, read_numbers

CATEGORIES = ["Food", "Transportation", "Entertainment", "Bills"]


def main() -> None:
    name = input("Enter your name: ")
    print(
        f"Hello, {name}! Welcome to SpendSense, your personal spending analysis tool."
    )
    print("Here we will help you track your expenses and understand your spending.\n")

    days = read_days()
    print(
        f"\nFor each category, enter {days} daily amounts "
        "separated by commas or spaces."
    )
    print("Enter 0 for days with no spending.\n")

    columns = [np.array(read_numbers(f"{cat} expenses: ", days)) for cat in CATEGORIES]

    expenses = np.column_stack(columns)  # shape: (days, categories)
    _income = read_income()  # not used yet; the summary report will need it

    print("\nShape of expense data:", expenses.shape)
    print("First 3 days:\n", expenses[:3])


if __name__ == "__main__":
    main()
