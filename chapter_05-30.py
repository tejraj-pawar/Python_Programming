'''
(Display the first days of each month) Write a program that prompts the user
to enter the year and first day of the year, and displays the first day of each month
in the year on the console. For example, if the user entered year 2013, and 2 for
Tuesday, January 1, 2013, your program should display the following output:
January 1, 2013 is Tuesday
...
December 1, 2013 is Sunday
'''

year,firstDay = eval(input('Enter year, first day of that year: '))

daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthsInYear = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
dayOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
year = int(year)

print('{} 1, {} is {}'.format(monthsInYear[0], year, dayOfWeek[firstDay]))

# for leap year
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    daysInMonth[1] = 29

totalDaysElapsed = 0

for i in range(1, 12):
    totalDaysElapsed += (daysInMonth[i-1])
    firstDayOfMonth = (firstDay + totalDaysElapsed) % 7
    print('{} 1, {} is {}'.format(monthsInYear[i], year, dayOfWeek[firstDayOfMonth]))










