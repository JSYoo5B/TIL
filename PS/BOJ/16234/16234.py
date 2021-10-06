#!/usr/bin/env python3

from collections import deque
from copy import deepcopy

def relocate(popus, bounds):
    next_popus = deepcopy(popus)
    for r in range(len(popus)):
        for c in range(len(popus[0])):
            # When the population relocated, each nation will be marked as -1
            if popus[r][c] == -1 or popus[r][c] == -2:
                continue

            union_nations = get_union_nations(popus, [r, c], bounds)
            new_popu = popus[r][c]
            mark = -2
            if len(union_nations) > 1:
                new_popu = sum([ popus[n[0]][n[1]] for n in union_nations ]) // len(union_nations)
                mark = -1
            for n in union_nations:
                next_popus[n[0]][n[1]] = new_popu
                popus[n[0]][n[1]] = mark
    return next_popus


def get_union_nations(popus, start_nation, bounds):
    que = deque([start_nation])
    nations = [start_nation]
    row_max, col_max = len(popus), len(popus[0])
    while len(que) > 0:
        current = que.popleft()
        r, c = current[0], current[1]
        neighbors = [ n for n in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]] \
                if 0 <= n[0] < row_max and 0 <= n[1] < col_max and n not in nations ]
        for n in neighbors:
            n_r, n_c = n[0], n[1]
            if popus[n_r][n_c] == -1 or popus[n_r][n_c] == -2:
                continue
            diff = max(popus[r][c], popus[n_r][n_c]) - min(popus[r][c], popus[n_r][n_c])
            if bounds[0] <= diff <= bounds[1]:
                nations.append(n)
                que.append(n)
    return nations


if __name__ == '__main__':
    N, low, high = map(int, input().split())
    popus = []
    for _ in range(N):
        row = list(map(int, input().split()))
        popus.append(row)

    date_elapsed = -1
    repos_cnt = 1
    while repos_cnt > 0:
        date_elapsed += 1
        next_popus = relocate(popus, [low, high])

        repos_cnt = sum([row.count(-1) for row in popus])
        popus = next_popus
    print(date_elapsed)
