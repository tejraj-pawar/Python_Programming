'''
(Population projection) Rewrite Exercise 1.11 to prompt the user to enter the
number of years and displays the population after that many years. Here is a
sample run of the program:
Enter the number of years: 5
The population in 5 years is 325932970
'''

years = eval(input("Enter the number of years: "))

currentPopulation = 312032486;
noOfSecondsInYear = 365 * 24 * 60 * 60;

for x in range(0, years):
    noOfBabiesBornInYear = noOfSecondsInYear // 7;
    noOfDeathsInYear = noOfSecondsInYear // 13;
    noOfImmigrantInYear = noOfSecondsInYear // 45;

    currentPopulation = currentPopulation + (noOfBabiesBornInYear + noOfImmigrantInYear - noOfDeathsInYear);

print("The population in", years, "years is", currentPopulation);