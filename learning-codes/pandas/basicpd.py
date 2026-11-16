import pandas as pd

print(pd.__version__)

#In Python, a Series most commonly refers to a Pandas Series, a one-dimensional labeled array 
#capable of holding any data type (integers, strings, floats, or Python objects). 
#It works like a single column in a spreadsheet or a database table.

data = [100, True, 300]

series = pd.Series(data)
print(series)

#dtype is object idk why loook around jk dtype is object because the Series contains mixed data types (integers and boolean).
# Pandas uses the object dtype to store values of different Python data types
# in a single Series without forcing them into one common numeric dtype.