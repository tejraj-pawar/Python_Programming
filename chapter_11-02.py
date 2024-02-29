'''
(Sum the major diagonal in a matrix)
Enter a 4-by-4 matrix row for row 1: 1 2 3 4
Enter a 4-by-4 matrix row for row 2: 5 6.5 7 8
Enter a 4-by-4 matrix row for row 3: 9 10 11 12
Enter a 4-by-4 matrix row for row 4: 13 14 15 16
Sum of the elements in the major diagonal is 34.5
'''

matrix = []
matrix.append([float(num) for num in input('Enter a 4-by-4 matrix row for row 1: ').split(' ')])
matrix.append([float(num) for num in input('Enter a 4-by-4 matrix row for row 2: ').split(' ')])
matrix.append([float(num) for num in input('Enter a 4-by-4 matrix row for row 3: ').split(' ')])
matrix.append([float(num) for num in input('Enter a 4-by-4 matrix row for row 4: ').split(' ')])

sum = 0
for i in range(0, len(matrix)):
    sum += matrix[i][i]

print('Sum of the elements in the major diagonal is', sum)
