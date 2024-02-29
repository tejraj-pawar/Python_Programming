'''
(Algebra: add two matrices)

Enter matrix1: 1 2 3 4 5 6 7 8 9
Enter matrix2: 0 2 4 1 4.5 2.2 1.1 4.3 5.2
The matrices are added as follows:
'''

def createMatrix(list):
    m1 = []
    for i in range(0, len(list), 3):
        row = []
        for j in range(i, i + 3):
            row.append(list[j])
        m1.append(row)

    return m1

m1Data = [float(num) for num in input('Enter matrix1: ').split()]
m2Data = [float(num) for num in input('Enter matrix2: ').split()]

m1 = createMatrix(m1Data)
m2 = createMatrix(m2Data)

result = []
for row in range(len(m1)):
    newRow = []
    for col in range(len(m1[0])):
        sum = m1[row][col] + m2[row][col]
        newRow.append(sum)
        print(format(sum, '6.2f'), end='')
    print()
    result.append(newRow)



