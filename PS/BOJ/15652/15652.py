#!/usr/bin/env python3

from itertools import combinations_with_replacement

if __name__ == '__main__':
    N, M = map(int, input().split())

    numbers = [ i+1 for i in range(N) ]
    combs = combinations_with_replacement(numbers, M)
    for c in combs:
        print(*c)
