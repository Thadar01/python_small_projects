# Ask user a question
# if uer enters y
#  Generate two random numbers
#  Print them
# if user enters n
#  Print Thank you messgaey
#  Terminate
# Else
#  Print Invalid input message
import random

while True:
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1}, {die2})')
    elif choice == 'n':
        print('Thank you for playing!')
        break
    else:
        print('Invalid input. Please enter y or n.')
