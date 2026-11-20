#logical operators = evaluate multiple conditions (or, and not)
#or = atleast one of the condition is true
#and = both conidtion must be true
#not = inverr the condition(if true,then output will be false)

temp = int(input("enter the temprature of today and ill check if its safe to go outside : "))

is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print ("the outdoor event is cancelled")
else:
    print("nanana")

