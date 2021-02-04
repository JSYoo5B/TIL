#!/usr/bin/env python3
""" Prime factor check in functional approach
1. As the definition of Prime number, check if given number
   is completely divisible by other lower prime number
2. For functional programming, make function to be iteratable
3. For performance, need to filter factor candidates
"""

REQUEST = 10001

def getFactorCandidates(num, primes):
    for x in primes:
        if x ** 2 < num:
            yield x
        else:
            return

def getPrimeNumber():
    primes = [2, 3]
    factor = 5

    yield 2
    yield 3
    while True:
        isPrime = True
        for x in getFactorCandidates(factor, primes):
            if factor % x == 0:
                isPrime = False
                break;
        if isPrime == True:
            primes.append(factor)
            yield factor
        factor += 2

if __name__ == '__main__':
    primes = []

    for x in getPrimeNumber():
        primes.append(x)
        if len(primes) == REQUEST:
            break

    print(primes[-1])

