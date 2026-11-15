def classify(a, b, c, d, e, f):
    m = d / a
    e2, f2 = e - m*b, f - m*c
    if e2 != 0:
        return f"unique: y={f2/e2}"
    return "0 = 0: infinitely many" if f2 == 0 else f"0 = {f2}: no solution"

print(classify(1,2,3, 4,5,6))
print(classify(1,2,3, 4,8,6))
print(classify(1,2,3, 4,8,12))