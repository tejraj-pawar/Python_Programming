'''
(Count characters, words, and lines in a file)
'''

fileName = input('Enter a filename: ')

file = open(fileName, mode='r')

linesCount = wordsCount = charsCount = 0

with open(fileName, mode='r') as file:

    for line in file:
        linesCount += 1

        for letter in line:
            if str.isspace(letter):
                wordsCount += 1
                continue

            charsCount += 1

print('{} characters \n{} words \n{} lines'.format(charsCount, wordsCount, linesCount))
