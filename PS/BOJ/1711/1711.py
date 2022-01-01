#!/usr/bin/env python3

from itertools import combinations
from sys import stdin
input = stdin.readline

def get_lineseg_sq_len(p1, p2):
    return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2


if __name__ == '__main__':
    points_cnt = int(input())
    points = []
    for _ in range(points_cnt):
        p = list(map(int, input().split()))
        points.append(p)

    answer = 0
    triples = combinations(points, 3)
    for p1, p2, p3 in triples:
        lines = [ get_lineseg_sq_len(p1, p2), \
                get_lineseg_sq_len(p2, p3), get_lineseg_sq_len(p3, p1) ]
        lines.sort()
        if lines[-1] * 2 == sum(lines):
            answer += 1
    print(answer)
