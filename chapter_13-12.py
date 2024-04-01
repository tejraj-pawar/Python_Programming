'''
The TriangularError.class
'''

class TriangularError(RuntimeError):
    def __init__(self, side1, side2, side3):
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def __str__(self):
        return 'Three given sides({}, {}, {}) cannot form a triangle'.format(self.__side1, self.__side2, self.__side3)

class GeometricObject:
    def __init__(self, color, isFilled):
        self.__color = color
        self.__isFilled = isFilled

    def getColor(self):
        return self.__color

    def isFilled(self):
        return self.__isFilled

class Triangle(GeometricObject):

    def __init__(self, color, isFilled, side1=1.0, side2=1.0, side3=1.0):
        super().__init__(color, isFilled)
        if not (side1 + side2) > side3 and (side2 + side3) > side1 and (side1 + side3) > side2:
            raise TriangularError(side1, side2, side3)
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def getSide1(self):
        return self.__side1

    def getSide2(self):
        return self.__side2

    def getSide3(self):
        return self.__side3

    def getArea(self):
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        return (s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3)) ** 0.5

    def getPerimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def __str__(self):
        return "Triangle: side1 = " + str(self.__side1) + " side2 = " + str(self.__side2) + " side3 = " + str(
            self.__side3)

t = Triangle('red', True, 5, 7, 10)

