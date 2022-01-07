#!/usr/bin/env python3

from collections import deque
from itertools import combinations
from sys import stdin
input = lambda : stdin.readline().rstrip()

def is_connected(selected, edges):
    visited = [selected[0]]
    que = deque([selected[0]])
    answer = False
    while len(que) > 0:
        cur = que.popleft()
        for neigh in edges[cur]:
            if neigh in selected and neigh not in visited:
                visited.append(neigh)
                que.append(neigh)
    return len(selected) == len(visited)


if __name__ == '__main__':
    reg_cnt = int(input())
    regions = list(map(int, input().split()))
    edges = []
    for i in range(reg_cnt):
        info = list(map(int, input().split()))
        edges.append([i-1 for i in info[1:]])

    reg_idxs = [ i for i in range(reg_cnt) ]
    teams = []
    for sel in range(1, reg_cnt // 2 + 1):
        teams += list(combinations(reg_idxs, sel))

    answer = sum(regions)
    for t1 in teams:
        t2 = [ i for i in reg_idxs if i not in t1 ]
        if is_connected(t1, edges) and is_connected(t2, edges):
            t1_pops = [ regions[i] for i in t1 ]
            t2_pops = [ regions[i] for i in t2 ]
            result = abs(sum(t1_pops) - sum(t2_pops))
            answer = min(answer, result)
        if answer == 0:
            break

    if answer == sum(regions):
        answer = -1

    print(answer)
