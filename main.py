import random
import string

Generated_password = []

print("Welcome to the Password Generator!")
password_character = int(input("Enter the total number of characters in the password:"))
Password_letter = int(input("Enter the number of letters in the password:"))
password_number = int(input("Enter the number of numbers in the password:"))
password_symbol = int(input("Enter the number of symbols in the password:"))

if password_character != Password_letter + password_number + password_symbol:
    print("Invalid input. The sum of letters, numbers, and symbols does not match the password")
else:
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    password_chars = (
    random.choices(letters, k=Password_letter) +
    random.choices(numbers, k=password_number) +
    random.choices(symbols, k=password_symbol)

    )

    random.shuffle(password_chars)

    password = "".join(password_chars)

    print("\nGenerated Password:", password)
