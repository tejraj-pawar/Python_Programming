'''
(Turtle: plot the sine and cosine functions) Write a program that plots the sine
function in red and cosine in blue
'''

import math
import turtle

win = turtle.Screen()


# coordinate setting
win.setworldcoordinates(0, -2, 500, 2)


# vertical line
turtle.goto(0, 2)
turtle.goto(0, -2)
turtle.goto(0, 0)

# Horizontal line
turtle.goto(500, 0)
turtle.penup()
turtle.pensize(4)

turtle.goto(0, 0)
turtle.pendown()
turtle.pencolor("red")
# Sin wave
for x in range(500):
    y = math.sin(math.radians(x))
    turtle.goto(x, y)

turtle.penup()

turtle.goto(0, 0)
turtle.pendown()
turtle.pencolor("blue")
# Cos wave
for x in range(3600):
    y = math.cos(math.radians(x))
    turtle.goto(x, y)

