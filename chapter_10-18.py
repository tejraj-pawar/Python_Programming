'''
(Game: Eight Queens)
'''

def nQueens(n):
    cols = set()
    negDiagonal = set()
    posDiagonal = set()

    response = []
    board = [['.'] * n for _ in range(n)]

    def backTrack(r):
        if r == n:
            copy = [''.join(row) for row in board]
            response.append(copy)
            return response

        for c in range(n):
            if c in cols or (r + c) in posDiagonal or (r - c) in negDiagonal:
                continue

            cols.add(c)
            negDiagonal.add(r - c)
            posDiagonal.add(r + c)
            board[r][c] = 'Q'

            backTrack(r + 1)

            cols.remove(c)
            negDiagonal.remove(r - c)
            posDiagonal.remove(r + c)
            board[r][c] = '.'

    backTrack(0)

    return response

num = eval(input('Enter number of queens: '))
response = nQueens(num)
print('There are total {} ways to plot n-queens: {}'.format(len(response), response))

sol1 = response[0]

print('One possible representation is: ')
for row in range(len(sol1)):
    cols = sol1[row]
    for i in range(len(cols)):
        print(format(cols[i], '3s'), end='')
    print()












