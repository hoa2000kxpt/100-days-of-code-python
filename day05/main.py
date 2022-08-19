"""
Password Generator Project
"""

import random

# Initialize letters, numbers, and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# The user enters the number of letters, symbols and number he/she expects
print("Welcome to the PyPassword Generator!")
nr_letters = (input("How many letters would you like in your password?\n"))
nr_symbols = (input(f"How many symbols would you like?\n"))
nr_numbers = (input(f"How many numbers would you like?\n"))

# If the letter or the symbol or the number is not a digit
if not nr_letters.isdigit() or not nr_symbols.isdigit() or not nr_numbers.isdigit():
    print("Invalid value, enter a number instead.")

# If not, continue the program
else:

    # Initialize the password
    password = []

    # Generate the random letter
    random_letter = random.randint(0, 51)
    for i in range(0, int(nr_letters)):
        random_letter = random.randint(0, 51)
        password.append(letters[random_letter])

    # Generate the random number
    random_number = random.randint(0, 9)
    for i in range(0, int(nr_numbers)):
        random_number = random.randint(0, 9)
        password.append(numbers[random_number])

    # Generate the random symbol
    random_symbol = random.randint(0, 8)
    for i in range(0, int(nr_symbols)):
        random_symbol = random.randint(0, 8)
        password.append(symbols[random_symbol])

    # Shuffle the password and display it randomly
    random.shuffle(password)
    print(f"Here is your password: {''.join(password)}")

    # If the length of password is not good, display warning
    if len(password) <= 6:
        print("Your password is weak, try to include at least 8 characters for a stronger password.")
    elif len(password) == 7:
        print("Your password is medium, try to include at least 8 characters for a stronger password.")
    else:
        print("Your password is strong.")
