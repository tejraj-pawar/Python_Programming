'''
(Count the letters in a string) Write a function that counts the number of letters in
a string using the following header:
def countLetters(s):
Write a test program that prompts the user to enter a string and displays the number of letters in the string.
'''

def countLetters(st1):
    letterCount = 0

    for chr in st1:
        if str.isalpha(chr):
            letterCount += 1

    return letterCount

st1 = eval(input('Enter a String: '))
print('Number of letters are', str(countLetters(st1)))
