parrot = "Norwegian Blue"

letter = input("Enter a chartacter: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")
# Using the the condition "In" to check the Boolean value of code