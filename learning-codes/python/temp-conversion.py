
# Temperature Conversion Program

temp = float(input("Enter the temperature: "))
unit = input("Convert to (C/F): ").upper()

if unit == "C":
    converted_temp = (temp - 32) * 5 / 9
    print(f"Temperature: {converted_temp:.2f}°C")

elif unit == "F":
    converted_temp = (temp * 9 / 5) + 32
    print(f"Temperature: {converted_temp:.2f}°F")

else:
    print("Invalid unit! Please enter C or F.")
