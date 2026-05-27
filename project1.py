# list of questions
# store the answers in a list
# randomly pick questions
# ask the questions
# see if they are correct
# keep track of the score
# tell the user their score
# {key as question and value as answer}

questions = {
    'What is the capital of France?': 'Paris',
    'What is the largest planet in our solar system?': 'Jupiter',
    'Who wrote "To Kill a Mockingbird"?': 'Harper Lee',
    'What is the chemical symbol for gold?': 'Au',
    'Who painted the Mona Lisa?': 'Leonardo da Vinci',
    'What is the smallest prime number?': '2',
    'What is the largest mammal?': 'Blue Whale',
    'Who is the author of "1984"?': 'George Orwell',
    'What is the square root of 64?': '8',
    'What is the currency of Japan?': 'Yen'
}

question_number = 0
mark = 0


def user_answer():
    global mark  # to modify the global variable mark

    question = list(questions.keys())[question_number]
    answer = questions[question]
    user_answer = input(f'{question} ').strip()
    if user_answer.lower() == answer.lower():
        print('Correct!')
        mark += 1
    else:
        print('Incorrect!')


while question_number < len(questions):
    user_answer()
    question_number += 1
    print(f'Your score is {mark}.')
print(f'Your final score is {mark} out of {len(questions)}.')
