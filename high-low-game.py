# This is a binary chop
high = 1000
low = 1



tries = (1)
print("Please think of a number between {} and {} :".format(low, high))
input("Please press enter to start ")

while low!= high:
    guess = low + (high - low) // 2 # This is the formularfor the chop
    high_low = input("my guess is {}. Should I guess higher or lower"
                    "enter c if I guessed correctly "
                      "".format(guess)).casefold()
    if high_low == "h":
        # Then low becomes 1 greater than the guess
        low = guess + 1
        
        
    elif high_low == "l":
        # Then high becomes 1 less than the guess
        high = guess - 1 

        
        
    elif high_low == "c":
        # Then the program should finish
        print("I guessed it in {} tries".format(tries))
        break
   
    else:
        "please press h, l, or c"

    tries = tries + 1
