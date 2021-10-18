#!/usr/bin/env python3

import copy
from collections import deque

def rotate_gear(gear, dir):
    gear.rotate(dir)

if __name__ == '__main__':
    gears = []
    for _ in range(4):
        gear_info = input()
        gear = deque([int(i) for i in gear_info])
        gears.append(gear)

    rotate_cnt = int(input())
    for _ in range(rotate_cnt):
        rotate_tasks = []
        gear_idx, dir = map(int, input().split())
        gear_idx -= 1 # offset to 0 starting index

        rotate_tasks.append([gear_idx, dir])

        left_idx, left_sign = gear_idx - 1, gears[gear_idx][6]
        cur_dir = -1 * dir
        while left_idx >= 0:
            if left_sign == gears[left_idx][2]:
                break
            else:
                left_sign = gears[left_idx][6]
                rotate_tasks.append([left_idx, cur_dir])
                left_idx -= 1
                cur_dir *= -1
        
        right_idx, right_sign = gear_idx + 1, gears[gear_idx][2]
        cur_dir = -1 * dir
        while right_idx < 4:
            if right_sign == gears[right_idx][6]:
                break
            else:
                right_sign = gears[right_idx][2]
                rotate_tasks.append([right_idx, cur_dir])
                right_idx += 1
                cur_dir *= -1
        
        for t in rotate_tasks:
            [idx, dir] = t
            rotate_gear(gears[idx], dir)
    answer = gears[0][0] + gears[1][0] * 2 + gears[2][0] * 4 + gears[3][0] * 8
    print(answer)
