## --> Caesar Cipher <-- ##

# As apart from exercise8_3_initial.py, the purpose of this final version is to unite all
# functions and conditionals into one single bit of code, instead of it being broken down into 3.

from caesar_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


def cesar(cipher_direction, start_text, shift_amount):
    final_text = ''
    if cipher_direction == 'decode':
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % 26
            final_text += alphabet[new_position]
        else:
            final_text += char
    print(f"The {cipher_direction}d text is '{final_text}'")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cesar(
        cipher_direction=direction,
        start_text=text,
        shift_amount=shift)
    final_action = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if final_action == 'no':
        print("Goodbye")
        should_continue = False
