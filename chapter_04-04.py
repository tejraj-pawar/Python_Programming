'''
Write a program that generates two integers under 100 and
prompts the user to enter the sum of these two integers. The program then reports
true if the answer is correct, false otherwise.
'''

import random

num1 = random.randint(0, 100)
num2 = random.randint(0, 100)

#sum = eval(input("Please enter sum of " + str(num1) + " and " + str(num2) + " : "))
sum = eval(input("Please enter sum of {} and {} :".format(num1, num2)))
print("True" if sum == num1 + num2 else "False")