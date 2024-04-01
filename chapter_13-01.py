'''
(Remove text) Write a program that removes all the occurrences of a specified
string from a text file. Your program should prompt the user to enter a filename
and a string to be removed. Here is a sample run:
Enter a filename:
Enter the string to be removed:
Done
'''
fileName = input('Enter a filename: ')
remove = input('Enter the string to be removed: ')

file = open(fileName, mode='r')
fileData = file.read()

fileData = fileData.replace(remove, '')

file = open(fileName, mode='w')
file.write(fileData)

