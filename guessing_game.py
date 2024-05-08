answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("please guess higher")
elif guess > answer:
    print("Please guess lower")  
else:
    print("You got it first time")
      