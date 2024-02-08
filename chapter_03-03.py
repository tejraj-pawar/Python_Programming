'''
(Geography: estimate areas) Find the GPS locations for Atlanta, Georgia;
Orlando, Florida; Savannah, Georgia; and Charlotte, North Carolina from
www.gps-data-team.com/map/ and compute the estimated area enclosed by these
four cities. (Hint: Use the formula in Programming Exercise 3.2 to compute the
distance between two cities. Divide the polygon into two triangles and use the
formula in Programming Exercise 2.14 to compute the area of a triangle.)

1] atlanta: -77.0185713 , 38.9583078
2] orlando: -82.7003776 , 27.8343204
3] Savannah: -81.1746 , 31.9821
4] NC: -0.1057326 , 51.4961002

1st Triangle: 1 > 3 > 4
2nd Triangle: 2 > 3 > 4
'''

from math import sin, cos, acos, radians


def calculateTriangleArea(x1, y1, x2, y2, x3, y3):
    side1 = 6371.01 * acos(sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos(y1 - y2))
    side2 = 6371.01 * acos(sin(x2) * sin(x3) + cos(x2) * cos(x3) * cos(y2 - y3))
    side3 = 6371.01 * acos(sin(x3) * sin(x1) + cos(x3) * cos(x1) * cos(y3 - y1))

    s = (side1 + side2 + side3) / 2
    return round(((s * (s - side1) * (s - side2) * (s - side3)) ** 0.5), 2)


x1, y1 = radians(-77.0185713), radians(38.9583078)
x2, y2 = radians(-82.7003776), radians(27.8343204)
x3, y3 = radians(-81.1746), radians(31.9821)
x4, y4 = radians(-0.1057326), radians(51.4961002)

totalArea = (calculateTriangleArea(-77.0185713, 38.9583078, -81.1746, 31.9821, -0.1057326, 51.4961002) +
             calculateTriangleArea(-82.7003776, 27.8343204, -81.1746, 31.9821, -0.1057326, 51.4961002))

print("Total area covered by all four GPS locations is", totalArea)
