# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇

if len(two_digit_number) > 1:
    a = int(two_digit_number[0])
    b = int(two_digit_number[1])
    print(a + b)
else:
    print("You need to enter a two digit number.\nPlease try  again.")
