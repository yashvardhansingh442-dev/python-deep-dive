import numpy as np

#filtering is used to extract elements from an array based on a condition.
ages = np.array([[11, 21, 37, 58, 45, 99],
                   [15, 36, 9, 12, 18, 25]])
teenagers = ages[ages < 21]
adults = ages[(ages >= 21) & (ages <= 45)]
print("The Original array: ", ages)
print("The teenagers are with ages are : ", teenagers)
print("The adults are with ages are : ", adults)
print("The seniors citizens are with ages are : ", ages[ages > 45])
even_ages = ages[ages % 2 == 0]
print("The even ages are : ", even_ages)
odd_ages = ages[ages % 2 != 0]
print("The odd ages are : ", odd_ages)

sigma = np.where(ages == 18, ages, 0) #this is what we called as filtering, where we filter it out like a fly in a milk, hehee 
print(sigma)