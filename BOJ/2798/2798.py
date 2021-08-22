#!/usr/bin/env python3

from itertools import combinations

if __name__ == '__main__':
    cards_cnt, target_num = map(int, input().split())
    numbers = list(map(int, input().split()))
    cases = combinations(numbers, 3)
    avails = [ sum(nums) for nums in cases if sum(nums) <= target_num ]
    answer = max(avails)
    print(answer)

