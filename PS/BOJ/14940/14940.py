#!/usr/bin/env python3

from collections import deque
import sys
input = sys.stdin.readline

def get_dists(tbl, pos):
    row_cnt, col_cnt = len(tbl), len(tbl[0])
    que = deque([[pos, 0]])
    while len(que) > 0:
        [[r, c], dist] = que.popleft()
        for [n_r, n_c] in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
            if 0 > n_r or n_r >= row_cnt \
                    or 0 > n_c or n_c >= col_cnt:
                continue
            if tbl[n_r][n_c] == -1:
                tbl[n_r][n_c] = dist + 1
                que.append([[n_r, n_c], dist+1])

if __name__ == '__main__':
    row_cnt, col_cnt = map(int, input().split())
    tbl = []
    start_pos = [-1, -1]
    for r in range(row_cnt):
        row = list(map(int, input().split()))
        if row.count(2) == 1:
            start_pos = [r, row.index(2)]
            row[row.index(2)] = 0
        conv_row = [ -1 * i for i in row ]
        tbl.append(conv_row)

    get_dists(tbl, start_pos)

    for row in tbl:
        print(*row)
