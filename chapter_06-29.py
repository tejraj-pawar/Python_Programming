'''
(Financial: credit card number validation)
'''

def getPrefix(number, k):
    if len(number) < k:
        return number
    else:
        return int(str(number)[0:k]);

def getSize(d):
    return len(d)

def prefixMatched(number, d):
    return str(number).startswith(str(d))

def sumOfOddPlace(number):
    numList = [int(num) for num in str(number)]
    sum = 0
    for i in range(1,len(numList),2):
        sum += numList[i]
    return sum

def getDigit(number):
    if number <= 9:
        return number
    else:
        sum = 0
        while(number > 0):
            sum += number % 10
            number //= 10
        return sum

def sumOfDoubleEvenPlace(number):
    numList = [int(num) for num in str(number)]
    numList = [i * 2 for i in numList]

    sum = 0
    for i in range(len(numList) - 2, -1, -2):
        num = numList[i]
        if num <= 9:
            sum += num
        else:
            sum += getDigit(num)

    return sum


def validatePrefix(number, prefixList):
    for prefix in prefixList:
        if prefixMatched(number, prefix):
            return True
    return False


def isValid(number):
    cardNumLen = len(str(number))
    if cardNumLen >= 13 and cardNumLen <= 16 and validatePrefix(number, ['4', '5', '37', '6']):
        tempNum = sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)
        if tempNum % 10 == 0:
            print("Credit Card is valid!!")
        else:
            print('Credit Card is Invalid!!')

cardNumber = int(eval(input('Please enter a credit card number: ')))
isValid(cardNumber)



