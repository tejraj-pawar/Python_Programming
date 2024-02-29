'''
(Count occurrence of numbers) Write a program that reads some integers
between 1 and 100 and counts the occurrences of each. Here is a sample run of the program:
Enter integers between 1 and 100: 2 5 6 5 4 3 23 43 2
2 occurs 2 times
3 occurs 1 time
Note that if a number occurs more than one time, the plural word “times” is used in the output.
'''

inputList = []
n = int(input('Enter the nos of element: '))

for _ in range(n):
    inputList.append(int(input('Enter a number: ')))

countList = [0] * 100

for num in inputList:
    countList[num] += 1

for i in range(0, len(countList)):
    if countList[i] == 0:
        continue
    elif countList[i] == 1:
        print('{} occurs 1 time'.format(i))
    else:
        print('{} occurs {} times'.format(i, countList[i]))

