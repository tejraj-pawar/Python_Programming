'''
(Geometry: two circles) Write a program that prompts the user to enter the center
coordinates and radii of two circles and determines whether the second circle is
inside the first or overlaps with the first, as shown in Figure 4.11. (Hint: circle2 is
inside circle1 if the distance between the two centers <= | r1 - r2| and circle2
overlaps circle1 if the distance between the two centers <= r1 + r2. Test your
program to cover all cases.)
Enter circle1's center x-, y-coordinates, and radius: 0.5, 5.1, 13
Enter circle2's center x-, y-coordinates, and radius: 1, 1.7, 4.5
circle2 is inside circle1
'''

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