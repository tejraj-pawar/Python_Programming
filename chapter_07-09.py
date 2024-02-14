'''
(Geometry: intersection)

Enter the endpoints of the first line segment: 2.0, 2.0, 0, 0
Enter the endpoints of the second line segment: 0, 2.0, 2.0, 0
The intersecting point is: (1.0, 1.0)
'''

class Coordinate:
	def __init__(self, x, y):
		self.x = x
		self.y = y


def findIntersectionPoint(A, B, C, D):
	a1 = B.y - A.y
	b1 = A.x - B.x
	c1 = a1 * (A.x) + b1 * (A.y)

	a2 = D.y - C.y
	b2 = C.x - D.x
	c2 = a2 * (C.x) + b2 * (C.y)

	determinant = a1 * b2 - a2 * b1

	if (determinant == 0): # lines are parallel
		return Coordinate(10 ** 9, 10 ** 9)
	else:
		x = (b2 * c1 - b1 * c2) / determinant
		y = (a1 * c2 - a2 * c1)/ determinant
		return Coordinate(x, y)

x1, y1, x2, y2 = eval(input('Enter the endpoints of the first line segment: '))
x3, y3, x4, y4 = eval(input('Enter the endpoints of the second line segment: '))

A = Coordinate(x1, y1)
B = Coordinate(x2, y2)
C = Coordinate(x3, y3)
D = Coordinate(x4, y4)

intersection = findIntersectionPoint(A, B, C, D)

if (intersection.x == 10 ** 9 and intersection.y == 10 ** 9):
	print("The given lines are parallel.")
else:
	print("The intersection of the given lines is: ", intersection.x, intersection.y)





