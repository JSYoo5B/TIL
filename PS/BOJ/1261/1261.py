#!/usr/bin/env python3

from collections import deque
from sys import stdin
input = stdin.readline


def get_lowest_cost(tbl):
    row_cnt, col_cnt = len(tbl), len(tbl[0])
    costs = [ [ -1 for _ in range(col_cnt) ] for _ in range(row_cnt) ] 
    costs[0][0] = 0
    que = deque([[0, 0]])
    while len(que) > 0:
        [r, c] = que.popleft()
        if r == row_cnt-1 and c == col_cnt - 1:
            break
        for [n_r, n_c] in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
            if 0 > n_r or n_r >= row_cnt or 0 > n_c or n_c >= col_cnt:
                continue
            if costs[n_r][n_c] > -1:
                continue
            if tbl[n_r][n_c] == 1:
                que.append([n_r, n_c])
                costs[n_r][n_c] = costs[r][c] + 1
            else:
                que.appendleft([n_r, n_c])
                costs[n_r][n_c] = costs[r][c]

    return costs[-1][-1]


if __name__ == '__main__':
    col_cnt, row_cnt = map(int, input().split())
    tbl = []
    for _ in range(row_cnt):
        line = input().rstrip()
        row = [ int(i) for i in line ]
        tbl.append(row)

    answer = get_lowest_cost(tbl)
    print(answer)
