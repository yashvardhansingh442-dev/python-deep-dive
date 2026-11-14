import numpy as np

#vectorized math functions

array = np.array([1, 2, 3])
print("This is the original array:", array)

print("Square root of the array:", np.sqrt(array))    #square root, every element of the array is raised to the power of 0.5
                         #Output: [1.         1.41421356 1.73205081]

arr = np.array([1.2, 2.5, 3.7])
print("\nThis is the second array:", arr)

print("Rounded array:", np.round(arr))     #round, every element of the array is rounded to the nearest integer
                         #Output: [1. 2. 4.]

print("Floor of the array:",  np.floor(arr))     #floor, every element of the array is rounded down to the nearest integer
                         #Output: [1. 2. 3.]

print("Ceil of the array:", np.ceil(arr))      #ceil, every element of the array is rounded up to the nearest integer
                         #Output: [2. 3. 4.]

print("Value of pi:", np.pi)             #prints the value of pi
                         #Output: 3.141592653589793

#Example
radii = np.array([1, 2, 3])
print("\nThis is the radii array:", radii)

print("The area of the circles with the given radii is:", np.pi * radii ** 2)
#area of circle = pi * r^2
#Output: [ 3.14159265 12.56637061 28.27433388]