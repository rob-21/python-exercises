## --> Love calcultor <-- ##

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."

# Write your code below this line 👇

names = name1.lower() + name2.lower()

love_phrase1 = ['T', 'R', 'U', 'E']
love_phrase2 = ['L', 'O', 'V', 'E']

score1 = []
score2 = []

name_characters = []
for i in names:
    name_characters.append(i)

print("Name characters: ", name_characters)

for char in love_phrase1:
    if char.lower() not in name_characters:
        continue
    else:
        score1.append(char)

for char in love_phrase2:
    if char.lower() not in name_characters:
        continue
    else:
        score2.append(char)

final_score = str(len(score1)) + str(len(score2))

print("Score1: ", score1)
print("Score2: ", score2)
print("Final score: ", final_score)
