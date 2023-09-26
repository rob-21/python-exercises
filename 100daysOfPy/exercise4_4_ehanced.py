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

pick = [rock, paper, scissors]

userChoice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print("\nYou chose:")

if userChoice < 0 or userChoice >= 3:
    raise Exception("Please chose a valid number.")

else:
    computerChoice = random.randint(0, 2)
    print(pick[userChoice], "\n"
          "Computer chose:\n", pick[computerChoice])

    if userChoice == computerChoice:
        print("\nIt's a draw")
    elif userChoice == 0 and computerChoice == 1 or userChoice == 1 and computerChoice == 2 or userChoice == 2 and computerChoice == 0:
        print("\nYou lose")
    elif userChoice == 0 and computerChoice == 2 or userChoice == 1 and computerChoice == 0 or userChoice == 2 and computerChoice == 1:
        print("\nYou win")
