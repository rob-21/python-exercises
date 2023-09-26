## --> Banker roulette <-- ##

# Import the random module here

# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

todays_winner = random.randint(1, (len(names)-1))

print(names[todays_winner], "is going to buy the meal today!")
