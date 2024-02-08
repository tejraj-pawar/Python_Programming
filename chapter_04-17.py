'''
(Game: scissor, rock, paper) Write a program that plays the popular scissor-rockpaper game. (A scissor can cut a paper, a rock can knock a scissor, and a paper can
wrap a rock.) The program randomly generates a number 0, 1, or 2 representing
scissor, rock, and paper. The program prompts the user to enter a number 0, 1, or
2 and displays a message indicating whether the user or the computer wins, loses,
or draws. Here are sample runs:

scissor (0), rock (1), paper (2):
The computer is scissor. You are rock. You won.
'''

import random

computer = random.randint(0, 2)
user = eval(input('scissor (0), rock (1), paper (2): '))

if computer == 0:
    print('The computer is scissor')
elif computer == 1:
    print('The computer is rock')
else:
    print('The computer is paper')

if user == 0:
    print('The user is scissor')
elif user == 1:
    print('The user is rock')
else:
    print('The user is paper')

if user == computer:
    print('Its a draw.')
else:
    # user can only win in following three ways
    userWin = (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1)
    print('User won' if userWin else 'Computer won')
