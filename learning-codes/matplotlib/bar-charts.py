import matplotlib.pyplot as plt
import numpy as np

# bar chart = compare categories of data by representing each category with bar

categories = np.array(["Grain", "Fruits", "Veggies", "Chocolate", "Curd", "Momos", "Pancake"])
values = np.array([4, 3, 2, 1, 5, 1, 6])

plt.bar(categories,values)

plt.xlabel("GROCERY LIST")
plt.ylabel("QTY.")
plt.title("SHOPPING CART", family = "impact")
plt.show()