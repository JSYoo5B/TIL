#!/usr/bin/env python3
""" Use permutations in python
Use internal API
"""

from itertools import permutations

REQUEST = 1000000

if __name__ == '__main__':
    elements = [x for x in range(0,9+1)]
    permutes = permutations(elements, len(elements))
    answer = list(permutes)[REQUEST-1]
    print(answer)
