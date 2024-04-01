'''
(Count the occurrences of each keyword) Write a program that reads in a Python
source code file and counts the occurrence of each keyword in the file.
Your program should prompt the user to enter the Python source code filename.
'''

fileName = input('Enter a file name: ')

keywordCount = {}
with open(fileName, 'r') as file:
    for line in file:
        line = line.replace('\n', '')
        for keyword in line.split(' '):
            if keyword in keywordCount:
                keywordCount[keyword] += 1
            else:
                keywordCount[keyword] = 1

print(keywordCount)