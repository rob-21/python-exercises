# BMI Calculator

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

height_number = float(height)
weight_number = float(weight)

BMI = weight_number / (height_number**2)
print(int(BMI))
