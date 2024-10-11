# Regular Expressions

# Regular expressions (regex) are patterns used to match sequences of characters in strings.
# In this project, to use Regular Expressions?
# Import modules from the Python standard library to build a password generator program.

import re
import secrets
import string

def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)

        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints
        if all(
                constraint <= len(re.findall(pattern, password))
                for constraint, pattern in constraints
        ):
            break

    return password

new_password = generate_password()
print('Generated password:', new_password)
