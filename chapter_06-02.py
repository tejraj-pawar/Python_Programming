'''
(Sum the digits in an integer) Write a function that computes the sum of the digits
in an integer. Use the following function header:
def sumDigits(n):
'''

def sumDigits(n):
    sum = 0
    while(n > 0):
        sum = sum + (n % 10);
        n //= 10

    return sum

print(sumDigits(1111))