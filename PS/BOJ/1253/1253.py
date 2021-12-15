#!/usr/bin/env python3

if __name__ == '__main__':
    nums_cnt = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()

    answer = 0
    for find_idx in range(nums_cnt):
        target = numbers[find_idx]
        others = numbers[:find_idx] + numbers[find_idx+1:]
        l, r = 0, nums_cnt - 2
        while l < r:
            comb = others[l] + others[r]
            if comb == target:
                answer += 1
                break
            if comb < target:
                l += 1
            else:
                r -= 1
    print(answer)
