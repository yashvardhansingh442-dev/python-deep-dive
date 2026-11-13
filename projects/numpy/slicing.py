import numpy as np

#array slicing
#array[start:end:step]

array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

print(array)

#rows
print(array[0:])      #you can also use this to get the whole array
print(array[0:2])     #get the first two rows
print(array[::2])     #get every second row
print(array[::3])     #get every third row

print("now we will get the columns")

#columns
print(array[:, 0])    #get the first column
print(array[:, 1])    #get the second column
print(array[:, -1])   #get the last column, this is the negative indexing

#negative indexing can be used to get the last elements of the array

print(array[:, 0:3])  #get the first three columns
print(array[:, ::2])  #get every second column

print("below is the slicing of both rows and columns")

print(array[0:2, 0:2])
#get the first two rows and first two columns
#this happens because we are slicing the rows and columns at the same time
#as we use the comma to separate the two slices

print("This is the slicing of another array")

arr = np.array([10, 20, 30, 40, 50, 60])
print(arr)

#slice from index 1 to 4 (exclusive)
print(arr[1:4])       #Output: [20 30 40]

#slice from index 3 to the end
print(arr[3:])        #Output: [40 50 60]

#get every second element (stepping)
print(arr[::2])       #Output: [10 30 50]

#reverse the array using a negative step
print(arr[::-1])      #Output: [60 50 40 30 20 10]