'''
(Palindrome integer) Write the functions with the following headers:
'''


def reverse(num):
    return int(str(num)[::-1])


def isPalindrome(num):
    return num == reverse(num)


print(isPalindrome(123))
