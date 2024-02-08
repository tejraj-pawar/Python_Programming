'''
(Turtle: draw shapes) Write a program that draws a triangle, square, pentagon,
hexagon, and octagon, as shown in Figure 3.6b. Note that the bottom edges of
these shapes are parallel to the x-axis. (Hint: For a triangle with a bottom line
parallel to the x-axis, set the turtle’s heading to 60 degrees.)
'''

import turtle
sideLength = 30

turtle.showturtle()
turtle.penup()
turtle.goto(-150, 40)
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.setheading(60)
turtle.circle(sideLength, steps=3)
turtle.end_fill()

turtle.showturtle()
turtle.penup()
turtle.goto(-90, 40)
turtle.pendown()
turtle.begin_fill()
turtle.color("orange")
turtle.setheading(45)
turtle.circle(sideLength, steps=4)
turtle.end_fill()

turtle.showturtle()
turtle.penup()
turtle.goto(-30, 40)
turtle.pendown()
turtle.begin_fill()
turtle.color("yellow")
turtle.setheading(36)
turtle.circle(sideLength, steps=5)
turtle.end_fill()

turtle.showturtle()
turtle.penup()
turtle.goto(30, 40)
turtle.pendown()
turtle.begin_fill()
turtle.color("violet")
turtle.setheading(30)
turtle.circle(sideLength, steps=6)
turtle.end_fill()

turtle.showturtle()
turtle.penup()
turtle.goto(90, 40)
turtle.pendown()
turtle.begin_fill()
turtle.color("blue")
turtle.setheading(22.5)
turtle.circle(sideLength, steps=8)
turtle.end_fill()

turtle.hideturtle()

turtle.done()