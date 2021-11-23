#!/usr/bin/env python3

from itertools import permutations

if __name__ == '__main__':
    nums_cnt, samp_cnt = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()
    permutes = permutations(numbers, samp_cnt)
    for p in permutes:
        print(*p)
