'''
(String permutation) Write a recursive function to print all the permutations of a
string. For example, for the string abc, the printout is:
abc acb bac bca cab cba
(Hint: Define the following two functions. The second function is a helper function.
def displayPermutation(s):
def displayPermutationHelper(s1, s2):
The first function simply invokes displayPermutation(" ", s). The second
function uses a loop to move a character from s2 to s1 and recursively invokes
it with a new s1 and s2. The base case is that s2 is empty and prints s1 to the console.)
Write a test program that prompts the user to enter a string and displays all its permutations
'''

def displayPermutation(s):
    displayPermutationHelper('', s)

def displayPermutationHelper(s1, s2):
    if len(s2) == 0:
        print(s1)
    for i in range(0, len(s2)):
        newS1 = s1 + s2[i]
        newS2 = s2[0:i] + s2[i + 1:]
        displayPermutationHelper(newS1, newS2)

displayPermutation('abc')



