#!/usr/bin/env python3

from collections import deque
from sys import stdin
input = lambda : stdin.readline().rstrip()

if __name__ == '__main__':
    steps_cnt = int(input())
    steps = []
    for _ in range(steps_cnt):
        steps.append(int(input()))

    scores = deque([])
    scores.append(steps[0])
    if steps_cnt > 1:
        scores.append(steps[0] + steps[1])
    if steps_cnt > 2:
        scores.append(max(steps[1] + steps[2], steps[0] + steps[2]))

    for i in range(3, steps_cnt):
        next = max(scores[-2], scores[-3] + steps[i-1]) + steps[i]
        scores.popleft()
        scores.append(next)
        
    print(scores[-1])
