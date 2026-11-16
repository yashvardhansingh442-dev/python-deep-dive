# Multiplications needed by elimination on an n x n system: the sum below
# grows like n**3 / 3, so doubling n makes the work about 8 times larger.
for n in [10, 100, 1000]:
    count = sum((n - k - 1) * (n - k) for k in range(n))
    print(n, count, round(n**3 / 3, 1))
