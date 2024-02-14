'''
(Turtle: draw points, rectangles, and circles) Use the functions defined in Listing
6.14 to write a program that displays a rectangle centered at (-75, 0) with width
and height 100 and a circle centered at (50, 0) with radius 50. Fill 10 random
points inside the rectangle and 10 inside the circle
'''
import random
import turtle

#draw rectangle
turtle.penup()
turtle.goto(-25, 50)
turtle.pendown()

turtle.goto(-25, -50)
turtle.goto(-125, -50)
turtle.goto(-125, 50)
turtle.goto(-25, 50)

for i in range(0, 10):
    x = random.randint(-125, -25)
    y = random.randint(-50, 50)
    turtle.penup()
    turtle.goto(x, y)
    turtle.begin_fill()
    turtle.circle(2)
    turtle.color('black')
    turtle.end_fill()

#draw circle
turtle.penup()
turtle.goto(50, -50)
turtle.pendown()

turtle.circle(50)

for i in range(0, 10):
    x = random.randint(25, 75)
    y = random.randint(-25, 25)
    turtle.penup()
    turtle.goto(x, y)
    turtle.begin_fill()
    turtle.circle(2)
    turtle.color('black')
    turtle.end_fill()

turtle.done()



