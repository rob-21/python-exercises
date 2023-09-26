## --> Calculator - entirely alone <-- ##
import calcArt
import os

print(calcArt.logo)


def calculator(n1, n2, operation):
    if operation == "+":
        return n1+n2
    elif operation == "-":
        return n1-n2
    elif operation == "x" or operation == "X" or operation == "*":
        return n1*n2
    elif operation == "/":
        return n1/n2


should_continue = True
init = 0
while should_continue:
    if init == 0:
        n1 = float(input("What's the first number?: "))
        init = n1
    operation = input("Pick an operation: ")
    n2 = float(input("What's the second number?: "))
    result = calculator(init, n2, operation)
    os.system('clear')

    print(init, operation, n2, "=", result)

    more_operations = input(
        f"\nType 'y' to continue operating with {result}, type 'n' to start a new calculation, or 'q' to quit: ")
    if more_operations == "y":
        init = result
        continue
    elif more_operations == "n":
        init = 0
        continue
    elif more_operations == "q":
        quit()
