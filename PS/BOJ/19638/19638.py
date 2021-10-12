#!/usr/bin/env python3

import heapq

if __name__ == '__main__':
    giants_cnt, centi_height, trial_max = map(int, input().split())
    giants = []
    for _ in range(giants_cnt):
        giant = int(input())
        heapq.heappush(giants, -1 * giant)

    found = False
    for trial in range(trial_max + 1):
        greatest = -1 * heapq.heappop(giants)
        if greatest < centi_height:
            print("YES")
            print(trial)
            found = True
            break
        if trial == trial_max:
            heapq.heappush(giants, -1 * greatest)
            break
        if greatest > 1:
            greatest //= 2
        heapq.heappush(giants, -1 * greatest)
    if not found:
        greatest = -1 * heapq.heappop(giants)
        print("NO")
        print(greatest)
