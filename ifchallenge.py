name = input("What is you name?: ")
age = int(input("How old are you?: "))

if age <= 30 and age >= 18:
    print("Welcome {} to the holiday".format(name))
else:
    print("I am sorry {} but you do not meet the age restriction" 
          "for this holiday".format(name) )


# # Added a line of code asking for the name and added this
#  to bot string outputs as a .fornmat for strings