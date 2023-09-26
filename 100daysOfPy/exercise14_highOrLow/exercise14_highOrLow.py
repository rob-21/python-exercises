import random
import os
import game_data
import art


# 4 if choice is true, then print result
# 5 store the user's score
# 6 persist the latest object and make a new random comparison
# 7 if user loses, then print out their score

# 2 the game should pick a random comparison from game_data


def compare_variants(variantA, variantB):
    global winningVersion
    if variantA > variantB:
        winningVersion = "A"
        # print("CF Winnin version: ", winningVersion)
        return winningVersion
    elif variantB > variantA:
        winningVersion = "B"
        # print("CF Winnin version: ", winningVersion)
        return winningVersion


def game():
    game_on = True
    SCORE = 0
    while game_on:
        os.system('clear')
        # 1 when launching the game, the artwork should be printed
        print(art.logo)
        if SCORE == 0:
            choiceA = random.choice(game_data.data)
        else:
            print(f"You're right! Current score: {SCORE}.")
        choiceB = random.choice(game_data.data)
        while choiceB == choiceA:
            choiceB = random.choice(game_data.data)

        # 3 the game should ask the user to pick the option that has more followers
        print(
            f"Compare A: {choiceA['name']}, a {choiceA['description']}, from {choiceA['country']}")
        print(art.vs)
        print(
            f"Against B: {choiceB['name']}, a {choiceB['description']}, from {choiceB['country']}")

        answer = input("Who has more followers? Type 'A' or 'B': ").upper()
        compare_variants(
            choiceA['follower_count'], choiceB['follower_count'])
        # print("Winning version is: ", winningVersion)
        if answer == winningVersion:
            if winningVersion == "A":
                choiceA = choiceA
            else:
                choiceA = choiceB
            SCORE += 1
        else:
            print(f"Sorry, that's wrong. Final score: {SCORE}")
            game_on = False


game()
