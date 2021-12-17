#!/usr/bin/env python3

from sys import stdin
input = stdin.readline

from heapq import heappush, heappop

if __name__ == '__main__':
    persons_cnt, stats_cnt = map(int, input().split())
    persons = []
    stats_heap, local_max = [], -1
    for i in range(persons_cnt):
        person = list(map(int, input().split()))
        person.sort()
        local_max = max(local_max, person[0])
        heappush(stats_heap, [person[0], i])
        persons.append(person)

    min_diff = local_max - stats_heap[0][0]
    indices = [ 0 for _ in range(persons_cnt) ]
    while len(stats_heap) > 0:
        head = heappop(stats_heap)
        min_diff = min(min_diff, local_max - head[0])
        next_person = head[1]
        indices[next_person] += 1
        if indices[next_person] == stats_cnt:
            break
        next_stat = persons[next_person][indices[next_person]]
        local_max = max(local_max, next_stat)
        heappush(stats_heap, [next_stat, next_person])
    print(min_diff)
