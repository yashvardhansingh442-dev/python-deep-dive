import matplotlib.pyplot as plt  # Imports Matplotlib to create the pie chart
import numpy as np  # Imports NumPy to create arrays

# Pie chart = A circular chart divided into slices to show percentages.
# Good for visualizing distribution among categories.

categories = np.array(["Freshman", "Sophomores", "Juniors", "Seniors"])  # Stores category names
values = np.array([100, 200, 75, 250])  # Stores values for each category
colors = ["red", "blue", "green", "orange"]  # Sets a different color for each slice

plt.pie(values, labels=categories,  # Creates pie chart and adds category labels
        autopct="%1.1f%%", colors=colors,  # Displays percentages and sets slice colors
        explode=[0, 0, 0, 0.1],  # Slightly separates the Seniors slice
        shadow=True, startangle=90)  # Adds shadow and rotates the chart

plt.show()  # Displays the pie chart