'''
(Financial application: compute future tuition) Suppose that the tuition for a university is $10,000 this year and increases 5% every year.
Write a program that computes the tuition in ten years and the total cost of four years’ worth of tuition starting ten years from now.
'''
import random

currentTuitionFees = 10000

tuitionFeesInTenYears = currentTuitionFees
for _ in range(0, 10):
    tuitionFeesInTenYears += (0.05 * tuitionFeesInTenYears)

print('Tuition fees in ten years is', round(tuitionFeesInTenYears, 2))


totalTuitionFeesForFourYears = 0
for _ in range(0, 4):
    totalTuitionFeesForFourYears += ((totalTuitionFeesForFourYears * 0.05) + tuitionFeesInTenYears)

print('Total cost of four years’ worth of tuition starting ten years from now is', round(totalTuitionFeesForFourYears, 2))

