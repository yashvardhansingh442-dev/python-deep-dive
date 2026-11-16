import time

import numpy as np


def det_recursive(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    return sum(
        (-1) ** j
        * matrix[0][j]
        * det_recursive([row[:j] + row[j + 1 :] for row in matrix[1:]])
        for j in range(n)
    )


for n in [4, 6, 8, 9]:
    A = np.random.rand(n, n)
    t0 = time.time()
    det_recursive(A.tolist())
    t_det = time.time() - t0
    t0 = time.time()
    np.linalg.solve(A, np.ones(n))
    t_sol = time.time() - t0
    print(n, round(t_det, 5), round(t_sol, 6))
