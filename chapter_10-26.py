'''
(Merge two sorted lists) Write the following function that merges two sorted lists
into a new sorted list:
def merge(list1, list2):
Enter list1: 1 5 16 61 111
Enter list2: 2 4 5 6
The merged list is 1 2 4 5 5 6 16 61 111
'''

def merge(list1, list2):

    len1 = len(list1)
    len2 = len(list2)
    result = []

    i = j = 0

    while i < len1 and j < len2:
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    result += list1[i:] + list2[j:]
    return result

    print(list1)


list1 = [int(x) for x in input('Enter list1: ').split(' ')]
list2 = [int(x) for x in input('Enter list2: ').split(' ')]

print('The merged list is', merge(list1, list2))


