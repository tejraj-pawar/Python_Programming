'''
The Rational Class: Throw RunTimeError Exception if denominator is 0.
'''

class Rational:
    def __init__(self, numerator=1, denominator=0):
        if denominator == 0:
            raise RuntimeError('Denominator can not be zero')
        divisor = gcd(numerator, denominator)
        self.__numerator = (1 if denominator > 0 else -1) * int(numerator / divisor)
        self.__denominator = int(abs(denominator) / divisor)

def gcd(n, d):
    n1 = abs(n)
    n2 = abs(d)
    gcd = 1

    k = 1
    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k
        k += 1
    return gcd

Rational()