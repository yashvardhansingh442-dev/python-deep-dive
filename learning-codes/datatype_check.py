# datatype_check.py
values = [42, 3.14, "python", True, None, [1, 2, 3], (1, 2)]

for v in values:
    print(f"{str(v):15} -> {type(v).__name__}")
