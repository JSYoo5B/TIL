#!/usr/bin/env python3

from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    size = int(input())
    mins, maxes = [ 0 for _ in range(3) ], [ 0 for _ in range(3) ]
    tmp = [ 0 for _ in range(3) ]
    for _ in range(size):
        nums = list(map(int, input().split()))
        
        tmp[0] = min(mins[0], mins[1]) + nums[0]
        tmp[1] = min(mins) + nums[1]
        tmp[2] = min(mins[1], mins[2]) + nums[2]
        for i in range(3):
            mins[i] = tmp[i]

        tmp[0] = max(maxes[0], maxes[1]) + nums[0]
        tmp[1] = max(maxes) + nums[1]
        tmp[2] = max(maxes[1], maxes[2]) + nums[2]
        for i in range(3):
            maxes[i] = tmp[i]

    print(max(maxes), min(mins))
