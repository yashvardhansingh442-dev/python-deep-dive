import matplotlib.pyplot as plt

# grid = helps make plots easier to read by adding reference lines.

x = [1, 2, 3, 4, 5]
y = [1, 3, 5, 7, 9]

#plt.grid(axis="x") # displays grid lines only along the x-axis
#plt.grid(axis ="y") # displays grid lines only along the y-axis
plt.grid() # we can also changes the axis, linewidth, color, linestyle,etc.

plt.plot(x, y)
plt.show()
