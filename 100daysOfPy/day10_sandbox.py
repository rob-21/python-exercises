# fname = "robert"
# lname = "diaconeasa"


def formatName(f_name, l_name):
    """Takes in a first name and last name, and capitalizes them."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs "

    formated_f_name, formated_l_name = f_name.title(), l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"


print(formatName(input("What's your first name?\n"),
      input("What's your last name?\n")))


formatName()
