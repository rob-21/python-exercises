## --> Rock, paper, scissors <-- ##

# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

userChoice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print("\nYou chose:")

if userChoice < 0 or userChoice >= 3:
    raise Exception("Please chose a valid number.")

else:
    if userChoice == 0:
        print(rock)
    elif userChoice == 1:
        print(paper)
    elif userChoice == 2:
        print(scissors)

    computerChoice = random.randint(0, 2)
    print("\nComputer chose:")
    if computerChoice == 0:
        print(rock)
    elif computerChoice == 1:
        print(paper)
    elif computerChoice == 2:
        print(scissors)

    if userChoice == computerChoice:
        print("\nIt's a draw")
    elif userChoice == 0 and computerChoice == 1 or userChoice == 1 and computerChoice == 2 or userChoice == 2 and computerChoice == 0:
        print("\nYou lose")
    elif userChoice == 0 and computerChoice == 2 or userChoice == 1 and computerChoice == 0 or userChoice == 2 and computerChoice == 1:
        print("\nYou win")


# How could this code be better?
# first of all, putting rock, paper and scissors inside a list and using that list's index when applying codintions
# see exercise4_4_enhanced.py for a better version
