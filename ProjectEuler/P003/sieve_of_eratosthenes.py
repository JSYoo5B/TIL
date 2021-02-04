#!/usr/bin/env python3
""" Sieve of Eratosthenes
1.  Get all prime numbers which is less than given number by the Sieve
    of Eratosthenes algorithm. (Loop till the sqrt of given number)
2.  Search the complete divisor from the prime numbers in descending order.
"""
from math import sqrt

REQUEST = 600851475143

def SieveOfEratosthenes(number):
    primes = [i for i in range(0, number)]

    primes[0] = 0
    primes[1] = 0
    for factor in range(2, int(sqrt(number))):
        if primes[factor] == 0: # 0 means the number isn't prime number
            continue
        non_prime = factor * 2
        while non_prime < number:
            primes[non_prime] = 0
            non_prime += factor
    
    primes = [p for p in primes if p != 0]
    return primes

if __name__ == '__main__':
    # Supposes that Prime factor may not exceed sqrt of given number
    primes = SieveOfEratosthenes(int(sqrt(REQUEST)))
    factors = []

    for p in primes:
        if REQUEST % p == 0:
            factors.append(p)

    max_factor = max(factors)
    print(max_factor)
