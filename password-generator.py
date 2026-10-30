import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', '?', '@', '[', ']', '^', '_', '{', '|', '}', '~']

letetrs_input = int(input("How many letters should include: "))
numbers_input = int(input("How many numbers should include: "))
symbols_input = int(input("How many symbols should include: "))

password_list = []
password = ""

for letter_count in range(0,letetrs_input):
    random_letters = random.choice(letters)
    password_list += random_letters

for number_count in range(0,numbers_input):
    random_numbers = random.choice(numbers)
    password_list += random_numbers

for symbol_count in range(0,symbols_input):
    random_symbols = random.choice(symbols)
    password_list += random_symbols

random.shuffle(password_list)

for character in password_list:
    password += character

print(f"Your password is: {password}")










