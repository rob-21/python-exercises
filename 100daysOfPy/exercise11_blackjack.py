## --> Blackjack <-- ##

# must keep track of 'score'
# Q, J, K -> These cards == 10
# A -> Can be 11, can be 1, depending on situation
# --> ( --> if score <= 10, A == 11, if score > 10, A = 1)
# 21 -> maximum score
# if cards = A + Q or A + J or A + K, it's a default win
# If cards total (player or dealer) > 21, the other wins
# The player with the score closest to 21 wins.
# if both players have the same score, it's a draw

# At the start of the game, you're dealt 2 cards, and the dealer gets 2 cards (you can see one of their cards)
# The player has the option to ask for another random card or stand
# ----> when does the dealer get another card? Perhaps python random has a random choice mechanism

import random
import artBlackjack
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def addCards(card_list):  # formula to calculate hand total
    """Adds all the cards in the list and returns the total amount"""
    total = 0
    for eachCard in card_list:
        total += eachCard
    return total


def drawCard(card, card_list):  # formula to draw one card
    """Picks a random card from the list and appends it to players cards"""
    card.append(random.choice(card_list))
    for i in card:
        if i == 11:
            card_list[0] = 1
        elif i == 1:
            card_list.pop(0)
    return card


def gameEnd(playerCards, computerCards, playerScore, computerScore, game_continue):
    """Calls the final status of the game and allows the player to start a new game"""
    while game_continue == True:
        print("\n   Your final hand: ", playerCards, f"final score: {playerScore}"
              "\n   Computer's final hand: ", computerCards, f"final score: {computerScore}\n")
        if playerScore > 21:
            print("You went over 21, so you lost the gane :(\n")
            game_continue = False
            game()
        else:
            if computerScore > playerScore:
                print("You lost! :(\n")
                game_continue = False
                game()
            elif playerScore == computerScore:
                print("It's a draw!\n")
                game_continue = False
                game()
            else:
                print("You won!\n")
                game_continue = False
                game()

# game


def game():
    game_continue = True
    while game_continue:
        if input("Do you want to play a game of Blackjack? Type 'y' for Yes or 'n' for No: ") == 'y':
            os.system("clear")
            print(artBlackjack.logo)
            game_continue = True
        else:
            quit()

        playerCards, computerCards = [], []
        # handout 2 cards cards each, player and dealer
        for i in range(0, 2):
            playerCards, computerCards = drawCard(
                playerCards, cards), drawCard(computerCards, cards)

        # calculate score & output result
        playerScore = addCards(playerCards)
        computerScore = addCards(computerCards)
        print(f"   Your cards: {playerCards}", f"current score: {playerScore}"
              "\n   Computer's first card: ", computerCards[0])
        if playerScore == 21 or computerScore == 21:
            gameEnd(playerCards, computerCards, playerScore,
                    computerScore, game_continue)

        # random mechanism for computer to draw another hand
        x = random.choice(cards)
        while computerScore < 21:
            if x < 5:
                computerCards = drawCard(computerCards, cards)
            break
        # do you want another card?
        while playerScore < 21:
            playerDecision = str(input(
                "\nType 'y' to get another card, type 'n' to pass: "))
            # nope
            if playerDecision == 'n':
                gameEnd(playerCards, computerCards, playerScore,
                        computerScore, game_continue)
                break
            # yes
            elif playerDecision == 'y':
                # draw another card for player
                playerCards = drawCard(playerCards, cards)
                playerScore = addCards(playerCards)
                if playerScore == 21:
                    gameEnd(playerCards, computerCards, playerScore,
                            computerScore, game_continue)
                elif playerScore > 21:
                    if 11 in playerScore:
                        ace = playerScore.index(11)
                        ace = 1
                else:
                    print(f"   Your cards: {playerCards}",
                          f"   current score: {playerScore}")
                    continue

# if the score is > 21 and there is an 11 in playerCards, change it into a 1


game()
