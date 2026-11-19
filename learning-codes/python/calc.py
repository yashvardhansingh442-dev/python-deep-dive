
# Python Calculator

operator = input("Enter the operator (+ - * /): ")

if operator == "":
    print("STFU")

elif operator not in ["+", "-", "*", "/"]:
    print("Bro fr!")

else:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        print(num1 + num2)

    elif operator == "-":
        print(num1 - num2)

    elif operator == "*":
        print(num1 * num2)

    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            print(num1 / num2)
