import random
highest = 10
answer = random.randint(1, highest)
guess =(0)
print(answer) # TODO: delete code after testing.

print("Please guess number \
      between 1 and {}, or press 0 to exit: ".format(highest))


while guess != answer:

    
    guess = int(input())
    if guess== 0:
        print("Thanks for stopping by")
        break
    elif guess  == answer:
        print("Well done you guessed corretly")
        break
    else:
        if guess < answer:
            print("Please guess higher, or press 0 to exit: ")
        else:
            print("Please guess lower, or press 0 to exit: ")
        # guess = int(input())
        # if guess == answer:
        #     print("Well done you guessed corretly")
         
        # else:
        #     print("Sorry, you have not guess correctly")









