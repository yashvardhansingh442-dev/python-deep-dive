# While loops = Execute code WHILE a condition remains TRUE

name = input("Enter your name: ")

# Check if the user entered an empty name
while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")

# Print the name
print(f"Hello {name}")


# while loop = execute some code WHILE some condition remains true

age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))

print(f"You are {age} years old")

num = int(input("Enter a # between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))

print(f"Your number is {num}")

