#!/usr/bin/env python3

from collections import deque

def grp_islands(tbl, grp_id, pos):
    tbl_size = len(tbl)
    [r, c] = pos

    tbl[r][c] = grp_id
    que = deque([ [r, c] ])
    shores = []
    while len(que) > 0:
        [r, c] = que.popleft()
        is_shore = False
        for [n_r, n_c] in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
            if 0 > n_r or n_r >= tbl_size or 0 > n_c or n_c >= tbl_size:
                continue
            if tbl[n_r][n_c] == -1:
                tbl[n_r][n_c] = grp_id
                que.append([n_r, n_c])
            elif tbl[n_r][n_c] == 0:
                is_shore = True
        if is_shore:
            shores.append([r, c])
    return shores


def expand_isle(shores, tbl, isle_id):
    tbl_size = len(tbl)
    next_shores = []
    for [r, c] in shores:
        for [n_r, n_c] in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
            if 0 > n_r or n_r >= tbl_size or 0 > n_c or n_c >= tbl_size:
                continue
            if tbl[n_r][n_c] == 0:
                tbl[n_r][n_c] = isle_id
                next_shores.append([n_r, n_c])
    return next_shores


def peek_adjusts(shores, tbl, isle_id):
    tbl_size = len(tbl)
    adjusts = []
    for [r, c] in shores:
        for [n_r, n_c] in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
            if 0 > n_r or n_r >= tbl_size or 0 > n_c or n_c >= tbl_size:
                continue
            if tbl[n_r][n_c] != 0 and tbl[n_r][n_c] != isle_id:
                if tbl[n_r][n_c] not in adjusts:
                    adjusts.append(tbl[n_r][n_c])
    return adjusts


if __name__ == '__main__':
    tbl_size = int(input())
    tbl = []
    for _ in range(tbl_size):
        row = list(map(int, input().split()))
        row = [ -i for i in row ]
        tbl.append(row)

    isle_cnt = 0
    isle_shores = []
    for r in range(tbl_size):
        for c in range(tbl_size):
            if tbl[r][c] == -1:
                shores = grp_islands(tbl, isle_cnt + 1, [r, c])
                isle_shores.append(shores)
                isle_cnt += 1

    answers = []
    expand_dists = [ 0 for _ in range(isle_cnt) ]
    isle_id = 0
    while True:
        if isle_id == 0 and len(answers) > 0:
            break
        next_shores = expand_isle(isle_shores[isle_id], tbl, isle_id+1)
        expand_dists[isle_id] += 1
        adjusts = peek_adjusts(next_shores, tbl, isle_id+1)
        for other in adjusts:
            other -= 1
            answers.append(expand_dists[isle_id] + expand_dists[other])
        isle_shores[isle_id] = next_shores
        isle_id += 1
        isle_id %= isle_cnt
    print(min(answers))
