import numpy as np

#vectorized math functions

array = np.array([1, 2, 3])
print("This is the original array: ", array)

print (np.sqrt(array)) #array square root every element of the array is raised to the power of 0.5

arr = np.array([1.2, 2.5, 3.7])
print("\n This is the second array: ", arr)
print (np.round(arr)) #array round every element of the array is rounded to the nearest integer)) 

print (np.floor(arr)) #array floor every element of the array is rounded down to the nearest integer

print (np.ceil(arr)) #array ceil every element of the array is rounded up to the nearest integer

print(np.pi) #prints the value of pi

#Example
radii = np.array([1, 2, 3])
print("\n This is the radii array: ", radii)
print("The area of the circles with the given radii is: ", np.pi * radii ** 2) #area of circle = pi * r^2