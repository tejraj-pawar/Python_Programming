'''
(Sort three numbers) Write the following function to display three numbers in
increasing order:
def displaySortedNumbers(num1, num2, num3):
Write a test program that prompts the user to enter three numbers and invokes the
function to display them in increasing order. Here are some sample runs:
Enter three numbers: 3,2.4,5
The sorted numbers are 2.4,3,5
'''

def displaySortedNumbers(num1, num2, num3):
    if num2 < num1 and num2 < num3:
        num1,num2 = num2,num1
    elif num3 < num1 and num3 < num2:
        num1,num3 = num3,num1
    
    if(num2 > num3):
        num2,num3 = num3,num2
    
    print(num1, num2, num3)


num1, num2, num3 = eval(input('Enter three numbers: '))
displaySortedNumbers(num1, num2, num3)
