'''
(Implement Stack using inheritance) In Listing 12.13, the Stack class is
implemented using composition. Define a new Stack class using inheritance that extends list.
Draw UML diagrams of the new class. Implement it. Write a test program that
prompts the user to enter five strings and displays them in reverse order.
'''


class List:
    def __init__(self, list = []):
        self.__list = list

    def getList(self):
        return self.__list

    def addFirst(self, item):
        self.__list.append(item)

    def removeLast(self):
        return self.__list.pop()


class Stack:

    def __init__(self):
        self.stack = List()


stack = List()
nums = [int(num) for num in input('Enter 5 random numbers: ').split()]

for num in nums:
    stack.addFirst(num)

for _ in range(0, len(stack.getList())):
    print(stack.removeLast(), end=' ')
