#!/usr/bin/env python3

from itertools import combinations
from collections import defaultdict

def get_subset_sums(numbers):
    subset_sums = defaultdict(int)
    for samp_cnt in range(len(numbers)+1):
        combs = combinations(numbers, samp_cnt)
        for com in combs:
            subset_sums[sum(com)] += 1
    return sorted(subset_sums.items())


if __name__ == '__main__':
    nums_cnt, tgt_num = map(int, input().split())
    numbers = list(map(int, input().split()))

    lefts, rights = numbers[:nums_cnt//2], numbers[nums_cnt//2:]
    left_sums = get_subset_sums(lefts)
    right_sums = get_subset_sums(rights)
    right_sums.reverse()

    l_i, r_i = 0, 0
    l_cnt, r_cnt = len(left_sums), len(right_sums)
    answer = 0
    while l_i < l_cnt and r_i < r_cnt:
        result = left_sums[l_i][0] + right_sums[r_i][0]
        if result == tgt_num:
            answer += left_sums[l_i][1] * right_sums[r_i][1]
            l_i += 1
            r_i += 1
        elif result < tgt_num:
            l_i += 1
        else:
            r_i += 1
    if tgt_num == 0:
        answer -= 1
    print(answer)
