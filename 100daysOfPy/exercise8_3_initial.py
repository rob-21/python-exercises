## --> Caesar Cipher <-- ##


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# In order fo the below 'encode' function to work (and not return 'index out of range' for words such as 'zulu', shift=5 , we have duplicated the characters in the list.
# this way the .index() function still works (returns the index of the fist match) and never outputs 'index out of range'.

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def encrypt(plain_text, shift_amount):

    # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.

    # e.g.
    # plain_text = "hello"
    # shift = 5
    # cipher_text = "mjqqt"
    # print output: "The encoded text is mjqqt"

    # HINT: How do you get the index of an item in a list:
    # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    # 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
    encrypted_text = ''
    for letter in plain_text:
        position = alphabet.index(letter)
        cipher_position = position + shift_amount
        cipher_letter = alphabet[cipher_position]
        encrypted_text += cipher_letter
    print(f"The encoded text is {encrypted_text}")

# TODO-4: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.


def decrypt(plain_text, shift_amount):
    decrypted_text = ''
    for letter in plain_text:
        position = alphabet.index(letter)
        proper_position = position - shift_amount
        proper_letter = alphabet[proper_position]
        decrypted_text += proper_letter
    print(f"The decoded text is {decrypted_text}")


# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print(f"{direction} is not a valid command. Please choose an existing option in order to proceed.")
