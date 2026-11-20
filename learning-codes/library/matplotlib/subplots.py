import matplotlib.pyplot as plt  # Imports Matplotlib to create graphs
import numpy as np  # Imports NumPy to create arrays

# Figure = The entire canvas containing all plots
# Axes = Individual plotting areas (subplots)

x = np.array([1, 2, 3, 4, 5])  # Creates an array of X values

figures, axes = plt.subplots(2, 2)  # Creates a figure with 2 rows and 2 columns (4 subplots)

axes[0,0].plot(x, x*2, color="red")  # Plots x multiplied by 2 in the first subplot
axes[0,0].set_title("x*2")  # Sets the title of the first subplot

axes[0,1].plot(x, x**2, color="blue")  # Plots x squared in the second subplot
axes[0,1].set_title("x**2")  # Sets the title of the second subplot

axes[1,0].plot(x, x**3, color="green")  # Plots x cubed in the third subplot
axes[1,0].set_title("x**3")  # Sets the title of the third subplot

axes[1,1].plot(x, x**4, color="orange")  # Plots x to the power of 4 in the fourth subplot
axes[1,1].set_title("x**4")  # Sets the title of the fourth subplot

plt.tight_layout()  # Automatically adjusts spacing between subplots
plt.show()  # Displays all four subplots