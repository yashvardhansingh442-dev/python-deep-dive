
import numpy as np

# Create a 3D NumPy array containing alphabets.
array = np.array([
    [["A", "B", "C"],
     ["D", "E", "F"],
     ["G", "H", "I"]],

    [["J", "K", "L"],
     ["M", "N", "O"],
     ["P", "Q", "R"]],

    [["S", "T", "U"],
     ["V", "W", "X"],
     ["Y", "Z", " "]]
])

# Extract individual characters using 3D indexing.
# Indexing format: array[depth, row, column]

word = (
    array[1, 2, 0] +  # P
    array[1, 2, 2] +  # R
    array[0, 2, 2] +  # I
    array[2, 0, 0] +  # S
    array[0, 2, 1] +  # H
    array[2, 2, 2] +  # Space
    array[0, 2, 2] +  # I
    array[2, 2, 2] +  # Space
    array[1, 0, 2] +  # L
    array[1, 1, 2] +  # O
    array[2, 1, 0] +  # V
    array[0, 1, 1] +  # E
    array[2, 2, 2] +  # Space
    array[2, 2, 0] +  # Y
    array[1, 1, 2] +  # O
    array[2, 0, 2]    # U
)

# Print the final combined string.
print(word)
