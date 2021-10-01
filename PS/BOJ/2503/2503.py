#!/usr/bin/env python3

from itertools import permutations

if __name__ == '__main__':
    input_cnt = int(input())
    avails = list(permutations([ i for i in range(1, 10) ], 3))

    for _ in range(input_cnt):
        trial, strike, ball = map(int, input().split())
        numbers = [ int(i) for i in str(trial) ]
        
        for avail_idx in range(len(avails)):
            cur_strike, cur_ball = 0, 0
            for i in range(3):
                if numbers[i] in avails[avail_idx]:
                    if numbers[i] == avails[avail_idx][i]:
                        cur_strike += 1
                    else:
                        cur_ball += 1
            if cur_strike != strike or cur_ball != ball:
                avails[avail_idx] = None
            
        avails = [ a for a in avails if a is not None ]
    print(len(avails))
