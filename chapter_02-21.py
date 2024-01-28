'''
(Financial application: compound value) Suppose you save $100 each month into
a savings account with an annual interest rate of 5%. Therefore, the monthly interest rate is After the first month,
the value in the account becomes
100 * (1 + 0.00417) = 100.417
After the second month, the value in the account becomes
(100 + 100.417) * (1 + 0.00417) = 201.252
After the third month, the value in the account becomes
(100 + 201.252) * (1 + 0.00417) = 302.507
and so on.
Write a program that prompts the user to enter a monthly saving amount and
displays the account value after the sixth month.

Here is a sample run of the program:
Enter the monthly saving amount: 100
After the sixth month, the account value is 608.81
'''

monthlySavingAmount = eval(input("Enter the monthly saving amount: "))

total = 0.0
monthlyInterestRate = 1.00417

for x in range(0,6):
    total = (total + monthlySavingAmount) * monthlyInterestRate

print("After the sixth month, the account value is", str(round(total,2)))