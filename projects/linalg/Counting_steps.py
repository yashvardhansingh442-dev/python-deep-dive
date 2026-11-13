for n in [10, 100, 1000]:
    count = sum((n-k-1)*(n-k) for k in range(n))
    print(n, count, round(n**3/3, 1))