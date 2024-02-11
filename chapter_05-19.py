'''
Write a program that prompts the user to enter an integer
from 1 to 15 and displays a pyramid, as shown in the following sample run:
Enter the number of lines:
'''

n = eval(input('Enter value between 1 to 15: '))

for i in range(1, n + 1):
    formatSpec = str(3 * (n - i)) + 's';
    print(format('',formatSpec), end='')
    for j in range(i, 0, -1):
        print(format(j, '3d'), end='')
    for k in range(2, i + 1):
        print(format(k, '3d'), end='')
    print()




