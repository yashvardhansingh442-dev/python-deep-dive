# Number of rows in the pyramid
rows = 5

for i in range(rows):
    # Calculate spaces and asterisks for the current row
    spaces = " " * (rows - i - 1)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)
