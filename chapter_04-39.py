'''
(Turtle: two circles)
Write a program that prompts the user to enter the center
coordinates and radii of two circles and determines whether the second circle is
inside the first or overlaps with the first
'''
import turtle

x1, y1, r1 = eval(input('Enter circle1\'s center x-, y-coordinates, and radius: '))
x2, y2, r2 = eval(input('Enter circle2\'s center x-, y-coordinates, and radius: '))

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(distance)

if distance <= abs(r1 - r2):
    print('circle2 is inside circle1')
elif distance <= r1 + r2:
    print('circle2 overlaps circle1')
elif distance > r1 + r2:
    print('circle2 does not overlap circle1')

turtle.penup()
turtle.goto(x1, y1 - r1)
turtle.pendown()
turtle.circle(r1)
turtle.write('Circle 1')

turtle.penup()
turtle.goto(x2, y2 - r2)
turtle.pendown()
turtle.circle(r2)
turtle.write('Circle 2')

turtle.hideturtle()

turtle.done()