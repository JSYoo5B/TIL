#!/usr/bin/env python3
""" Sieve of Eratosthenes
1.  Get all prime numbers which is less than given number by the Sieve
    of Eratosthenes algorithm. (Loop till the sqrt of given number)
2.  Search the complete divisor from the prime numbers in descending order.
"""
from math import sqrt

REQUEST = 10001
LIMIT = 1000000

def SieveOfEratosthenes(number):
    primes = [x for x in range(2, number)]
    
    for factor in range(2, int(sqrt(number))):

        primes = list(filter(lambda x: x == factor or x % factor != 0, primes))
    
    return primes

if __name__ == '__main__':
    # Supposes that Prime factor may not exceed sqrt of given number
    primes = SieveOfEratosthenes(LIMIT)
    
    if len(primes) >= REQUEST:
        print(primes[REQUEST - 1])

