# generate a random number between 1 and 100
# loop
#  Ask Guess the number between 1 and 100
# if user enter a number
#  if the number is correct
#   Print Congratulation message
#   Terminate
#  if the number is too low
#   Print Too low message
#  if the number is too high
#   Print Too high message
# Else
#  Print Invalid input message

import random
number_to_guess = random.randint(1, 100)
while True:
    try:
        user_input = int(input('Guess the number between 1 and 100: '))

        if user_input == number_to_guess:
            print('Congratulations! You guessed the number!')
            break
        elif user_input < number_to_guess:
            print('Too low! Try again.')
        elif user_input > number_to_guess:
            print('Too high! Try again.')
        else:
            print('Invalid input. Please enter a number between 1 and 100.')
    except ValueError:
        print('Invalid input. Please enter a number between 1 and 100.')
