
import numpy as np

# Create a 1D NumPy array.
array = np.array([1, 2, 3, 4])

# Create a 2D NumPy array with 1 row and 4 columns.
arr = np.array([[5, 6, 7, 8]])

# Multiply every element of the first array by 2.
array = array * 2

# Print the modified array.
print("Modified array:", array)

# Check the data type of the array.
print("Data type:", type(array))

# Check the number of dimensions in the first array.
print("Dimensions of array:", array.ndim)  # Output: 1

# Check the number of dimensions in the second array.
print("Dimensions of arr:", arr.ndim)  # Output: 2
