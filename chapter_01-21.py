'''
(Turtle: display a clock) Write a program that displays a clock to show the time 9:15:00
'''

import turtle

turtle.showturtle()

turtle.circle(100)

turtle.penup()
turtle.goto(0,100)
turtle.pendown()

turtle.forward(90)
turtle.write(3)
turtle.backward(180)
turtle.write(9)

turtle.goto(0,100)
turtle.right(90)
turtle.penup()
turtle.forward(100)
turtle.write(6)
turtle.backward(180)
turtle.write(12)

turtle.hideturtle()

turtle.done()