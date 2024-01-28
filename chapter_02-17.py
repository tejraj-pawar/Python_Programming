'''
(Health application: compute BMI) Body mass index (BMI) is a measure of health
based on weight. It can be calculated by taking your weight in kilograms and
dividing it by the square of your height in meters. Write a program that prompts
the user to enter a weight in pounds and height in inches and displays the BMI.
Note that one pound is 0.45359237 kilograms and one inch is 0.0254 meters.

Here is a sample run:
Enter weight in pounds: 95.5
Enter height in inches: 50
BMI is 26.8573
'''

weightInPounds = eval(input("Enter weight in pounds: "))
heightInInches = eval(input("Enter height in inches: "))

weightInKgs = round((weightInPounds * 0.45359237), 2)
heightInMeter = round((heightInInches * 0.0254), 2)

bmi = weightInKgs / (heightInMeter ** 2)

print("BMI is", round(bmi,4))