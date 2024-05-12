# This is anotehr example of true false values 'Tuthy values'
if 0 :
    print("True")
else:
    print("False")
name = input("Please enter your name: ")
# if name: This is a check for truth but is not relly easy to underatnd,
#this can be re-written to make more sense as written below
if name != "": 
    print("Hello {} ".format(name))
else:
    print("Are you the man with no name?")


