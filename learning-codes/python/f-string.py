# f-string is a way to format strings in Python.
# It allows you to embed expressions inside string literals, using curly braces {}.
# This makes it easier to create dynamic strings that include variable values or expressions.

# strings
first_name = "John"
last_name = "Doe"
print(f"My name is {first_name} {last_name}.")  # this will print "My name is John Doe."

var = "bro"
print(f"hello {var}!")


# integers
x = 10
print(f"the age is {x} years old")


# float
price = 100.99
gpa = 3.7
print(f"the total is {price} cents")
print(f"Your gpa is {gpa}")


# boolean
is_student = True
print(f"Are you a student {is_student}")
