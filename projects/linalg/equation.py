import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 400)
y = (1 - x) / 2

plt.figure(figsize=(8,6))
plt.plot(x, y, linewidth=2)

# x-intercept (1,0)
plt.scatter(1, 0)
plt.text(1, 0, "(1,0)")

# y-intercept (0,0.5)
plt.scatter(0, 0.5)
plt.text(0, 0.5, "(0,0.5)")

plt.axhline(0)
plt.axvline(0)

plt.grid(True)
plt.title("x + 2y = 1")
plt.xlabel("x")
plt.ylabel("y")

plt.show()