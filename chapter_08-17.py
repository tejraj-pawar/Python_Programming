'''
(The Point class) Design a class named Point to represent a point with x- and y-coordinates. The class contains:
■ Two private data fields x and y that represent the coordinates with get methods.
■ A constructor that constructs a point with specified coordinates with default point (0, 0).
■ A method named distance that returns the distance from this point to another point of the Point type.
■ A method named isNearBy(p1) that returns true if point p1 is close to this
point. Two points are close if their distance is less than 5.
■ Implement the _ _str_ _ method to return a string in the form (x, y).
Draw the UML diagram for the class, and then implement the class. Write a test
program that prompts the user to enter two points, displays the distance between
them, and indicates whether they are near each other. Here are sample runs:

Enter two points x1, y1, x2, y2: 2.1, 2.3, 19.1, 19.2
The distance between the two points is 23.97
The two points are not near each other
'''


class Point:

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def distance(self, point):
        return (((point.__x - self.__x) ** 2) + ((point.__y - self.__y) ** 2)) ** 0.5

    def isNearBy(self, point):
        if self.distance(point) < 5:
            print('The two points are near each other')
        else:
            print('The two points are not near each other')

    def __str__(self):
        return '({},{})'.format(self.__x, self.__y)

x1, y1, x2, y2 = eval(input('Enter two points x1, y1, x2, y2: '))

p1 = Point(x1, y1)
p2 = Point(x2, y2)

distance = p1.distance(p2)
print('The distance between the two points is', round(distance, 2))
p1.isNearBy(p2)
