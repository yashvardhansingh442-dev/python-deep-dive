
# Python Compound Interest Calculator

principle = 0
rate = 0
time = 0

# Get the principal amount (must be greater than zero)
while principle <= 0:
    principle = float(input("Enter the principal amount: "))

    if principle <= 0:
        print("Principal can't be less than or equal to zero")

# Get the interest rate (must be greater than zero)
while rate <= 0:
    rate = float(input("Enter the interest rate percentage: "))

    if rate <= 0:
        print("Rate can't be less than or equal to zero")

# Get the time period (must be greater than zero)
while time <= 0:
    time = float(input("Enter the time in years: "))

    if time <= 0:
        print("Time can't be less than or equal to zero")

# Display the entered values
print(f"Principal: ${principle}")
print(f"Interest Rate: {rate}%")
print(f"Time: {time} years")

# Calculate compound interest
total = principle * pow((1 + rate / 100), time)

# Display the final balance
print(f"Balance after {time} years is: ${total:.2f}")
