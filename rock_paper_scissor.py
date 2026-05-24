# ask user to choose rock paper and siccors
# if user enters rock
#  print you chose rock emj
# if user enters paper
#  print you chose paper emj
# if user enters scissors
#  print you chose scissors emj
# else
#  print invalid input message
# the computer will choose ramdomly between rock paper and scissors
# compare user choice and computer choice
import random
ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
emojis = {
    ROCK: '🪨',
    PAPER: '📄',
    SCISSORS: '✂️'
}
choices = tuple(emojis.keys())


def get_user_choice():
    while True:
        user_choice = input('Rock, Paper, Scissors? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid choice! Please enter r, p, or s.')


def display_choice(user_choice, random_choice):
    print(f'You chose: {emojis[user_choice]}')
    print(f'Computer chose: {emojis[random_choice]}')


def determine_winner(user_choice, random_choice):
    if user_choice == random_choice:
        print('It\'s a tie!')
    elif ((user_choice == ROCK and random_choice == SCISSORS) or
          (user_choice == PAPER and random_choice == ROCK) or
          (user_choice == SCISSORS and random_choice == PAPER)):
        print('You win!')
    else:
        print('You Lose!')


def play_game():
    while True:

        user_choice = get_user_choice()

        random_choice = random.choice(choices)

        display_choice(user_choice, random_choice)

        determine_winner(user_choice, random_choice)

        should_continue = input('Play again? (y/n): ').lower()
        if should_continue == 'n':
            print('Thanks for playing!')
            break


play_game()
