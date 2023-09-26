# Life in weeks

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

age_number = int(age)

months = (12 * 90) - (age_number * 12)
weeks = (52*90) - (age_number * 52)
days = (365*90) - (age_number * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
