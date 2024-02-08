'''
 Write a program that prompts the user to enter an integer for
today’s day of the week (Sunday is 0, Monday is 1, ..., and Saturday is 6). Also
prompt the user to enter the number of days after today for a future day and display the future day of the week. Here is a sample run:

Enter today's day: 1
Enter the number of days elapsed since today: 3
Today is Monday and the future day is Thursday
'''

todayDay = eval(input('Enter today\'s day: '))
noOfDaysElapsed = eval(input('Enter the number of days elapsed since today: '))

futureDay = (todayDay + noOfDaysElapsed) % 7;
print('Future Day is', futureDay)

if futureDay == 0:
    print('Sunday')
elif futureDay == 1:
    print('Monday')
elif futureDay == 2:
    print('Tuesday')
elif futureDay == 3:
    print('Wednesday')
elif futureDay == 4:
    print('Thursday')
elif futureDay == 5:
    print('Friday')
elif futureDay == 6:
    print('Saturday')