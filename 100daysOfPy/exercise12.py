## --> Number guessing game <-- ##

import random
import os
import guessArt


def compareNum(num1, num2):
    if num1 < num2:
        print("Too low.\nGuess again.")
    elif num1 > num2:
        print("Too high.\nGuess again.")


def game():
    os.system("clear")
    x = range(1, 101)
    numberPick = random.choice(x)
    game_on = True
    while game_on:
        print(guessArt.logo)
        noOfTries = 0
        print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100. ")
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard':  ")
        print(f"Pssst, the numbeer is {numberPick}")
        if difficulty == 'easy':
            noOfTries = 10
        else:
            noOfTries = 5
        print(f"You have {noOfTries} attempts remaining to guess the number")

        for i in range(0, noOfTries-1):
            numberInput = int(input("Make a guess: "))
            if numberInput == numberPick and noOfTries != 0:
                print(f"You got it! The number was {numberInput}")
                break
            else:
                compareNum(numberInput, numberPick)
                noOfTries -= 1
                print(f"You have {noOfTries} attempts left.")
                if noOfTries == 0:
                    print("You've run out of guesses, you lose.")
        if input("Play again?: ") == "yes":
            game_on = False
            game()
        else:
            quit()


game()
