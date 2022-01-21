#!/usr/bin/env python3

from collections import defaultdict
from sys import stdin
input = lambda : stdin.readline().rstrip()

if __name__ == '__main__':
    test_cnt = int(input())
    for _ in range(test_cnt):
        items_cnt = int(input())
        items = defaultdict(int)
        for _ in range(items_cnt):
            name, type = input().split()
            items[type] += 1

        answer = 1
        for v in items.values():
            answer *= (v + 1)
        answer -= 1
        print(answer)
