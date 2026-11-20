import matplotlib.pyplot as plt  # Imports Matplotlib to create graphs
import numpy as np  # Imports NumPy to create arrays

# Scatter graph = Shows the relationship between two variables.
# Helps identify positive, negative, or no correlation.
# Example: Study hours vs test scores.

x1 = np.array([0,1,2,3,4,5,6,7,8,9])  # Stores Class A study hours
y1 = np.array([2,4,6,8,10,12,14,16,18,20])  # Stores Class A grades

x2 = np.array([10,11,1,6,4,5,7,8,10,4])  # Stores Class B study hours
y2 = np.array([5,5,1,10,20,4,6,7,8,5])  # Stores Class B grades

plt.scatter(x1, y1, color="red",  # Creates scatter plot for Class A
            alpha=0.6,  # Sets dot transparency
            s=100,  # Sets dot size
            label="CLASS A")  # Adds a name for the legend

plt.scatter(x2, y2, color="skyblue",  # Creates scatter plot for Class B
            alpha=0.8,  # Sets dot transparency
            s=100,  # Sets dot size
            label="CLASS B")  # Adds a name for the legend

plt.xlabel("STUDIED HOURS")  # Labels the X-axis
plt.ylabel("GRADES")  # Labels the Y-axis
plt.title("CLASS PERFORMANCE", family="Impact")  # Adds title with Impact font

plt.legend()  # Displays labels for both classes
plt.show()  # Displays the scatter plot