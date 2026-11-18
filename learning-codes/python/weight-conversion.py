
# Weight Conversion Program

weight = float(input("Enter your weight: "))
unit = input("Convert to (KG or LBS): ").upper()

if unit == "KG":
    converted_weight = weight / 2.205
    print(f"Your weight is {converted_weight:.2f} kg")

elif unit == "LBS":
    converted_weight = weight * 2.205
    print(f"Your weight is {converted_weight:.2f} lbs")

else:
    print("Invalid unit! Please enter KG or LBS.")
