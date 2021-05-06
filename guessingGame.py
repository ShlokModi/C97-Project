import random
print("Let's play a guessing game")
number= random.randint(1,9)
chance = 0
print("Guess any number between 1 to 9")

while chance<5:
    numberGuessed = int(input("Enter your Guess"))
    if (numberGuessed == number):
        print("Correct")
        print("You Win")
        chance=6
    elif (numberGuessed < number):
        print("Your guess is too low")
        print("Guess a number higher than this number")
    else:
        print("Your guess is too high")
        print("Guess a number lower than this number")
    chance= chance+1

if (chance==5 and numberGuessed!= number):
    print("You Lose")