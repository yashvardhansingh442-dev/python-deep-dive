import matplotlib.pyplot as plt
import numpy as np

#histograms = visual representation of the distribution of quantitative data. they gorups values into bins(intervals) and counts how many falls into each range.

scores = np.random.normal(loc=80, scale =10 ,size = 100)
scores = np.clip(scores, 0, 100)

plt.hist(scores,bins=15, color = "lightblue", edgecolor = "black")

plt.title("SCORES", family = "impact")

plt.xlabel("SUBJECT")
plt.ylabel("no. of students")

plt.show()

