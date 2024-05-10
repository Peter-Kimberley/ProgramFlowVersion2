# Guessing game #
answer = 5

print("Please guess a number betweem 1 and 10: ")
guess = int(input())

if guess < answer:
    print("Please guess higher")
    guess = int(input())
    if guess  == answer:
        print("well done you guessed it")
    else:
        print("Sorry you have not guessed correctly")

elif guess > answer:
    print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("well done you guessed it")
    else:
        print("Sorry you have not guessed correctly")

else:
    print("You got it first time")

    