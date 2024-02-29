'''
(Simulation using Turtle: self-avoiding random walk)
'''
import turtle
import random

turtle.speed(100)

x = -80
for y in range(-80, 80 + 1, 10):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.goto(abs(x), y)

y = -80
for x in range(-80, 80 + 1, 10):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.goto(x, abs(y))

turtle.penup()
turtle.goto(0,0)
turtle.pensize(3)
turtle.color('blue')
turtle.pendown()

x = y = 0
traceTrack = []
traceDeadEnd = set()

while abs(x) < 80 and abs(y) < 80:
    if len(traceDeadEnd) == 4:
        print("It has reached a dead end!!")
        break

    walkDirection = random.randint(1, 4)
    if walkDirection == 1: # go right
        if [x+10,y] in traceTrack:
            traceDeadEnd.add('right')
            continue
        else:
            x += 10
            traceTrack.append([x, y])
            turtle.goto(x, y)
    elif walkDirection == 2: # go up
        if [x,y+10] in traceTrack:
            traceDeadEnd.add('up')
            continue
        else:
            y += 10
            traceTrack.append([x, y])
            turtle.goto(x, y)
    elif walkDirection == 3: # go left
        if [x - 10, y] in traceTrack:
            traceDeadEnd.add('left')
            continue
        else:
            x -= 10
            traceTrack.append([x, y])
            turtle.goto(x, y)
    elif walkDirection == 4: # go down
        if [x, y - 10] in traceTrack:
            traceDeadEnd.add('down')
            continue
        else:
            y -= 10
            traceTrack.append([x, y])
            turtle.goto(x, y)

turtle.done()