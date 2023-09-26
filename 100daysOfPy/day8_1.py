
name = input("What's your name? \n").capitalize()
location = input("And where do you live? \n").capitalize()
# def greet(param):
#     print(f"Hi, {param}")


# greet(name)


def greet_with(nombre, deDonde):
    print(f"Hi {nombre}!")
    print(f"How's the weather like in {deDonde}?")


greet_with(name, location)
