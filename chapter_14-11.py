'''
(Count consonants and vowels) Write a program that prompts the user to enter a
text filename and displays the number of vowels and consonants in the file. Use
a set to store the vowels A, E, I, O, and U.
'''

fileName = input('Enter a file name: ')

vowelsCount = consonantsCount = 0
vowels = {'A', 'E', 'I', 'O', 'U'}
with open(fileName, 'r') as file:
    for line in file:
        for letter in line:
            if not str.isspace(letter):
                if letter in vowels:
                    vowelsCount += 1
                else:
                    consonantsCount += 1

print('Vowels Counts: {}, Consonants Count: {}'.format(vowelsCount, consonantsCount))
