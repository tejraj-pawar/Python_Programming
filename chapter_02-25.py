'''
Write a program that prompts the user to enter the
center of a rectangle, width, and height, and displays the rectangle
'''

import turtle

x,y = eval(input("Enter the center x,y co-ordinates of the rectangle: "))
width, height = eval(input("Enter width, height: "))

turtle.showturtle()

turtle.penup()
turtle.goto(x-width/2,y-height/2)
turtle.pendown()
turtle.goto(x-width/2,y+height/2)
turtle.goto(x+width/2,y+height/2)
turtle.goto(x+width/2,y-height/2)
turtle.goto(x-width/2, y-height/2)
turtle.hideturtle()

turtle.done()