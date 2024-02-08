'''
 Zeller’s congruence is an algorithm developed by Christian Zeller to calculate the day of the week. The formula is where
■ h is the day of the week (0: Saturday, 1: Sunday, 2: Monday, 3: Tuesday,
4: Wednesday, 5: Thursday, 6: Friday).
■ q is the day of the month.
■ m is the month (3: March, 4: April, ..., 12: December). January and February are
counted as months 13 and 14 of the previous year.
■ j is the century (i.e., ). (year/100)
■ k is the year of the century (i.e., year % 100).
Write a program that prompts the user to enter a year, month, and day of the
month, and then it displays the name of the day of the week. Here are some sample runs:

Enter year: (e.g., 2008): 2013
Enter month: 1-12: 1
Enter the day of the month: 1-31: 25
Day of the week is Friday
'''

year = eval(input('Enter year: '))
month = eval(input('Enter month: '))
dayOfMonth = eval(input('Enter the day of the month: '))

j = year / 100
k = year % 100

dayOfWeek = int( dayOfMonth + (26 * (month + 1) / 10) + k + (k / 4) + (j / 4) + (5 * j) ) % 7

print('Day of the week is ', end='')
if dayOfWeek == 0:
    print('Saturday')
elif dayOfWeek == 1:
    print('Sunday')
elif dayOfWeek == 2:
    print('Monday')
elif dayOfWeek == 3:
    print('Tuesday')
elif dayOfWeek == 4:
    print('Wednesday')
elif dayOfWeek == 5:
    print('Thursday')
elif dayOfWeek == 6:
    print('Friday')
