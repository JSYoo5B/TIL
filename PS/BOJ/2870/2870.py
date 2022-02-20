#!/usr/bin/env python3

import re
from sys import stdin
input = lambda : stdin.readline().rstrip()

if __name__ == '__main__':
    line_cnt = int(input())
    texts = ""
    for _ in range(line_cnt):
        texts += input()
        texts += ' '

    numbers = list(map(int, re.findall(r"\d+", texts)))
    numbers.sort()
    for n in numbers:
        print(n)
