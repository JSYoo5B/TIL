#!/usr/bin/env python3

from math import sqrt

def calculate(x1, y1, r1, x2, y2, r2):
    dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    max_r = max(r1, r2)
    min_r = min(r1, r2)

    # When the center are same
    if dist == 0:
        # r1 == r2, it's same circle
        if max_r == min_r:
            return -1
        # otherwise, no any point intersects
        else:
            return 0
    # When the two circles tangents
    elif dist == (max_r + min_r) or dist == (max_r - min_r):
        return 1
    # When the two circle doesn't intersects
    elif dist > (max_r + min_r) or max_r > (dist + min_r):
        return 0
    else:
        return 2

if __name__ == '__main__':
    cases = int(input())

    for i in range(0, cases):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        answer = calculate(x1, y1, r1, x2, y2, r2)
        print(answer)
