import pandas as pd

df = pd.read_csv("data.csv")

# Filtering = Keeping the rows that match a condition
# tall_pokemon = df[df["Height"] >= 2]
heavy_pokemon = df[df["Weight"] > 100]

print(heavy_pokemon)
