'''
Write a program to draw a chessboard
'''

import turtle

win = turtle.Screen()

boardSize = 8
win.setworldcoordinates(0, 0, boardSize, boardSize)

def drawSquare():
    for _ in range(4):
        turtle.forward(1)
        turtle.left(90)
    turtle.forward(1)

for i in range(0, boardSize):
    color = ''
    for j in range(0, boardSize):
        if (i + j) % 2 == 0:
            color = 'black'
        else:
            color = 'white'

        turtle.begin_fill()
        drawSquare()
        turtle.fillcolor(color)
        turtle.end_fill()

    turtle.penup()
    turtle.goto(0, i)
    turtle.pendown()

turtle.done()



