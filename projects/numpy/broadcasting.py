import numpy as np

#broadcasting allows numpy to perform operations on arrays of different shapes. 
# It automatically expands the smaller array to match the shape of the larger array.

#The dimensions have the same size, or one of the dimensions is 1. 
# In this case, the smaller array is "stretched" to match the larger array.

array1 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8]])
array2 = np.array([[1], [2], [3], [4]])
print("This is the first array: ", array1)
print("This is the second array: ", array2)

#The shape of the array is determined by the number of rows and columns.
#First row and then column. 
#The shape of the first array is (1, 4) and the shape of the second array is (4, 1).
print("Shape of the first array: ", array1.shape)
print("Shape of the second array: ", array2.shape)
print(array1 * array2)  
#The result is a 4x4 array where each element is the product of the corresponding elements in the two arrays.
