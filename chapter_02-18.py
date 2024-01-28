'''
(Current time) Listing 2.7, ShowCurrentTime.py, gives a program that displays the
current time in GMT. Revise the program so that it prompts the user to enter the
time zone in hours away from (offset to) GMT and displays the time in the specified time zone.

Here is a sample run:
Enter the time zone offset to GMT: -5
The current time is 4:50:34
'''
import time

zoneOffset = eval(input("Enter the time zone offset to GMT: "))

todaysTimeInSeconds = time.time() % (60 * 60 * 24)

zoneOffsetTimeInSeconds = todaysTimeInSeconds + (zoneOffset * 60 * 60)

hours = zoneOffsetTimeInSeconds // (60 * 60);
minutes = (zoneOffsetTimeInSeconds % (60 * 60)) // 60;
seconds = (zoneOffsetTimeInSeconds % (60 * 60)) % 60;

print("The current time is: " + str(int(hours % 24)) + ":" + str(int(minutes)) + ":" + str(int(seconds)))
