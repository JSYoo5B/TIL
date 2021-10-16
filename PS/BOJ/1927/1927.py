#!/usr/bin/env python3

import heapq
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    operations_cnt = int(input())
    heap = []
    for _ in range(operations_cnt):
        operation = int(input())
        if operation == 0:
            answer = 0
            if len(heap) > 0:
                answer = heapq.heappop(heap)
            print(answer)
        else:
            heapq.heappush(heap, operation)
            
