#!/usr/bin/env python3
""" Sieve of Eratosthenes
1.  Get all prime numbers which is less than given number by the Sieve
    of Eratosthenes algorithm. (Loop till the sqrt of given number)
2.  Search the complete divisor from the prime numbers in descending order.
"""
from math import sqrt

REQUEST = 600851475143

def SieveOfEratosthenes(number):
    primes = [x for x in range(2, number)]
    
    for factor in range(2, int(sqrt(number))):
        primes = [p for p in primes if p == factor or p % factor != 0]
    
    return primes

if __name__ == '__main__':
    # Supposes that Prime factor may not exceed sqrt of given number
    primes = SieveOfEratosthenes(int(sqrt(REQUEST)))
    max_factor = 0
    
    factors = [f for f in primes if REQUEST % f == 0]

    print(max(factors))
