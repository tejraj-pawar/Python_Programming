'''
(Sort students)
Enter students’ names and scores: John 34 Jim 45 Peter 59 Tim 45
John 34
Jim 45
Tim 45
Peter 59
'''

l1 = input('Enter students’ names and scores: ').split(' ')
l2 = []
for i in range(0, len(l1), 2):
    newList = [l1[i], int(l1[i + 1])]
    l2.append(newList)

l2.sort(key=lambda x: x[1])

for pair in l2:
    print('{} {}'.format(pair[0], pair[1]))
