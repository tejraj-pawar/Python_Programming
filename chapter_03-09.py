'''
(Financial application: payroll) Write a program that reads the following information and prints a payroll statement:
Employee’s name (e.g., Smith)
Number of hours worked in a week (e.g., 10)
Hourly pay rate (e.g., 9.75)
Federal tax withholding rate (e.g., 20%)
State tax withholding rate (e.g., 9%)

Enter employee's name:
Enter number of hours worked in a week:
Enter hourly pay rate:
Enter federal tax withholding rate:
Enter state tax withholding rate:

Employee Name: Smith
Hours Worked: 10.0
Pay Rate: $9.75
Gross Pay: $97.5
Gross Pay:
    Federal Withholding (20.0%): $19.5
    State Withholding (9.0%): $8.77
    Total Deduction: $28.27
Net Pay: $69.22

'''

name = input("Enter employee's name: ")
hoursPerWeek = eval(input("Enter number of hours worked in a week: "))
payPerHour = eval(input("Enter hourly pay rate: "))
federalTaxRate = eval(input("Enter federal tax withholding rate: "))
stateTaxRate = eval(input("Enter state tax withholding rate: "))

grossPay = hoursPerWeek * payPerHour
federalTaxDeducted = federalTaxRate * grossPay
stateTaxDeducted = stateTaxRate * grossPay
totalDeduction = federalTaxDeducted + stateTaxDeducted

print("Employee Name:", name)
print("Hours Worked:", hoursPerWeek)
print("Pay Rate:", payPerHour)
print("Gross Pay:", grossPay)
print("Gross Pay:")
print("\t  Federal Withholding:", federalTaxDeducted)
print("\t State Withholding:", stateTaxDeducted)
print("\t Total Deduction:", totalDeduction)
print("Net Pay:", grossPay - totalDeduction)
