#!/usr/bin/env python3
""" Power of prime numbers
The smallest positive number that is evenly divisible by all of the number
from 1 to 20 means the Least Common Multiplier of all the number from 1 to 20
Obviously, the LCM will use all the prime numbers between the given numbers.
Now let's check 4, 8 and 16 which are the power numbers of 2, the prime number.
Multiplication of only the prime numbers cannot evenly divisible those numbers.
The 16, greatest power number in the number range, is evenly divisible of all
other power numbers of 2.
1. Find all prime numbers form 1 to 20
2. For each prime numbers, power itself until it is the largest number which
   doesn't exceed the 20
3. Multiply all the powered prime numbers
"""
from math import sqrt

REQUEST = 20

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
    primes = SieveOfEratosthenes(REQUEST)
    lcm = 1

    for prime in primes:
        factor = prime
        while (factor * prime) < REQUEST:
            factor *= prime
        lcm *= factor

    print(lcm)
