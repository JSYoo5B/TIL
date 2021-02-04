#!/usr/bin/env python3
""" Brute-force solution
1. do loop from 1 to 1000
2. check if current number is multiples of 3 or 5
3. accumulate sum
expected time complexity = O(n)
"""

from functools import reduce

REQUEST = 1000

if __name__ == '__main__':
    numbers = list(range(1, REQUEST))
    multiples = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, numbers))
    answer = reduce(lambda x, y: x + y, multiples)

    print(answer)

