'''
(Turtle: plot the square function) Write a program that draws a diagram for the
function (see Figure 5.6a). f(x) = x^2
'''
import turtle
import turtle as t

t.penup()
t.goto(0, -100)
t.pendown()
t.goto(0, 100)

t.penup()
t.goto(-100, 0)
t.pendown()
t.goto(100, 0)

t.penup()
t.goto(-100, 100)
t.pendown()

for x in range(-100, 100):
    y = (x ** 2) / 100
    turtle.goto(x, y)

t.done()

