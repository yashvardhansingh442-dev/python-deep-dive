import numpy as np

#element wise arithmetic operations

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print("This is the first array: ", array1)
print("This is the second array: ", array2)
print("The sum of the two arrays is: ", array1 + array2) #array addition every element of the first array is added to the corresponding element of the second array
print("The difference of the two arrays is: ", array1 - array2) #array subtraction every element of the first array is subtracted by the corresponding element of the second array
print("The product of the two arrays is: ", array1 * array2) #array multiplication every element of the first array is multiplied by the corresponding element of the second array
print("The quotient of the two arrays is: ", array1 / array2) #array division every element of the first array is divided by the corresponding element of the second array
print("The exponentiation of the two arrays is: ", array1 ** array2) #array exponentiation every element of the first array is raised to the power of the corresponding element of the second array
