import matplotlib
import matplotlib.pyplot as plt
import numpy as np #we can also us numpy library for some more functionality

# pyplot is a module which we import from matplotlib as plt

print(matplotlib.__version__)
# __version__ prints the installed Matplotlib version

x = [2023, 2024, 1998, 1990, 1920]
y = [15, 20, 25, 30, 35]

plt.plot(x,y, marker = ".") #unction draws 2D lines and markers using x-axis and y-axis data arrays
plt.show() #function renders and displays all open figures on your screen