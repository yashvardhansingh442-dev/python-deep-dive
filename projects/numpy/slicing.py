import numpy as np

array = np.array([[1, 2, 3, 4], 
                  [5, 6, 7, 8], 
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

#array slicing
#array[start:end:step]

print(array[0:]) #you can also use this to get the whole array

print(array[0:2]) #get the first two rows

print(array[0:4:2]) #get every second row

print(array[0:4:3]) #get every third row

print(array[::2]) #get every second row

print("now we will get the columns")

print(array[:,0]) #get the first column

print(array[:,1]) #get the second column
