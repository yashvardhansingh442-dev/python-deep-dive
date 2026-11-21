
import numpy as np

# Create a random number generator.
# Using a seed ensures that the same random numbers are generated every time.
rng = np.random.default_rng(seed=42)

# Generate a random integer between 1 and 5 (inclusive).
print("Random Dice Roll:", rng.integers(low=1, high=6))

# Generate 5 random integers between 1 and 99.
# size=(5, 1) creates an array with 5 rows and 1 column.
random_numbers = rng.integers(low=1, high=100, size=(5, 1))
print("Random Numbers:", random_numbers)

# Generate 5 random floating-point numbers between 0 and 1.
random_floats = rng.random(size=5)
print("Random Floats:", random_floats)
