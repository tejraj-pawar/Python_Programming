'''
(Binary to decimal) Write a recursive function that parses a binary number as a
string into a decimal integer. The function header is as follows:
def binaryToDecimal(binaryString):
Write a test program that prompts the user to enter a binary string and displays its
decimal equivalent
'''

from math import pow

def binaryToDecimal(binaryString, i = 0):
    if binaryString == 0:
        return 0
    return (binaryString % 10) * pow(2, i) + binaryToDecimal(binaryString // 10, i + 1)


print(binaryToDecimal(1111))
