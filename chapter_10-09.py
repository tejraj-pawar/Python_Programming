'''
(Statistics: compute deviation)

Enter numbers: 1.9 2.5 3.7 2 1 6 3 4 5 2
The mean is 3.11
The standard deviation is 1.55738
'''

st1 = input('Enter numbers: ')
numList = st1.split()
n = len(numList)

sum1 = 0
for num in numList:
    sum1 += float(num)
mean = sum1 / n
print('The mean is ', round(mean, 2))

sum2 = 0
for num in numList:
    sum2 += (float(num) - mean) ** 2

deviation = (sum2 / (n -1)) ** 0.5
print('The standard deviation is', round(deviation, 2))