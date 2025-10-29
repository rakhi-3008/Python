import random

num = random.randint(1,100)

guess = int(input("Guess the number "))

numofguess = 1

while(num != guess):

    if(guess > num ):
        print("lower number please")
    elif(guess < num):

        print("higher number please")

    numofguess+=1

    guess = int(input("Guess the number "))

print(f"congratulations, you guess correct number {num}")

print(f"you guess corect number in {numofguess} guesses")