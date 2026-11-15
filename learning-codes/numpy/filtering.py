import numpy as np

#filtering is used to extract elements from an array based on a condition.
ages = np.array([[11, 21, 37, 58, 45, 99],
                   [15, 36, 9,  12, 18, 25]])
teenagers = ages[ages > 21]
print("The Original array: ", ages)
print("The filtered array: ", teenagers)