import matplotlib
import matplotlib.pyplot as plt

# pyplot is a module which we import from matplotlib as plt

print(matplotlib.__version__) # prints the installed matplotlib version

x = [2023, 2024, 1998, 1990, 1920]
y1 = [15, 20, 25, 30, 35]
y2 = [10, 18, 26, 28, 45]
y3 = [12, 20, 28, 24, 50]

# plot() is used to draw 2d line graphs using x and y values

line_style = {
    "marker": ".", # adds a dot at each data point
    "markersize": 10, # changes the size of the marker (ms)
    "markerfacecolor": "cyan", # changes the inside color of marker (mfc)
    "markeredgecolor": "cyan", # changes the border color of marker (mec)
    "linestyle": "solid", # changes the style of line (solid, dashed, dotted, dashdot)
    "linewidth": 2, # changes the thickness of line (lw)
}

# we can use a dictionary to store multiple styling properties
# ** is used to unpack the dictionary inside plt.plot()

plt.plot(x, y1, **line_style, color="red", label="LINE 1") # plots first line in red
plt.plot(x, y2, **line_style, color="green", label="LINE 2") # plots second line in green
plt.plot(x, y3, **line_style, color="blue", label="LINE 3") # plots third line in blue

plt.xlabel("Year") # adds label to x-axis
plt.ylabel("Values") # adds label to y-axis

plt.title("Multiple Line Graphs", fontsize=15, family="impact") # changes title, fontsize and font family

plt.legend() # displays labels of all lines

plt.show() # displays the graph


# color is used to change the line color
# alpha is used to control transparency (0 = invisible, 1 = fully visible)
# marker can be ., o, *, +, x, s, D etc.
# linestyle can be solid, dashed, dotted or dashdot
# linewidth changes the thickness of the line

# matplotlib automatically assigns different colors to each plot
# when we don't specify any color manually
# it uses a default color cycle for every new plt.plot()

# plt.xticks() is used to get or change the x-axis tick locations and labels
# example: plt.xticks([1990, 1998, 2023, 2024])

# tick_params() is used to customize the appearance of axis ticks and labels
# example: plt.tick_params(axis="x", labelsize=12)