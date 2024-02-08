'''
Write a program that prompts the user to enter a four-digit integer and displays the number in reverse order. Here is a sample run:
abgdPzhu.
Enter an integer: 3125
The reversed number is 5213
'''

num = eval(input("Enter an integer: "))

while num > 0:
    print(num % 10, end='')
    num = num // 10
