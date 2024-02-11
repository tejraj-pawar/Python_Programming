'''
Write a program to sum the following series:
'''

sum = 0

for i in range(1, 98, 2):
    sum = sum + (i / (i+2))

print("Sum of series is", round(sum, 2))



