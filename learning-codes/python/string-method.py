name = input("ENTER YOUR HEAVENLY NAME : ")
result = len(name) #len is a fucntion that find the total length of the string. 
observation = name.find("o") #.find is a function that find the index of the " " wtv feed bw this.
hell = name.rfind("o") #returns the highest index (the rightmost or last occurrence) of a substring within a string.
name=name.capitalize()#returns a new string with the first character converted to uppercase and all other characters converted to lowercase
upperr = name.upper()#converts all lowercase letters in a string to uppercase and returns a new string
lowerr = upperr.lower()#converts all uppercase letter in a sting to lowercase and returns a new string
specific = name.isdigit()#function that checks whether all characters in a string are digits. 
#                        It returns True if every character is a digit and the string is not empty, and False otherwise

print(result)
print(observation)
print(hell)
print(name)
print(upperr)
print(lowerr)
print(specific)