#!/usr/bin/env python3

import sys
from collections import deque

input = sys.stdin.readline

def move_to_fish(tbl, shark_pos, shark_size):
    tbl_size = len(tbl)

    time_elapsed = tbl_size ** 2
    end_candidates = []

    que = deque([ [shark_pos, 0] ])
    visited = [ [ 0 for _ in range(tbl_size) ] for _ in range(tbl_size) ]
    visited[shark_pos[0]][shark_pos[1]] = 1
    while len(que) > 0:
        [[r, c], time] = que.popleft()
        if 0 < tbl[r][c] < 7 and tbl[r][c] < shark_size \
                and time_elapsed >= time:
            time_elapsed = time
            end_candidates.append([r, c])
            continue

        neighbors = [ [r-1, c], [r, c-1], [r, c+1], [r+1, c] ]
        for [n_r, n_c] in neighbors:
            if 0 > n_r or n_r >= tbl_size \
                    or 0 > n_c or n_c >= tbl_size:
                continue
            if visited[n_r][n_c] == 0 \
                    and tbl[n_r][n_c] <= shark_size:
                visited[n_r][n_c] = 1
                que.append([[n_r, n_c], time + 1])
    
    end_candidates.sort()
    if time_elapsed == tbl_size ** 2:
        return 0, shark_pos
    else:
        return time_elapsed, end_candidates[0]


if __name__ == '__main__':
    tbl_size = int(input())
    tbl = []
    shark_pos = []
    for row_idx in range(tbl_size):
        row = list(map(int, input().split()))
        if row.count(9) == 1:
            col_idx = row.index(9)
            shark_pos = [row_idx, col_idx]
            row[col_idx] = 0
        tbl.append(row)

    elapsed_accum = 0
    shark_size = 2
    eat_accum = 0
    while True:
        elapsed, new_pos = move_to_fish(tbl, shark_pos, shark_size)
        if elapsed == 0:
            break
        elapsed_accum += elapsed
        eat_accum += 1
        if eat_accum == shark_size:
            shark_size += 1
            if shark_size > 7:
                shark_size = 7
            eat_accum = 0
        tbl[new_pos[0]][new_pos[1]] = 0
        shark_pos = new_pos
    print(elapsed_accum)
