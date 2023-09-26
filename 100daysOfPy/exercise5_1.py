## --> Average height <-- ##

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

counter = 0
total = 0
for h in student_heights:
    counter += 1
    total += h

average_height = total / counter
print(int(round(average_height)))

# Write your code below this row 👇
