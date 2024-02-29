'''
(Reverse the numbers entered) Write a program that reads a list of integers and
displays them in the reverse order in which they were read.
'''

inputList = []
n = int(input('Enter the nos of element: '))

for _ in range(n):
    inputList.append(int(input('Enter a number: ')))

print(inputList[::-1])