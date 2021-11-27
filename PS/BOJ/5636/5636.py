#!/usr/bin/env python3

from math import sqrt

import sys
input = sys.stdin.readline

def SieveOfEratosthenes(number):
    primes = [i for i in range(0, number)]

    primes[0] = 0
    primes[1] = 0
    prev = 2
    for factor in range(2, int(sqrt(number))):
        if primes[factor] == 0: # 0 means the number isn't prime number
            continue
        non_prime = factor * prev
        while non_prime < number:
            primes[non_prime] = 0
            non_prime += factor
        prev = factor
    
    primes = [p for p in primes if p != 0]
    return primes

if __name__ == '__main__':
    primes = SieveOfEratosthenes(100000)
    while True:
        num_str = input().rstrip()
        if int(num_str) == 0:
            break

        avail_nums = set()
        for l in range(min(5, len(num_str))):
            avail_nums.update([ int(num_str[i:i+l+1]) for i in range(len(num_str)-l) ])
        substr_primes = [ n for n in avail_nums if n in primes ]
        print(max(substr_primes))
