'''
(Sorted?) Write the following function that returns true if the list is already sorted in increasing order:
def isSorted(lst):
Write a test program that prompts the user to enter a list and displays whether the
list is sorted or not. Here is a sample run:
Enter list: 1 1 3 4 4 5 7 9 10 30 11
The list is not sorted
'''

st1 = input('Enter numbers: ')
numList = st1.split()


n1 = list(numList)
n1.sort()

if n1 == numList:
    print('The list is sorted')
else:
    print('The list is not sorted')