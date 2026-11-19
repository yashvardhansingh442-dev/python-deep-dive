import matplotlib
import matplotlib.pyplot as plt
import numpy as np #we can also us numpy library for some more functionality

# pyplot is a module which we import from matplotlib as plt

print(matplotlib.__version__)
# __version__ prints the installed Matplotlib version

x = [2023, 2024, 1998, 1990, 1920]
y1 = [15, 20, 25, 30, 35]
y2 = [10, 18, 26, 28, 45]

plt.plot(x,y1, marker = ".",markersize = 10, markerfacecolor = "cyan", 
         markeredgecolor = "cyan", linestyle = "dashed",linewidth = 2, 
         color = "red") #unction draws 2D lines and markers using x-axis and y-axis data arrays

#marker means just marker which can be used to poin out in the graph
#markersize can be used to adjust the size of the marker, we can also use ms instead of markersize short abbrevation
#markerfacecolor is used to ajust the color of the marker, we can also use mf instead of markerfacecolor short abbrevation
#markeredge color is used to adjust the color of the marker edge, we can also use mec instead of markeredgecolor short abbrevation
#linestyle dashed is used to change the line used to plot the graph 
#linewidth is used to chnage the line width used to plot the graph
#color is used to change the line color used to plot the graph

plt.plot(x,y2, marker = "*")
plt.show() #function renders and displays all open figures on your screen
#In Matplotlib, creating a line_style = dict(...) lets you group multiple line properties (color, width, dash pattern, markers, transparency) 
#into a single reusable dictionary and apply it cleanly using Python's dictionary unpacking operator