#!/usr/bin/env python3

import sys
from copy import deepcopy
from collections import deque
from itertools import combinations

input = sys.stdin.readline

def spread_viruses(lab_status, init_points):
    time_elapsed, non_virus_elapsed = 0, 0
    que = deque([ [i, 0] for i in init_points])
    while len(que) > 0:
        [[cur_r, cur_c], step] = que.popleft()
        time_elapsed = max(time_elapsed, step)
        neighbors = [ [cur_r - 1, cur_c], [cur_r + 1, cur_c], \
                [cur_r, cur_c - 1], [cur_r, cur_c + 1] ]
        for [n_r, n_c] in neighbors:
            if 0 > n_r or n_r >= len(lab_status) \
                    or 0 > n_c or n_c >= len(lab_status[0]):
                continue
            if lab_status[n_r][n_c] == 0:
                lab_status[n_r][n_c] = 3
                non_virus_elapsed = step + 1
                que.append([[n_r, n_c], step + 1])
            elif lab_status[n_r][n_c] == 2:
                lab_status[n_r][n_c] = 3
                que.append([[n_r, n_c], step + 1])
    return min(time_elapsed, non_virus_elapsed)


def count_empty_spaces(lab_status):
    empty_cnt = 0
    for row in lab_status:
        empty_cnt += row.count(0)
    return empty_cnt


if __name__ == '__main__':
    lab_size, active_cnt = map(int, input().split())
    lab_status = []
    virus_pos = []
    for r in range(lab_size):
        row = list(map(int, input().split()))
        virus_detected = [ [r, c] for c in range(lab_size) if row[c] == 2 ]
        virus_pos += virus_detected
        lab_status.append(row)

    time_elapsed = lab_size ** 2
    select_viruses = combinations(virus_pos, active_cnt)
    new_status = deepcopy(lab_status)
    for viruses in select_viruses:
        recent_elapsed = spread_viruses(new_status, viruses)
        empty_cnt = count_empty_spaces(new_status)
        if empty_cnt == 0:
            time_elapsed = min(time_elapsed, recent_elapsed)
        for r in range(lab_size):
            for c in range(lab_size):
                new_status[r][c] = lab_status[r][c]
    if time_elapsed == lab_size ** 2:
        time_elapsed = -1

    print(time_elapsed)
