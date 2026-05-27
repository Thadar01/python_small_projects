# collect user preferences
# length
# upper
# special
# digits

# generate password based on preferences

import random
import string


def generate_password():
    is_valid_length = False
    while not is_valid_length:
        try:
            length = int(input("Enter the desired password length: ").strip())
            if length < 8:
                print("Password length should be at least 8 characters.")
            else:
                is_valid_length = True
        except ValueError:
            print("Please enter a valid number for password length.")
     # this is use to stop code execution

    include_uppercase = input(
        "Include uppercase letters? (y/n): ").strip().lower()
    include_special = input(
        "Include special characters? (y/n): ").strip().lower()
    include_digits = input("Include digits? (y/n): ").strip().lower()

    if length < 8:
        print("Password length should be at least 8 characters.")
        return  # this is use to stop code execution

    lowercase = string.ascii_lowercase  # give all lowercase letters
    # inline if statement
    uppercase = string.ascii_uppercase if include_uppercase == 'y' else ''
    special = string.punctuation if include_special == 'y' else ''
    digits = string.digits if include_digits == 'y' else ''

    all_characters = lowercase + uppercase + special + digits
    required_characters = []
    if include_uppercase == 'y':
        required_characters.append(random.choice(uppercase))
    if include_special == 'y':
        required_characters.append(random.choice(special))
    if include_digits == 'y':
        required_characters.append(random.choice(digits))

    remaining_length = length - len(required_characters)
    password = required_characters
    for _ in range(remaining_length):
        chracter = random.choice(all_characters)
        password.append(chracter)
    print("Generated Password:", ''.join(password))


generate_password()
