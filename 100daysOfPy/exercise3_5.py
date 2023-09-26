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

score1 = {}
score2 = {}

names = name1.lower() + name2.lower()
names = names.strip()

love_phrase1 = ['T', 'R', 'U', 'E']
love_phrase2 = ['L', 'O', 'V', 'E']

for char in names:
    if char.upper() in love_phrase1:
        score1[char] = score1.get(char, 0) + 1
    if char.upper() in love_phrase2:
        score2[char] = score2.get(char, 0) + 1

# print("This is score1: ", score1)
# print("This is score2: ", score2)

score1_count = 0
score2_count = 0
for k, v in score1.items():
    score1_count += v
for k, v in score2.items():
    score2_count += v

final_score = str(score1_count) + str(score2_count)
final_score_int = int(final_score)


if final_score_int < 10 or final_score_int > 90:
    print(
        f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score_int >= 40 and final_score_int <= 50:
    print(
        f"Your score is {final_score}, you are alright together."
    )
else:
    print(
        f"Your score is {final_score}."
    )
# print(f'Your final love score is {final_score}')
