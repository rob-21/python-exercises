## --> Calculator - guided version <-- ##
import calcArt


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "x": multiply,
    "/": divide,
}


def calculator():
    print(calcArt.logo)
    n1 = float(input("What's the first number?: "))

    for o in operations:
        print(o)

    should_continue = True

    while should_continue:
        operation = input("Pick an operation from the ones above: ")
        n2 = float(input("What's the second number?: "))
        answer = operations[operation](n1, n2)

        print(f"{n1} {operation} {n2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            n1 = answer
        else:
            should_continue = False
            calculator()


calculator()
