'''
(Palindromic prime) A palindromic prime is a prime number that is also palindromic.
For example, 131 is a prime and also a palindromic prime, as are 313 and 757.
Write a program that displays the first 100 palindromic prime numbers.
Display 10 numbers per line and align the numbers properly, as follows:
2 3 5 7 11 101 131 151 181 191
313 353 373 383 727 757 787 797 919 929
'''
import sys


def isPrime(num):
    for i in range(num//2, 1, -1):
        if num % i == 0:
            return False
    return True

def isPalindrome(num):
    return num == int(str(num)[::-1])

def isPalindromePrime(num):
    return isPrime(num) and isPalindrome(num)


count = 0

for i in range(2, sys.maxsize):

    if count == 100:
        break

    if isPalindromePrime(i):
        count += 1
        print(format(i, '6d'), end='')
        if(count % 10 == 0):
            print()



