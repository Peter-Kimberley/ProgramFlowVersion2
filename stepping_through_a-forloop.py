number = "9,223;372:036 854,775;807"
seperators = ""

for char in number:
    if not char.isnumeric():
        seperators = seperators + char
# This is a check to see if the value of "isnumeric is false, 
# when this checks out as false, then the char is added to seperators"

print(seperators)

values = "".join(char if char not in seperators else " " \
                 for char in number).split()
print([int(val) for val in values])
