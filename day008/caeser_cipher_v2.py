alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    if cipher_direction == 'decode':
        shift_amount *= -1

    end_text = ""
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            shifted_position = position + shift_amount
            if cipher_direction == 'encode' and shifted_position > 25:
                shifted_position -= 26
            elif cipher_direction == "decode" and shifted_position < 0:
                shifted_position += 26
            end_text += alphabet[shifted_position]
        else:
            end_text += letter

    print(f"The {cipher_direction}d text is {end_text}")

from art import logo
print(logo)
should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(start_text = text, shift_amount = shift, cipher_direction = direction)

    restart = input("Type 'yes' if you want to go again, otherwise type 'no'\n")
    if restart == "no":
        should_end = True
        print("Goodbye!")
