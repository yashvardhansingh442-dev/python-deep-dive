import pandas as pd

#data = [100, 200, 410 ,400, 450, 150, 625, 215 ]

#series = pd.Series(data, index = ["a", "b", "c", "d", "e", "f", "g", "h"])

#print(series[series >= 350])

#example 1 
calories = {"day 1 " : 1750, "day 2" : 2550, "day 3" : 1500}
series = pd.Series(calories)

#series.loc["day 3"] += 500
#print(series)

#example 2

import pandas as pd

data = ["bulbasaur", "Ivysaur", "Venasaur",
        "Charmander", "charmeleon", "charlizard"]

series = pd.Series(data, index=[1, 2, 3, 4, 5, 6], dtype=object)

print(series)