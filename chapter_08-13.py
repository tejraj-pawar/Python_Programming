'''
(Longest common prefix) Write a method that returns the longest common prefix
of two strings. For example, the longest common prefix of distance and
disinfection is dis. The header of the method is:
def prefix(s1, s2)
If the two strings have no common prefix, the method returns an empty string.
Write a main method that prompts the user to enter two strings and displays their
common prefix
'''

def prefix(s1, s2):
    l1 = l2 = 0
    r1 = len(s1)
    r2 = len(s2)
    commonPrefix = ''

    for i in range(0, len(s1)):
        if s1[i] == s2[i]:
            commonPrefix += s1[i]
        else:
            break

    return commonPrefix

print(prefix('distance', 'disinfection'))
