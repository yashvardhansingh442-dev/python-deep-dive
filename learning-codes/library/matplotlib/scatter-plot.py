import matplotlib.pyplot as plt  # Imports Matplotlib to create graphs
import numpy as np  # Imports NumPy to create arrays

# Scatter graph = Shows the relationship between two variables.
# Helps identify positive, negative, or no correlation.
# Example: Study hours vs test scores.

x1 = np.array([0,1,2,3,4,5,6,7,8,9])  # Stores the first set of study hours
y1 = np.array([2,4,6,8,10,12,14,16,18,20])  # Stores the corresponding grades

x2 = np.array([10,11,1,6,4,5,7,8,10,4])  # Stores the second set of study hours
y2 = np.array([5,5,1,10,20,4,6,7,8,5])  # Stores the corresponding grades

plt.scatter(x1, y1, color="red",  # Creates the first scatter plot with red dots
            alpha=0.6,  # Makes the dots slightly transparent
            s=100)  # Sets the size of the dots

plt.scatter(x2, y2, color="skyblue",  # Creates the second scatter plot with sky-blue dots
            alpha=0.8,  # Controls the transparency of the dots
            s=100)  # Sets the size of the dots

plt.xlabel("STUDIED HOURS")  # Adds a label to the X-axis
plt.ylabel("GRADES")  # Adds a label to the Y-axis
plt.title("CLASS PERFORMANCE", family = "impact")  # Adds a title to the graph

plt.show()  # Displays the scatter plot