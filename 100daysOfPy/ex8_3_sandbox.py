from string import punctuation


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = 'encode'
shift = 5
text_list = ['meet', 'me', 'at', '3']


def cesar(cipher_direction, start_text, shift_amount):
    final_text_list = []
    final_text = ''
    char_dict = {}
    for word in text_list:
        # print(word)
        new_word = ''
        if cipher_direction == "decode":
            shift_amount *= -1
        for letter in word:
            for letter in set(punctuation) or letter in range(0, len(start_text)):
                # need to ignore special characters / numbers
                char_dict[letter] = start_text.index(letter)
                break
            # print(letter)
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            new_letter = alphabet[new_position]
            new_word += new_letter
        final_text_list.append(new_word)
    for k, v in char_dict.items():
        final_text_list.insert(v, k)
    # print(final_text_list)
    final_text = ' '.join(final_text_list)

    print(f"The {cipher_direction}d text is {final_text}.")


cesar(
    cipher_direction=direction,
    start_text=text_list,
    shift_amount=shift)
