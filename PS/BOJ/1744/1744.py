#!/usr/bin/env python3

import sys
input = sys.stdin.readline

if __name__ == '__main__':
    nums_cnt = int(input())
    
    negatives = []
    zeros_cnt, ones_cnt = 0, 0
    positives = []
    for _ in range(nums_cnt):
        num = int(input())
        if num < 0:
            negatives.append(num)
        elif num == 0:
            zeros_cnt += 1
        elif num == 1:
            ones_cnt += 1
        else:
            positives.append(num)

    negatives.sort()
    negatives.reverse()
    positives.sort()

    answer = 0
    while len(negatives) > 0:
        if len(negatives) >= 2:
            answer += negatives[-1] * negatives[-2]
            negatives.pop()
        elif zeros_cnt == 0:
            answer += negatives[0]
        negatives.pop()
    while len(positives) > 0:
        if len(positives) >= 2:
            answer += positives[-1] * positives[-2]
            positives.pop()
        else:
            answer += positives[0]
        positives.pop()
    answer += ones_cnt
    print(answer)
