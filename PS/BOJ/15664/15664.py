#!/usr/bin/env python3

from itertools import combinations


if __name__ == '__main__':
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()

    combs = set(list(combinations(numbers, M)))
    answers = list(combs)
    answers.sort()
    for c in answers:
        print(*c)
