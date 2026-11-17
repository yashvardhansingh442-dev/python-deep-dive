import pandas as pd

data = [100, 200, 410 ,400, 450, 150, 625, 215 ]

series = pd.Series(data, index = ["a", "b", "c", "d", "e", "f", "g", "h"])

print(series[series >= 350])