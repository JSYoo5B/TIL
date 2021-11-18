#!/usr/bin/env python3

from collections import deque
import sys

input = sys.stdin.readline


def traverse(tbl, sword_pos, max_step):
    row_cnt, col_cnt = len(tbl), len(tbl[0])
    naive_step, sword_step = row_cnt * col_cnt, row_cnt * col_cnt
    sword_adjust = abs(sword_pos[0] - (row_cnt-1))
    sword_adjust += abs(sword_pos[1] - (col_cnt-1))
    que = deque([ [0, 0, 0] ])
    tbl[0][0] = 1
    while len(que) > 0:
        [r, c, step] = que.popleft()
        if step > max_step:
            break
        if r == row_cnt - 1 and c == col_cnt - 1:
            naive_step = step
            break
        for [n_r, n_c] in [ [r-1, c], [r+1, c], [r, c-1], [r, c+1] ]:
            if 0 > n_r or n_r >= row_cnt or 0 > n_c or n_c >= col_cnt:
                continue
            if tbl[n_r][n_c] != 1:
                que.append([n_r, n_c, step+1])
                if tbl[n_r][n_c] == 2:
                    sword_step = step + 1
                tbl[n_r][n_c] = 1

    return min(naive_step, sword_step + sword_adjust)


if __name__ == '__main__':
    row_cnt, col_cnt, max_step = map(int, input().split())
    tbl = []
    sword_pos = []
    for r in range(row_cnt):
        row = list(map(int, input().split()))
        if row.count(2) == 1:
            sword_pos = [r, row.index(2)]
        tbl.append(row)

    theorical_max = row_cnt * col_cnt - 1
    if max_step > theorical_max:
        max_step = theorical_max
    answer = traverse(tbl, sword_pos, max_step)
    if answer > max_step:
        print("Fail")
    else:
        print(answer)
