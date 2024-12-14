from scales import *


#   Basic Linear Game Logic
def linear_check():
    for note in en_scale:
        if note == 'A':
            print(f'''What's the equivalent of {note}, in Romanian?''')     # Just For Testing
            answer = input('>>> ')
            if answer.lower() == 'la':
                print('Correct.\n')
            else:
                print('Wrong! The Correct Answer is "La".\n')

        elif note == 'B':
            print(f'''What's the equivalent of {note}, in Romanian?''')  # Just For Testing
            answer = input('>>> ')
            if answer.lower() == 'si':
                print('Correct.\n')
            else:
                print('Wrong! The Correct Answer is "Si".\n')

        elif note == 'C':
            print(f'''What's the equivalent of {note}, in Romanian?''')  # Just For Testing
            answer = input('>>> ')
            if answer.lower() == 'do':
                print('Correct.\n')
            else:
                print('Wrong! The Correct Answer is "Do".\n')

        elif note == 'D':
            print(f'''What's the equivalent of {note}, in Romanian?''')  # Just For Testing
            answer = input('>>> ')
            if answer.lower() == 're':
                print('Correct.\n')
            else:
                print('Wrong! The Correct Answer is "Re".\n')

        elif note == 'E':
            print(f'''What's the equivalent of {note}, in Romanian?''')  # Just For Testing
            answer = input('>>> ')
            if answer.lower() == 'mi':
                print('Correct.\n')
            else:
                print('Wrong! The Correct Answer is "Mi".\n')

        elif note == 'F':
            print(f'''What's the equivalent of {note}, in Romanian?''')  # Just For Testing
            answer = input('>>> ')
            if answer.lower() == 'fa':
                print('Correct.\n')
            else:
                print('Wrong! The Correct Answer is "Fa".\n')

        elif note == 'G':
            print(f'''What's the equivalent of {note}, in Romanian?''')  # Just For Testing
            answer = input('>>> ')
            if answer.lower() == 'sol':
                print('Correct.\n')
            else:
                print('Wrong! The Correct Answer is "Sol".\n')