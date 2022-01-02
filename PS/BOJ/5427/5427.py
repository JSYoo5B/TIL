#!/usr/bin/env python3

from collections import deque
from sys import stdin
input = stdin.readline

SPACE, WALL, HUMAN, FIRE = [0, 1, 2, 3]
CONV_MAP = { "." : SPACE, "#" : WALL, "@" : HUMAN, "*" : FIRE }


def escape(tbl):
    row_sz, col_sz = len(tbl), len(tbl[0])
    humans, fires = deque([]), deque([])
    for r in range(row_sz):
        for c in range(col_sz):
            if tbl[r][c] == HUMAN:
                humans.append([0, r, c])
            elif tbl[r][c] == FIRE:
                fires.append([0, r, c])
    
    answer, cur_step = -1, 0
    while len(humans) > 0 and answer == -1:
        # Spread fire first
        while len(fires) > 0 and cur_step == fires[0][0]:
            cur_step, r, c = fires.popleft()
            for [n_r, n_c] in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
                if 0 > n_r or n_r >= row_sz or 0 > n_c or n_c >= col_sz:
                    continue
                if tbl[n_r][n_c] == SPACE:
                    tbl[n_r][n_c] = FIRE
                    fires.append([cur_step+1, n_r, n_c])

        # Try to move
        while len(humans) > 0 and cur_step == humans[0][0]:
            cur_step, r, c = humans.popleft()
            if r in [0, row_sz-1] or c in [0, col_sz-1]:
                answer = cur_step + 1
                break
            for [n_r, n_c] in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
                if 0 > n_r or n_r >= row_sz or 0 > n_c or n_c >= col_sz:
                    continue
                if tbl[n_r][n_c] == SPACE:
                    tbl[n_r][n_c] = HUMAN
                    humans.append([cur_step+1, n_r, n_c])

        # Increase next step
        cur_step += 1

    return answer


if __name__ == '__main__':
    test_cnt = int(input())
    for _ in range(test_cnt):
        col_size, row_size = map(int, input().split())
        tbl = []
        for r in range(row_size):
            line = input().rstrip()
            row = [ CONV_MAP[c] for c in line ]
            tbl.append(row)
        
        answer = escape(tbl)
        if answer == -1:
            print("IMPOSSIBLE")
        else:
            print(answer)
