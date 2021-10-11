#!/usr/bin/env python3

import heapq

if __name__ == '__main__':
    visits_cnt = int(input())
    knapsack = []
    for _ in range(visits_cnt):
        visit_info = list(map(int, input().split()))
        if len(visit_info) == 1:
            # When the length of visit_info is one,
            # it means first number will be 0, asks to pop from heapq
            if len(knapsack) > 0:
                gift = -1 * heapq.heappop(knapsack)
                print(gift)
            else:
                print(-1)
        else:
            for g in visit_info[1:]:
                heapq.heappush(knapsack, -1 * g)
