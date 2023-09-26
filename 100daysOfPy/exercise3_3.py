## --> Leap year <-- ##

# a leap year occurs once every 4 years (if year % 4 == 0)
# this is still a little too much, so every 100 years (if year % 100 == 0), a leap year is skipped.
# however this is still a little too much, so every 400 years (if century % 400 == 0), then there is an actual leap year

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

if year % 400 == 0:
    print("Leap year.")
elif year % 100 == 0:
    print("Leap year.")
elif year % 4 == 0:
    print("Leap year.")
else:
    print("Not leap year.")
