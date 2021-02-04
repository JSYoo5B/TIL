#!/usr/bin/env python3
""" Brute-force solution
1. Loop from 2 to 10000
2. Get the divisors
3. Check if the number is Amicable
"""

from math import ceil, sqrt

def get_divisors(num):
    divisors = [1]
    for i in range(2, ceil(sqrt(num))):
        if num % i == 0:
            divisors.append(i)
            # Add pair divisor whether the num isn't square of number
            if num != i * i:
                divisors.append(int(num / i))
    return divisors

REQUEST = 10000

if __name__ == '__main__':
    amicables = []
    numbers = [None] * (REQUEST + 1)
    for i in range(2, REQUEST + 1):
        # Skip if d(n) were calculated
        if numbers[i] != None:
            continue
        # Calculate d(i) and d(d(i))
        d_i = sum(get_divisors(i))
        d_d_i = sum(get_divisors(d_i))
        # Save d(i) and d(d(i))
        numbers[i] = d_i
        if d_i < REQUEST:
            numbers[d_i] = d_d_i
        # Amicable numbers are pair of different numbers
        if d_i != i and i == d_d_i:
            amicables.append(i)
            if d_i < REQUEST:
                amicables.append(d_i)
    answer = sum(amicables)
    print(answer)
