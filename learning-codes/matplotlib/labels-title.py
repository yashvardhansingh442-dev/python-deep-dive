import matplotlib
import matplotlib.pyplot as plt
import numpy as np #we can also use numpy library for some more functionality

#pyplot is a module which we will import in matplotlib as plt

print(matplotlib.__version__)
# __version__ prints the installed matplotlib version

x = [2023, 2024, 1998, 1990, 1920]
y1 = [15, 20, 25, 30, 35]
y2 = [10, 18, 26, 28, 45]
y3 = [12, 20, 28, 24, 50]

# function draws 2D lines and markers using x-axis and y-axis data arrays

line_style = dict(
    marker=".",
    markersize=10,
    markerfacecolor="cyan",
    markeredgecolor="cyan",
    linestyle="solid",
    linewidth=2,
)

# marker means just marker which can be used to point out data points in the graph
# markersize can be used to adjust the size of the marker, we can also use ms instead of markersize (short abbreviation)
# markerfacecolor is used to adjust the fill color of the marker, we can also use mfc instead of markerfacecolor (short abbreviation)
# markeredgecolor is used to adjust the color of the marker edge, we can also use mec instead of markeredgecolor (short abbreviation)
# linestyle dashed is used to change the line style used to plot the graph
# linewidth is used to change the line width used to plot the graph
# color is used to change the line color used to plot the graph

plt.plot(x, y1, **line_style,color = "RED")
plt.plot(x, y2, **line_style, color = "green")
plt.plot(x, y3, **line_style, color = "blue")

plt.xlabel("Year")
plt.ylabel("Values")
plt.title("Multiple Line Graphs", fontsize = 15, family = "impact") #we can change the fontsize using fontsize, using font as family, 
#                                                                   fontweight as bold, and also the color

plt.legend()

plt.show()
# function renders and displays all open figures on your screen

# In Matplotlib, creating a line_style = dict(...) lets you group multiple line properties (color, width, dash pattern, markers, transparency)
# into a single reusable dictionary and apply it cleanly using Python's dictionary unpacking operator (**).
# Matplotlib automatically assigns different colors to each plot
# using its default color cycle when no color is explicitly specified.

# Each new plt.plot() call takes the next color from the color cycle.

# If we specify color manually or pass a dictionary containing color,
# Matplotlib uses our specified color instead of the default color cycle.


#In Matplotlib, plt.xticks() is a function used to get or set the current tick locations and labels on the x-axis. 
#If you are working with the object-oriented interface (fig, ax), the equivalent method is ax.set_xticks()

#In Matplotlib, tick_params() is used to customize the appearance of axis ticks, tick labels, and gridlines at once. 
#You can call it on an Axes object (ax.tick_params()) or via the pyplot interface (plt.tick_params()