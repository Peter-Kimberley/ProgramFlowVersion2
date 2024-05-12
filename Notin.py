activity = input("What would you like to do today? ")

if "cinema" not in activity.casefold(): # capitalise could be used here if the condition "cinema" started with a capital letter  
    print("But I want to go to the Cinema")

# checking the Boolean expresion using a "not in" condition, also using the dot notation of .casefold to ignore case sensititvity.
# String methods can be found at https://docs.python.org/3/library/stdtypes.html#string-methods