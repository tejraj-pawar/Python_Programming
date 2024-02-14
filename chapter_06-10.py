'''
(Use the isPrime Function) Listing 6.7, PrimeNumberFunction.py, provides the
isPrime(number) function for testing whether a number is prime. Use this
function to find the number of prime numbers less than 10,000.
'''

def isPrime(num):
    for i in range(num//2, 1, -1):
        if num % i == 0:
            return False
    return True


for i in range(2, 10001):
    if isPrime(i):
        print(i)