#!/usr/bin/env python3

from itertools import combinations

if __name__ == '__main__':
    N, M = map(int, input().split())
    numbers = [ i for i in range(1, N+1) ]
    combs = combinations(numbers, M)
    for c in combs:
        print(*c)
