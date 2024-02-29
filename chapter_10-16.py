'''
Bubble sort
'''

st1 = input('Enter numbers: ')
l1 = st1.split()
l1 = [int(n) for n in l1]

for i in range(0, len(l1)):
    for j in range(0, len(l1) - 1):
        if l1[j+1] < l1[j]:
            l1[j+1],l1[j] = l1[j],l1[j+1]

print('Sorted List:', l1)