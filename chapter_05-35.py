'''
(Perfect number) A positive integer is called a perfect number if it is equal to the
sum of all of its positive divisors, excluding itself.
For example, 6 is the first perfect number, because The next is 28 = 14 + 7 + 4 + 2 + 1.
There are four perfect numbers less than 10,000. Write a program to find these
four numbers.'''

for i in range(10000, 1, -1):
    sum = 0
    for j in range(i//2, 0, -1):
        if i % j == 0:
            sum += j
    if(sum == i):
        print(i)


