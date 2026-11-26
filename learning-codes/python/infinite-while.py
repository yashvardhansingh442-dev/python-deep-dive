# While loops = Execute code WHILE a condition remains TRUE

name = input("Enter your name: ")

# Infinite loop if the name is empty
while name == "":
    print("You did not enter your name")

# Print the name
print(f"Hello {name}")