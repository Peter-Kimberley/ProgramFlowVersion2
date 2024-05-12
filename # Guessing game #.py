answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

if guess == answer:
    print("You got it first time")
else:
    if guess < answer:
     print("Please guess higher")
    else:
       print("Please guess lower")
    guess = int((input))
    if guess == answer:
       print("Well done you guessed it")
    else:
       print("Sorry you didnt guees correctly")
       
    
# Guessing game is now simplified to allow to check if answer is correct first time.



# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")


