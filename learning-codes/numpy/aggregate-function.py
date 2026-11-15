import numpy as np

#aggregate functions are used to perform operations on an entire array and return a single value.
array = np.array([[1, 2, 3, 4, 5], 
                  [6, 7, 8, 9, 10]])

print("The Original array: ", array)
print("The sum of all elements in the array: ", np.sum(array))     #sum of all elements in the array
print("The mean of all elements in the array: ", np.mean(array))     #mean of all elements in the array
#mean is the average of all elements in the array. It is calculated by adding all the elements and dividing by the number of elements.
print("The standard deviation of all elements in the array: ", np.std(array))     #standard deviation of all elements in the array
#standard deviation is a measure of how spread out the numbers are in the array.
#It is calculated as the square root of the variance.
print("The variance of all elements in the array: ", np.var(array))     #variance of all elements in the array
#variance is the average of the squared differences from the mean. 
#A low standard deviation indicates that the values tend to be close to the mean,
#while a high standard deviation indicates that the values are spread out over a wider range.
print("The minimum value in the array: ", np.min(array))     #minimum value in the array
print("The maximum value in the array: ", np.max(array))     #maximum value in the array
print("The index of the minimum value in the array: ", np.argmin(array))     #index of the minimum value in the array
print("The index of the maximum value in the array: ", np.argmax(array))     #index of the maximum value in the array

#example
print("The sum of all elements in the array along axis 0: ", np.sum(array, axis=0))     #sum of all elements in the columns of the array
print("The sum of all elements in the array along axis 1: ", np.sum(array, axis=1))     #sum of all elements in the rows of the array

