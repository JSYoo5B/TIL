#!/usr/bin/env python3
""" Brute-force solution
Evident
(This is evident for python and other environment which supports big integer)
"""

from math import pow

REQUEST = 1000

if __name__ == '__main__':
    number = int(pow(2, REQUEST))
    digits = str(number)
    digits = [int(i) for i in digits]
    answer = sum(digits)
    print(answer)
