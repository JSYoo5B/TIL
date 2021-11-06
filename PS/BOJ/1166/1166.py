#!/usr/bin/env python3

if __name__ == '__main__':
    box_cnt, length, width, height = map(int, input().split())
    left, right = 0.0, float(min(length, width, height))
    trial_left = 100
    while left < right and right-left >= 10 ** -9 and trial_left > 0:
        mid = (left + right) / 2
        cur_cnt = 1
        cur_cnt *= int(length / mid)
        cur_cnt *= int(width / mid)
        cur_cnt *= int(height / mid)
        if cur_cnt < box_cnt:
            right = mid
        else:
            left = mid
        trial_left -= 1
    print(right)
