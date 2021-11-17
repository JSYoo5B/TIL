#!/usr/bin/env python3

from collections import deque

def get_far_dist(tbl, pos):
    row_cnt, col_cnt = len(tbl), len(tbl[0])
    que = deque([ [pos, 0] ])
    visited = [[0 for _ in range(col_cnt)] for _ in range(row_cnt)]
    visited[pos[0]][pos[1]] = 1
    dist = 0
    while len(que) > 0:
        [[r, c], dist] = que.popleft()
        for [n_r, n_c] in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
            if 0 > n_r or n_r >= row_cnt \
                    or 0 > n_c or n_c >= col_cnt:
                continue
            if tbl[n_r][n_c] == 'L' and visited[n_r][n_c] == 0:
                visited[n_r][n_c] = 1
                que.append([[n_r, n_c], dist+1])
    return dist


if __name__ == '__main__':
    row_cnt, col_cnt = map(int, input().split())
    tbl = []
    for _ in range(row_cnt):
        row = input()
        tbl.append(row)

    answer = 0
    for r in range(row_cnt):
        for c in range(col_cnt):
            if tbl[r][c] == 'L':
                answer = max(answer, get_far_dist(tbl, [r, c]))
    print(answer)
