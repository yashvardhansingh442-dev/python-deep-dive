import numpy as np

# Filtering is used to extract elements from an array based on a condition.

# Create a 2D array containing different ages.
ages = np.array([[11, 21, 37, 58, 45, 99],
                 [15, 36, 9, 12, 18, 25]])

# Extract ages which are in teen like thirteen fifteen etc.
teenagers = ages[(ages < 21) & (ages >= 13)]

# Extract ages between 21 and 45 (inclusive).
adults = ages[(ages >= 21) & (ages <= 45)]

# Print the original array.
print("The Original array:", ages)

# Print all teenagers.
print("The teenagers are:", teenagers)

# Print all adults.
print("The adults are:", adults)

# Extract and print ages above 45.
print("The senior citizens are:", ages[ages > 45])

# Extract all even ages (divisible by 2).
even_ages = ages[ages % 2 == 0]
print("The even ages are:", even_ages)

# Extract all odd ages (not divisible by 2).
odd_ages = ages[ages % 2 != 0]
print("The odd ages are:", odd_ages)

# Keep the age 18 and replace all other values with 0.
sigma = np.where(ages == 18, ages, 0)
print("Using np.where():", sigma)
