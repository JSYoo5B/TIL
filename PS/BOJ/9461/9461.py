#!/usr/bin/env python3

from sys import stdin
input = stdin.readline

def get_waveform_seq(n, memo = [1, 1, 1, 2, 2]):
    if len(memo) >= n:
        return memo[n-1]
    
    for _ in range(len(memo), n):
        next = memo[-1] + memo[-5]
        memo.append(next)

    return memo[-1]


if __name__ == '__main__':
    test_cnt = int(input())
    for _ in range(test_cnt):
        n = int(input())
        answer = get_waveform_seq(n)
        print(answer)
