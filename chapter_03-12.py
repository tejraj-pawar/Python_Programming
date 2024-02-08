'''
 Write a program that prompts the user to enter the length of star and draw a star.
'''

import turtle

length = eval(input("Enter the length of the star: "))

turtle.showturtle()

turtle.forward(length)
turtle.left(324)
turtle.backward(length)
turtle.left(324)
turtle.forward(length)
turtle.left(324)
turtle.backward(length)
turtle.left(324)
turtle.forward(length)
turtle.left(324)
turtle.hideturtle()

turtle.done()