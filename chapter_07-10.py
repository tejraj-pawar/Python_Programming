'''
The Time Class

Enter the elapsed time: 55550505
The hour:minute:second for the elapsed time is 22:41:45
'''

class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def getHour(self):
        return self.__hour

    def getMinute(self):
        return self.__minute

    def getSecond(self):
        return self.__second

    def setTime(self, seconds):
        seconds = seconds % (24 * 3600) # removed days
        self.__hour = seconds // (60 * 60)
        self.__minute = (seconds % (60 * 60)) // 60
        self.__second = (seconds % (60 * 60)) % 60


seconds = eval(input('Enter the elapsed time: '))
t = Time(12, 41, 6)
t.setTime(seconds)

print(str(t.getHour()) + ':' + str(t.getMinute()) + ':' + str(t.getSecond()))

