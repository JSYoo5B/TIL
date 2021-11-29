#!/usr/bin/env python3

import sys
input = sys.stdin.readline

if __name__ == '__main__':
    nums_cnt, queries_cnt = map(int, input().split())
    numbers = list(map(int, input().split()))

    acc_sum = [ 0 for i in range(nums_cnt+1) ]
    for i in range(1, nums_cnt+1):
        acc_sum[i] = acc_sum[i-1] + numbers[i-1]
    for _ in range(queries_cnt):
        start, end = map(int, input().split())
        answer = acc_sum[end] - acc_sum[start-1]
        print(answer)
