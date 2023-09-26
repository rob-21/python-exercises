## --> Silent Auction <-- ##

from auctionArt import logo
import os

print(logo)
print("\nWelcome to the secret auction program.")

bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n$"))

    bids.update({
        name: bid
    })

    anyone_else = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if anyone_else == 'no':
        os.system('clear')
        # print(bids)
        largest_bid = 0
        winner = ''
        for k, v in bids.items():
            if v > largest_bid:
                largest_bid = v
                winner = k
        print(f"The winner is {winner} with a bid of ${largest_bid}")
        continue_bidding = False

    else:
        os.system('clear')
