import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

nr_total_characters = nr_letters + nr_symbols + nr_numbers
password = ""

for number in range(1, nr_total_characters + 1):
    character_type = random.randint(1, 3)
    if character_type == 1:
        random_letter_index = random.randint(0, 25)
        password = password + letters[random_letter_index]
    if character_type == 2:
        random_number_index = random.randint(0, 9)
        password = password + numbers[random_number_index]
    if character_type == 3:
        random_symbol_index = random.randint(0, 8)
        password = password + symbols[random_symbol_index]

print(f"Your password is {password}")

