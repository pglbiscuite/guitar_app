from scales import *
from artwork import *


#   Basic Linear Game Logic
def linear_check(training):
    score = 0

    for note in en_scale:
        if note == 'A':
            print(f'''What's the equivalent of {note}, in Romanian?''')     # Just For Testing
            answer = input('>>> ')
            if answer.lower() == 'la':
                score += 1
                print(f'Correct.{score} Streak.\n')
                if score_check(score, training):
                    break
            else:
                score = 0
                print(f'Wrong! The Correct Answer is "La". Streak back to {score}.\n')



        elif note == 'B':
            print(f'''What's the equivalent of {note}, in Romanian?''')  # Just For Testing
            answer = input('>>> ')
            if answer.lower() == 'si':
                score += 1
                print(f'Correct.{score} Streak.\n')
                if score_check(score, training):
                    break
            else:
                score = 0
                print(f'Wrong! The Correct Answer is "Si". Streak back to {score}.\n')

        elif note == 'C':
            print(f'''What's the equivalent of {note}, in Romanian?''')  # Just For Testing
            answer = input('>>> ')
            if answer.lower() == 'do':
                score += 1
                print(f'Correct.{score} Streak.\n')
                if score_check(score, training):
                    break
            else:
                score = 0
                print(f'Wrong! The Correct Answer is "Do". Streak back to {score}.\n')

        elif note == 'D':
            print(f'''What's the equivalent of {note}, in Romanian?''')  # Just For Testing
            answer = input('>>> ')
            if answer.lower() == 're':
                score += 1
                print(f'Correct.{score} Streak.\n')
                if score_check(score, training):
                    break
            else:
                score = 0
                print(f'Wrong! The Correct Answer is "Re". Streak back to {score}.\n')

        elif note == 'E':
            print(f'''What's the equivalent of {note}, in Romanian?''')  # Just For Testing
            answer = input('>>> ')
            if answer.lower() == 'mi':
                score += 1
                print(f'Correct.{score} Streak.\n')
                if score_check(score, training):
                    break
            else:
                score = 0
                print(f'Wrong! The Correct Answer is "Mi". Streak back to {score}.\n')

        elif note == 'F':
            print(f'''What's the equivalent of {note}, in Romanian?''')  # Just For Testing
            answer = input('>>> ')
            if answer.lower() == 'fa':
                score += 1
                print(f'Correct.{score} Streak.\n')
                if score_check(score, training):
                    break
            else:
                score = 0
                print(f'Wrong! The Correct Answer is "Fa". Streak back to {score}.\n')

        elif note == 'G':
            print(f'''What's the equivalent of {note}, in Romanian?''')  # Just For Testing
            answer = input('>>> ')
            if answer.lower() == 'sol':
                score += 1
                print(f'Correct.{score} Streak.\n')
                if score_check(score, training):
                    break
            else:
                score = 0
                print(f'Wrong! The Correct Answer is "Sol". Streak back to {score}.\n')


#   Simple Score Checking and Ending
def score_check(score, training):
    if score >= training:
        print('\nWell Done! Training Finished.')
        print(f'''You've successfully gathered an impressive score of: {score}.\n''')
        print(f'{model_see_you}')
        print(f'{model_artist}')
        print('\n\n\n')       # Temporary until we can exit the while loop
        return True
    return False
