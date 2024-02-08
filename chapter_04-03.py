'''
(Algebra: solve linear equations) You can use Cramer’s rule to solve the
following system of linear equation:
Write a program that prompts the user to enter a, b, c, d, e, and f and display the
result. If ad – bc is 0, report that The equation has no solution

Enter a, b, c, d, e, f: 9.0, 4.0, 3.0, -5.0, -6.0, -21.0
x is -2.0 and y is 3.0
'''

a, b, c, d, e, f = eval(input('Enter a, b, c, d, e, f: '))

x = (e * d - b * f) / (a * d - b * c)
y = (a * f - e * c) / (a * d - b * c)

print('x is', x, 'and y is', y)