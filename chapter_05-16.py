'''
(Compute the greatest common divisor) For Listing 5.8, another solution to find
the greatest common divisor of two integers n1 and n2 is as follows: First find d to
be the minimum of n1 and n2, and then check whether d, d - 1, d - 2, ..., 2, or
1 is a divisor for both n1 and n2 in this order. The first such common divisor is the
greatest common divisor for n1 and n2.
'''

n1, n2 = eval(input('Enter n1 and n2: '))

min = n1 if n1 < n2 else n2

while(min > 0):
    if n1 % min == 0 and n2 % min == 0:
        print("GCD is", min)
        break;
    else:
        min -= 1



