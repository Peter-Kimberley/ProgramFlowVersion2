name = input("Please enter your name: ")
age = int(input("How old are yoy, {0}? ". format (name)))
print(age)

if age >= 18:
    print("You are old enough to vote")
    print("Please put an X in the box")
else:
    print("Please come back in {0} years".format(18 - age)) 

if age <= 18:
    print("Please come back in {0} years".format(18 - age)) 
else:
    print("You are old enough to vote")
    print("Please put an X in the box")
# There are more conditions added to the code #     