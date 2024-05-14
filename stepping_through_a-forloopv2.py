number = input("Please enter a series of numbers, using any characters to seperator that is not a number: ")
seperators = ""

for char in number:
    if not char.isnumeric():
        seperators = seperators + char
# This is a check to see if the value of "isnumeric is false, when this checks out as false, then the char is added to seperators"
#print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print(sum([int(val) for val in values]))
# we have used the built in function sum() to add all the numbers in our sequence and output the total