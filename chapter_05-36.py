'''
(Game: scissor, rock, paper) Programming Exercise 4.17 gives a program that
plays the scissor, rock, paper game. Revise the program to let the user
play continuously until either the user or the computer wins more than two times.
'''

import random

computerWinCount = 0
userWinCount = 0

while(computerWinCount < 2 and userWinCount < 2):
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

        if userWin:
            userWinCount += 1
        else:
            computerWinCount += 1

print('Computer won count:', computerWinCount, 'User won count:', userWinCount)

