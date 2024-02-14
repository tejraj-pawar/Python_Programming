'''
(Check password) Some Web sites impose certain rules for passwords. Write a
function that checks whether a string is a valid password. Suppose the password
rules are as follows:
■ A password must have at least eight characters.
■ A password must consist of only letters and digits.
■ A password must contain at least two digits.
Write a program that prompts the user to enter a password and displays valid
password if the rules are followed or invalid password otherwise.
'''

def isValidPassword(password):
    if len(password) < 8:
        return False

    if not str.isalnum(password):
        return False

    digitCount = 0
    for chr in password:
        if str.isdigit(chr):
            digitCount += 1
        if digitCount == 2:
            return True

    return False

password = eval(input('Enter a password:'))
print('Password is invalid', isValidPassword(password))