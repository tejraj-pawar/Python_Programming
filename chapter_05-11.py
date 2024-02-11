'''
(Find the two highest scores) Write a program that prompts the user to enter the
number of students and each student’s score, and displays the highest and second highest scores.
'''

noOfStudents = eval(input('Enter total number of students: '))

scores = []
max1 = 0
max2 = 0

for i in range(1, noOfStudents + 1):
    score = eval(input('Enter score for student ' + str(i) + ' : '))
    scores.append(score)
    if(score > max1):
        max2 = max1
        max1 = score
    if(score < max1 and score > max2):
        max2 = score

print('Highest Score:', str(max1), 'and Second Highest Score:', str(max2))

