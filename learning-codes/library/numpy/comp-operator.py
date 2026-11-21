import numpy as np

# Create a NumPy array containing student scores.
score = np.array([55, 24, 73, 14, 100, 68, 80, 60])

# Print the original score array.
print("This is the score array:", score)

# Check which scores are equal to 100.
print("Scores equal to 100:", score == 100)

# Check which scores are greater than or equal to 60.
print("Passing scores (60 or above):", score >= 60)

# Check which scores are less than 40.
print("Scores less than 40:", score < 40)
