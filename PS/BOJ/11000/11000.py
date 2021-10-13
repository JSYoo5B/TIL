#!/usr/bin/env python3

import heapq
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    lectures_cnt = int(input())
    lectures = []
    for _ in range(lectures_cnt):
        start, end = map(int, input().split())
        lectures.append([start, end])
    
    lectures.sort()
    classroom_avails = [ lectures[0][1] ]
    for l in lectures[1:]:
        early_avail = heapq.heappop(classroom_avails)
        if l[0] < early_avail:
            heapq.heappush(classroom_avails, early_avail)
        heapq.heappush(classroom_avails, l[1])
    answer = len(classroom_avails)
    print(answer)
