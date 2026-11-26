# For loops = Execute a block of code a fixed number of times.
# You can iterate over a range, string, sequence, etc.

# Print numbers from 1 to 10
for x in range(1, 11):
    print(x)


print("Now we will print the reversed order")

# Print numbers from 10 to 1
for y in reversed(range(1, 11)):
    print(y)


print("Now we will print this with a gap between the numbers")

# Step = 2 (skip every alternate number)
for z in range(1, 11, 2):
    print(z)


print("Now we will skip number 13")

# Continue = Skip the current iteration and move to the next one.
# Break = Stop the loop completely.
for a in range(1, 21):
    if a == 13:
        continue
        # break
    print(a)