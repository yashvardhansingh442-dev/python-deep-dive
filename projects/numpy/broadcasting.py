import numpy as np

#broadcasting allows numpy to perform operations on arrays of different shapes. 
# It automatically expands the smaller array to match the shape of the larger array.

#The dimensions have the same size, or one of the dimensions is 1. 
# In this case, the smaller array is "stretched" to match the larger array.

array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1], [2], [3], [4]])
print("This is the first array: ", array1)
print("This is the second array: ", array2)
