'''
(Guess the capitals) Rewrite Exercise 11.40 using a dictionary to store the pairs
of states and capitals so that the questions are randomly displayed.
What is the capital of Alabama?
The correct answer should be Montgomery
What is the capital of Alaska?
Your answer is correct
What is the capital of Arizona? ...
...
The correct count is 35
'''

stateDict = {'Texas':'Austin', 'Georgia':'Atlanta', 'Ohio':'Columbus'}

score = 0
for entry in stateDict.items():
    ans = input('What is the capital of {}? '.format(entry[0]))
    if ans == entry[1]:
        print('Your answer is correct')
        score += 1
    else:
        print('The correct answer should be {}'.format(entry[1]))

print('The correct count is {}'.format(score))