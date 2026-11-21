import numpy as np

# Broadcasting allows NumPy to perform operations on arrays of different shapes.
# NumPy automatically expands the smaller dimensions when necessary.

# Broadcasting works when dimensions are equal or one of them is 1.

# Create a 2D array with 1 row and 4 columns.
array1 = np.array([[1, 2, 3, 4]])

# Create a 2D array with 4 rows and 1 column.
array2 = np.array([[1], [2], [3], [4]])

# Print both arrays.
print("This is the first array:", array1)
print("This is the second array:", array2)

# Display the shape (rows, columns) of each array.
print("Shape of the first array:", array1.shape)
print("Shape of the second array:", array2.shape)

# Multiply both arrays using broadcasting.
# The result is a 4x4 array.
print("Multiplication result:\n", array1 * array2)


# Create another array with 1 row and 10 columns.
array_a = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])

# Create another array with 10 rows and 1 column.
array_b = np.array([
    [1], [2], [3], [4], [5],
    [6], [7], [8], [9], [10]
])

# Print both arrays.
print("This is the first array:", array_a)
print("This is the second array:", array_b)

# Display the shape of both arrays.
print("Shape of the first array:", array_a.shape)
print("Shape of the second array:", array_b.shape)

# Multiply both arrays using broadcasting.
# The result is a 10x10 array.
print("Multiplication result:\n", array_a * array_b)
