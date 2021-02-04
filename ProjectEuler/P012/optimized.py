#!/usr/bin/env python3
""" Optimized solution
For single dividend, each divisor has its pair divisor to make dividend.
If given dividend is square of natural number, its pair divisor is itself.
But the formula of triangular number is n * (n + 1) / 2,
which cannot be the square of natural number (ignoring evident case 1)
So, calculating the count of divisor can be optimized by following:
1. for given number, find divisor till the square root of given number.
2. divisors till sqrt of given number * 2 is the total count of given number.
"""

REQUEST=500

from math import sqrt, ceil

def get_triangular_number(num):
    return int(num * (num + 1) / 2)

def get_divisor_count(num):
    if num == 1:
        return 1

    divisor_count = 0
    for i in range(1, ceil(sqrt(num)), 1):
        if (num % i) == 0:
            divisor_count += 1

    return divisor_count * 2

if __name__ == '__main__':
    triangular_num = 0
    divisor_cnt = 0
    nth = 1
    while divisor_cnt < REQUEST:
        triangular_num = get_triangular_number(nth)
        divisor_cnt = get_divisor_count(triangular_num)
        nth += 1

    print(triangular_num)
