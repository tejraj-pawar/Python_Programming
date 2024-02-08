'''
(Game: lottery) Revise Listing 4.10, Lottery.py, to generate a three-digit lottery
number. The program prompts the user to enter a three-digit number and determines whether the user wins according to the following rules:
1. If the user input matches the lottery number in the exact order, the award is $10,000.
2. If all the digits in the user input match all the digits in the lottery number, the award is $3,000.
3. If one digit in the user input matches a digit in the lottery number, the award is $1,000.
'''

import random

lotteryNumber = random.randint(100, 999)
print('Lottery Number: ', lotteryNumber)
userLotteryNumber = eval(input('Enter three-digit lottery number: '))


lotteryNumberDigit1 = lotteryNumber // 100
lotteryNumberDigit2 = (lotteryNumber % 100) // 10
lotteryNumberDigit3 = (lotteryNumber % 100) % 10

userLotteryNumberDigit1 = userLotteryNumber // 100
userLotteryNumberDigit2 = (userLotteryNumber % 100) // 10
userLotteryNumberDigit3 = (userLotteryNumber % 100) % 10

userLotteryNumberList = [userLotteryNumberDigit1, userLotteryNumberDigit2, userLotteryNumberDigit3]
if lotteryNumber == userLotteryNumber:
    print('Reward is $10,000.')
elif (lotteryNumberDigit1 in userLotteryNumberList) and (lotteryNumberDigit2 in userLotteryNumberList) and (lotteryNumberDigit3 in userLotteryNumberList):
    print('Reward is $3,000.')
elif (lotteryNumberDigit1 in userLotteryNumberList) or (lotteryNumberDigit2 in userLotteryNumberList) or (lotteryNumberDigit3 in userLotteryNumberList):
    print('Reward is $1,000.')
else:
    print('No Reward!')


