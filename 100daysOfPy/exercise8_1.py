## --> Area calculation <-- ##

# 1 can of paint can cover 5 square meters (of wall)
# number of cans = (wall height x wall width) / coverage per can.

# e.g. Height = 2, Width = 4, Coverage = 5
# number of cans = (2 * 4) / 5
#    = 1.6
# then this final number should get rounded

def paint_calc(height, width, cover):
    number_of_cans = round((height * width)/coverage)
    print(f"You'll need {number_of_cans} cans of paint.")


# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
