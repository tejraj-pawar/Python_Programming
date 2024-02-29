'''
3 (Locate the largest element) Write the following function that returns the location of the largest element in a two-dimensional list:
def locateLargest(a):
Enter the number of rows in the list:
Enter a row: 23.5 35 2 10
Enter a row: 4.5 3 45 3.5
Enter a row: 35 44 5.5 11.6
The location of the largest element is at (1, 2)
'''
m = []
rowCount = eval(input('Enter the number of rows in the list: '))
for _ in range(rowCount):
    m.append([float(num) for num in input('Enter a row: ').split()])

max = col = row = 0
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] > max:
            max = m[i][j]
            row = i
            col = j

print('The location of the largest element is at ({}, {})'.format(row, col))

