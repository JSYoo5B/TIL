#!/usr/bin/env python3

if __name__ == '__main__':
    cnt_trees, target = map(int, input().split())
    trees = list(map(int, input().split()))

    left, right = 1, max(trees)
    while left <= right:
        mid = (left + right) // 2
        remains = [ t - mid for t in trees if t > mid ]
        log = sum(remains)
        if log >= target:
            left = mid + 1
        else:
            right = mid - 1
    print(right)
