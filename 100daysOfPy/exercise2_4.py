### ---> Tip calculator <--- ###

# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

print('Welcome to the tip calculator.')

bill_total = float(
    input('What was the total bill? $'))
percentage_tip = int(
    input('What percentage tip would you like to give? 10, 12 or 15? '))
number_of_people = int(
    input('How many people to split the bill? '))

percentage_tip = percentage_tip/100 + 1

pay_per_person = (bill_total / number_of_people) * percentage_tip

print("Each person should pay: $ %.2f" % pay_per_person)
