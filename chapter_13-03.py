'''
Process a score in textfile
'''

fileName = input('Enter a filename: ')

with open(fileName, 'r') as file:
    data = file.read()
    scores = [int(score) for score in data.split()]

    total = 0
    for score in scores:
        total += score

print('There are {} scores \nThe total is {} \nThe average is {}'.format(len(scores), total, round(total/len(scores), 2)))