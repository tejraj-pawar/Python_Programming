'''
(Find the character of an ASCII code) Write a program that receives an ASCII
code (an integer between 0 and 127) and displays its character. For example, if the
user enters 97, the program displays the character a.

Enter an ASCII code: 69
The character is E
'''

asciiCode = eval(input("Enter an ASCII code: "))

print("The character is", chr(asciiCode))