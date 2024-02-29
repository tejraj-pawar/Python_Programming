'''
(Markov matrix) An matrix is called a positive Markov matrix if each element is positive and the sum of the elements in each column is 1. Write the following function to check whether a matrix is a Markov matrix:
def isMarkovMatrix(m):
Enter a 3-by-3 matrix row by row:
0.15 0.875 0.375
0.55 0.005 0.225
0.30 0.12 0.4

It is a Markov matrix
'''
m = []

m.append([float(num) for num in input('Enter a 3-by-3 matrix row by row: \n').split()])
m.append([float(num) for num in input().split()])
m.append([float(num) for num in input().split()])

isMarkov = 1
for col in range(len(m[0])):
    sum = 0
    for row in range(len(m)):
        sum += m[row][col]
    if sum != 1:
        isMarkov = 0
        break


print('It is a Markov matrix' if isMarkov else 'It is not a Markov matrix')