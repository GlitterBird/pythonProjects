import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo.logo)


def caesar(word, shift_amount, instruction):
    """Takes in a string and  shifts it by the given shift number to either decode or encode it."""
    final = ""
    shift_amount = shift_amount % 26
    if direction == "decode":
        shift_amount *= -1

    for char in word:
        if char in alphabet:
            index = alphabet.index(char)
            index += shift_amount

            if direction == "encode" and index > 25:
                index -= 26
            elif direction == "decode" and index < 0:
                index += 26

            final += alphabet[index]
        else:
            final += char

    print(f"Here's your {instruction}d result: {final}")


keep_going = True
while keep_going:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    answer = input("\nWould you like to rerun the program? Enter 'Y' to continue and 'N' to stop: ").lower()
    if answer != 'y':
        keep_going = False
        print("Goodbye")