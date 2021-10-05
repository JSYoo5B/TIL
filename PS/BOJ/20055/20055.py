#!/usr/bin/env python3

from collections import deque

if __name__ == '__main__':
    N, obsolete_threshold = map(int, input().split())
    durabilities = list(map(int, input().split()))
    
    belts = deque(durabilities)
    robots = deque([ False for _ in range(N) ])
    
    steps_cnt = 1
    while True:
        # Step 1, rotate tables and its robots
        belts.rotate(1)
        robots.rotate(1)
        robots[-1] = False

        # Step 2, move robots
        for i in range(N-2, -1, -1):
            if robots[i] == False:
                continue
            elif robots[i+1] == False and belts[i+1] > 0:
                robots[i + 1] = True
                robots[i] = False
                belts[i + 1] -= 1
        robots[-1] = False

        # Step 3, add robots when the pos 0 remains durability
        if belts[0] > 0:
            robots[0] = True
            belts[0] -= 1
        
        # Step 4, check obsolete belts (which has 0 durability) and decide to stop
        if belts.count(0) >= obsolete_threshold:
            break
        steps_cnt += 1
        
    print(steps_cnt)

