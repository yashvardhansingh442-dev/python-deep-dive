import numpy as np

# Create a 3D NumPy array containing alphabets.
array = np.array([
    [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]],
    [["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R"]],
    [["S", "T", "U"], ["V", "W", "X"], ["Y", "Z", " "]]
])

# ndim tells us how many dimensions the array has.
print(array.ndim)  # Output: 3

# shape tells us the size of the array in each dimension.
print(array.shape)  # Output: (3, 3, 3)
