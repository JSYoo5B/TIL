#!/usr/bin/env python3
""" Sieve of Eratosthenes
1.  Get all prime numbers which is less than given number by the Sieve
    of Eratosthenes algorithm. (Loop till the sqrt of given number)
2.  Search the complete divisor from the prime numbers in descending order.
"""
from math import sqrt

REQUEST = 600851475143

def SieveOfEratosthenes(number):
    primes = []

    for i in range(0, number):
        primes.append(i)

    primes[0] = 0
    primes[1] = 0
    for factor in range(2, int(sqrt(number))):
        if primes[factor] == 0: # 0 means the number isn't prime number
            continue
        non_prime = factor * 2
        while non_prime < number:
            primes[non_prime] = 0
            non_prime += factor
    
    try:
        while True:
            primes.remove(0)
    except ValueError:
        return primes

if __name__ == '__main__':
    # Supposes that Prime factor may not exceed sqrt of given number
    primes = SieveOfEratosthenes(int(sqrt(REQUEST)))
    max_factor = 0

    for i in range(len(primes),0):
        if REQUEST % primes[i] == 0:
            max_factor = primes[i]
            break

    print(max_factor)
