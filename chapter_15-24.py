'''
(Number of files in a directory) Write a program that prompts the user to enter a
directory and displays the number of files in the directory.
'''
import os

def listDirFiles(directoryName):
    dirList = os.listdir(directoryName)
    for item in dirList:
        if os.path.isdir(directoryName + '\\' + item):
            listDirFiles(directoryName + '\\' + item)
        else:
            print(directoryName + '\\' + item)

# Enter a absolute path
directory = input('Enter a directory name: ')
listDirFiles(directory)

