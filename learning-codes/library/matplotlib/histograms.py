import matplotlib.pyplot as plt  # Imports Matplotlib to create graphs
import numpy as np  # Imports NumPy to generate numerical data

# Histogram = Shows the distribution of numerical data.
# Groups values into bins (intervals) and counts how many fall into each range.

scores = np.random.normal(loc=80, scale=10, size=100)  # Generates 100 random scores with mean 80 and standard deviation 10
scores = np.clip(scores, 0, 100)  # Keeps all scores between 0 and 100

plt.hist(scores, bins=15, color="lightblue", edgecolor="black")  # Creates a histogram with 15 bins and black borders

plt.title("SCORES", family="Impact")  # Adds a title with Impact font

plt.xlabel("SUBJECT")  # Labels the X-axis
plt.ylabel("NO. OF STUDENTS")  # Labels the Y-axis

plt.show()  # Displays the histogram