import numpy as np

#comparison operator
score = np.array([55, 24, 73, 14, 100, 68, 80, 60])
print("This is the score array: ", score)
print("Scores equal to 100: ", score == 100)
print("Passing scores greater than or equal to 60: ", score >= 60)
print("Scores less than 40: ", score < 40)