#!/usr/bin/env python3

from collections import deque
from sys import stdin
input = lambda : stdin.readline().rstrip()

if __name__ == '__main__':
    wines_cnt = int(input())
    wines = [0]
    for _ in range(wines_cnt):
        wines.append(int(input()))

    scores = deque([])
    scores.append(0)
    scores.append(wines[1])
    if wines_cnt > 1:
        scores.append(wines[1] + wines[2])
        
    for i in range(3, wines_cnt+1):
        next = max(scores[-2], scores[-3] + wines[i-1]) + wines[i]
        next = max(scores[-1], next)
        scores.popleft()
        scores.append(next)

    print(scores[-1])
