'''
(Binary to hex) Write a function that parses a binary number into a hex number.
The function header is:
def binaryToHex(binaryValue):
Write a test program that prompts the user to enter a binary number and displays the corresponding hexadecimal value.
'''


def binaryToHex(binaryValue):
    binaryNum = int(binaryValue)
    temp = 0
    mul = 1
    count = 1

    hexaDeciNumber = ['0'] * 100

    i = 0
    while binaryNum != 0:
        rem = binaryNum % 10
        temp = temp + (rem * mul)

        if count % 4 == 0:
            if temp < 10:
                hexaDeciNumber[i] = chr(temp + 48)
            else:
                hexaDeciNumber[i] = chr(temp + 55)
            mul = 1
            temp = 0
            count = 1
            i = i + 1
        else:
            mul = mul * 2
            count = count + 1
        binaryNum = int(binaryNum / 10)

    if count != 1:
        hexaDeciNumber[i] = chr(temp + 48)

    if count == 1:
        i = i - 1

    while i >= 0:
        print(end=hexaDeciNumber[i])
        i = i - 1

binaryValue = eval(input('Enter binary value: '))
binaryToHex(binaryValue)