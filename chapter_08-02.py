'''
(Check substrings) You can check whether a string is a substring of another string
by using the find method in the str class. Write your own function to implement
find. Write a program that prompts the user to enter two strings and then checks
whether the first string is a substring of the second string.
'''

def find(st1, st2):
    return str.find(st2, st1)


st1, st2 = eval(input('Enter two strings: '))
if find(st1, st2) != -1:
    print('first string is a substring of the second string')



