a, b, c = 1, 2, 3        # x + 2y = 3
d, e, f = 4, 5, 6        # 4x + 5y = 6

m  = d / a               # multiplier
e2 = e - m * b           # new y-coefficient in eq 2
f2 = f - m * c           # new right side in eq 2
y  = f2 / e2             # solve the last equation
x  = (c - b * y) / a     # back-substitution
print(m, e2, f2, y, x)