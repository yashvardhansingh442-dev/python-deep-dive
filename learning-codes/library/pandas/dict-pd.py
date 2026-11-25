import pandas  as pd

calories = {"Day 1" : 1750 , "Day 2" : 2500, "Day 3" : 2100}

series = pd.Series(calories)
print(series)