'''
(Largest rows and columns) Write a program that randomly fills in 0s and 1s into
a matrix, prints the matrix, and finds the rows and columns with the most
1s. Here is a sample run of the program:
0011
0011
1101
1010
The largest row index: 2
The largest column index: 2, 3
'''
import random

m = []
for row in range(4):
    newRow = []
    for col in range(4):
        newRow.append(random.randint(0,1))
    m.append(newRow)

maxRowIndex = 0
maxRowCount = 0
maxColIndex = 0
maxColCount = 0

for row in range(len(m)):
    rowCount = colCount = 0
    for col in range(len(m[0])):
        if m[row][col] == 1:
            rowCount += 1

        if m[col][row] == 1:
            colCount += 1

    if rowCount > maxRowCount:
        maxRowCount = rowCount
        maxRowIndex = row

    if colCount > maxColCount:
        maxColCount = colCount
        maxColIndex = row

print('The largest row index:', str(maxRowIndex))
print('The largest column index:', str(maxColIndex))




