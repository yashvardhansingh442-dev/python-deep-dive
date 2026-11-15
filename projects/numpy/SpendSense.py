"""This is a simple Python script that demonstrates basic functionality for a spending analysis tool. 
It allows users to input their expenses, categorize them, and generate a summary report of their spending habits."""

import numpy as np

CATEGORIES = ["Food", "Transportation", "Entertainment", "Bills"]


def read_days():
    """Ask for the number of days until a positive whole number is given."""
    while True:
        raw = input("How many days of expenses will you enter? ").strip()
        if raw.isdigit() and int(raw) > 0:
            return int(raw)
        print("Please enter a whole number greater than 0.")


def read_numbers(prompt, expected):
    """Read numbers separated by commas and/or spaces, e.g. '80, 90 100'.

    Keeps asking until the input is valid: only non-negative numbers,
    and exactly `expected` of them. Returns a float NumPy array.
    """
    while True:
        parts = input(prompt).replace(",", " ").split()
        try:
            values = np.array([float(p) for p in parts])
        except ValueError:
            print("Please enter numbers only, separated by commas or spaces.")
            continue
        if len(values) != expected:
            print(f"You entered {len(values)} values, but need exactly {expected}.")
            continue
        if (values < 0).any():
            print("Expenses cannot be negative.")
            continue
        return values


def read_income():
    """Ask for monthly income until a valid non-negative number is given."""
    while True:
        try:
            income = float(input("Enter your monthly income: ").strip())
        except ValueError:
            print("Please enter a number.")
            continue
        if income < 0:
            print("Income cannot be negative.")
            continue
        return income


name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to SpendSense, your personal spending analysis tool.")
print("Here we will help you track your expenses and understand your spending habits better.\n")

days = read_days()
print(f"\nFor each category, enter {days} daily amounts separated by commas or spaces.")
print("Enter 0 for days with no spending.\n")

columns = [read_numbers(f"{cat} expenses: ", days) for cat in CATEGORIES]

expenses = np.column_stack(columns)   # shape: (days, categories)
income = read_income()

print("\nShape of expense data:", expenses.shape)
print("First 3 days:\n", expenses[:3])