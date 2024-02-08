'''
(Turtle: draw a line) Write a program that prompts the user to enter two points
and draw a line to connect the points and displays the coordinates of the points,
'''

import turtle

x1, y1, x2, y2 = eval(input("Enter x1, y1, x2, y2 co-ordinates for line: "))


turtle.showturtle()
turtle.penup()
turtle.goto(x1, y1)
turtle.write(turtle.pos())
turtle.pendown()
turtle.goto(x2, y2)
turtle.write(turtle.pos())
turtle.hideturtle()

turtle.done()