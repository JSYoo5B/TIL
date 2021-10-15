#!/usr/bin/env python3

import sys
import heapq

input = sys.stdin.readline

if __name__ == '__main__':
    jewel_cnt, bag_cnt = map(int, input().split())
    jewels = []
    for _ in range(jewel_cnt):
        jewel_info = list(map(int, input().split()))
        heapq.heappush(jewels, jewel_info)
    bags = []
    for _ in range(bag_cnt):
        capacity = int(input())
        heapq.heappush(bags, capacity)

    answer = 0
    avail_jewels = []
    while len(bags) > 0:
        capacity = heapq.heappop(bags)
        while len(jewels) > 0:
            [weight, price] = heapq.heappop(jewels)
            if weight <= capacity:
                heapq.heappush(avail_jewels, -1 * price)
            else:
                heapq.heappush(jewels, [weight, price])
                break

        if len(avail_jewels) > 0:
            answer += -1 * heapq.heappop(avail_jewels)
    print(answer)
