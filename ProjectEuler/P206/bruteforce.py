#!/usr/bin/env python3
""" Brute-force solution
1_2_3_4_5_6_7_8_9_0 means this squared number has factor 10.
it means end of this square number will be 900
(must be squared, need 100 as factor)
Square of 30 and 70 will make its end with 900 (30*30 == 900, 70*70 == 900)
(This is evident for python and other environment which supports big integer)
"""

from math import sqrt

def is_concealed_square(num):
    num_digits = [int(d) for d in str(num)]
    # Check every fixed position
    for i in range(0, len(num_digits)-1, 2):
        if num_digits[i] != int(i/2) + 1:
            return False
    if num_digits[-1] == 0:
        return True
    return False

if __name__ == '__main__':
    MIN = 1020304050607080900
    MAX = 1929394959697989900

    min_sqrt = int(sqrt(MIN) / 100) * 100
    max_sqrt = int(sqrt(MAX) / 100) * 100

    for i in range(min_sqrt, max_sqrt, 100):
        num = i + 30
        if is_concealed_square(num ** 2):
            break
        num = i + 70
        if is_concealed_square(num ** 2):
            break

    print(num)
