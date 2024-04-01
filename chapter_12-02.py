'''
The Location Class:
Enter the number of rows and columns in the list:
Enter row 0:
Enter row 1:
Enter row 2:
The location of the largest element is 45 at (1, 2)
'''


class Location:

    def __init__(self, row, column, maxValue):
        self.__row = row
        self.__column = column
        self.__maxValue = maxValue

    def getRow(self):
        return self.__row

    def getColumn(self):
        return self.__column

    def getMaxValue(self):
        return self.__maxValue

def locateLargest(a):
    maxValue = maxRowIndex = maxColIndex = 0
    for i in range(0, rows):
        for j in range(0, cols):
            if a[i][j] > maxValue:
                maxValue = a[i][j]
                maxRowIndex = i
                maxColIndex = j

    return Location(maxRowIndex, maxColIndex, maxValue)

m = []
rows, cols = eval(input('Enter the number of rows and columns in the list: '))
for i in range(0, rows):
    m.append([float(num) for num in input('Enter row {}: '.format(i)).split()])

l1 = locateLargest(m)
print('The location of the largest element is {} at ({}, {})'.format(l1.getMaxValue(), l1.getRow(), l1.getColumn()))



