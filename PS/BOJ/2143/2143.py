#!/usr/bin/env python3

from collections import defaultdict

if __name__ == '__main__':
    tgt_num = int(input())
    a_cnt = int(input())
    a_nums = list(map(int, input().split()))
    b_cnt = int(input())
    b_nums = list(map(int, input().split()))

    a_sums, b_sums = defaultdict(int), defaultdict(int)
    for l in range(a_cnt):
        for r in range(l, a_cnt):
            a_sums[sum(a_nums[l:r+1])] += 1
    for l in range(b_cnt):
        for r in range(l, b_cnt):
            b_sums[sum(b_nums[l:r+1])] += 1

    kinds = 0
    for a_sum in a_sums.keys():
        kinds += (b_sums[tgt_num-a_sum] * a_sums[a_sum])
    print(kinds)

