#!/usr/bin/env python3

import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

def dual_priority_queue_test():
    operation_cnt = int(input())
    min_heap, max_heap = [], []
    counter = defaultdict(int)
    for _ in range(operation_cnt):
        operation, operand = input().split()
        operand = int(operand)
        if operation == 'I':
            heapq.heappush(min_heap, operand)
            heapq.heappush(max_heap, -1 * operand)
            counter[operand] += 1
        elif len(max_heap) > 0:
            if operand == -1:
                while len(min_heap) > 0:
                    min_val = heapq.heappop(min_heap)
                    if counter[min_val] > 0:
                        counter[min_val] -= 1
                        break
            else:
                while len(max_heap) > 0:
                    max_val = -1 * heapq.heappop(max_heap)
                    if counter[max_val] > 0:
                        counter[max_val] -= 1
                        break
    remains = [ i[0] for i in counter.items() if i[1] > 0 ]
    if len(remains) < 1:
        print("EMPTY")
    else:
        min_val = min(remains)
        max_val = max(remains)
        print("{} {}".format(max_val, min_val))

if __name__ == '__main__':
    trials_cnt = int(input())
    for _ in range(trials_cnt):
        dual_priority_queue_test()
