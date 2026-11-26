
# Format specifiers = {value:flags}
# Format a value using different flags

# .(number)f = Round to specified decimal places
# :(number)  = Allocate a specific number of spaces
# :0(number) = Allocate spaces and fill them with zeros
# :<         = Left align
# :>         = Right align
# :^         = Center align
# :+         = Show + sign for positive numbers
# :=         = Place sign at the leftmost position
# :          = Add a space before positive numbers
# :,         = Add comma separators

# Creating variables
price1 = 3.14159
price2 = -987.65
price3 = 12.34
price4 = 134.5495

# Printing without formatting
print(f"Price 1 is {price1}")
print(f"Price 2 is {price2}")
print(f"Price 3 is {price3}")

print("BREAK")

# Decimal formatting
print(f"Price 1 is {price1:.2f}")  # Round to 2 decimal places
print(f"Price 4 is {price4:.2f}")  # Round to 2 decimal places

# Space formatting
print(f"Price 2 is {price2:10}")  # Allocate 10 spaces
print(f"Price 3 is {price3:10}")  # Right align in 10 spaces

# Zero padding
print(f"Price 3 is {price3:010}")  # Fill empty spaces with zeros

# Alignment
print(f"Price 4 is {price4:<10}")  # Left align
print(f"Price 4 is {price4:>10}")  # Right align
print(f"Price 4 is {price4:^10}")  # Center align

# Sign formatting
print(f"Price 3 is {price3:+}")    # Show positive sign
print(f"Price 2 is {price2:+}")    # Show negative sign

# Comma separator
salary = 1500000
print(f"Salary is {salary:,}")    # Add commas

# More examples
print(f"{price1:.3f}")             # 3 decimal places
print(f"{price2:,.2f}")            # Commas and 2 decimals
print(f"{price3:+010.2f}")         # Sign, zero padding and 2 decimals
