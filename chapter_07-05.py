'''
(Geometry: n-sided regular polygon)
'''

from math import tan

class RegularPolygon:

    def __init__(self, n = 3, side = 1, x = 0, y = 0):
        self.n = n
        self.side = side
        self.x = x
        self.y = y

    def getN(self):
        return self.n

    def getSide(self):
        return self.side

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getPerimeter(self):
        return self.side * self.n

    def getArea(self):
        return (self.n * self.side * self.side) / (4 * (tan(3.14/self.n)))


p1 = RegularPolygon()
p2 = RegularPolygon(6, 4)
p3 = RegularPolygon(10, 4, 5.6, 7.8)

print(p1.getPerimeter(), p1.getArea())
print(p2.getPerimeter(), p2.getArea())
print(p3.getPerimeter(), p3.getArea())