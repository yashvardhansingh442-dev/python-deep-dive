import pandas as pd

print(pd.__version__)

#In Python, a Series most commonly refers to a Pandas Series, a one-dimensional labeled array
#capable of holding any data type (integers, strings, floats, or Python objects).
#It works like a single column in a spreadsheet or a database table.

data = [100, True, 300]

series = pd.Series(data, index = ["a", "b", "c"]) #index in series function is used on lhs
#                                                  side of the series.

print(series) #can print the series in a tabular format happy!
series.loc["c"] = 200 # we can also change the value of the data later on

print(series.loc["c"]) #.loc[] is a label-based indexing property used to access,
#                       filter, and modify groups of rows and columns in a DataFrame or Series.

#dtype is object idk why loook around jk dtype is object because the Series contains
#mixed data types (integers and boolean).
# Pandas uses the object dtype to store values of different Python data types
# in a single Series without forcing them into one common numeric dtype.

#iloc
#.iloc[], which relies on zero-based integer positions,
#.loc[] looks up data using explicit row index labels and column names.
