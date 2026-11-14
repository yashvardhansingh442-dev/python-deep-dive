import numpy as np

#scalar operations on an array

array = np.array([1, 2, 3])
print("The Original array: ", array)

print("Array after addition by 1: ", array + 1)     #addition, every element of the array is added by 1
                     #Output: [2 3 4]

print("Array after subtraction by 1: ", array - 1)     #subtraction, every element of the array is subtracted by 1
                                                       #Output: [0 1 2]

print("Array after multiplication by 2: ", array * 2)     #multiplication, every element of the array is multiplied by 2
                                                          #Output: [2 4 6]

print("Array after division by 2: ", array / 2)     #division, every element of the array is divided by 2
                                                   #Output: [0.5 1.  1.5]

print("Array after exponentiation by 2: ", array ** 2)    #exponentiation, every element of the array is raised to the power of 2
                                                         #Output: [1 4 9]