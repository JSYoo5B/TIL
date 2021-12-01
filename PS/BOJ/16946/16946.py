#!/usr/bin/env python3

from collections import deque
import sys

input = sys.stdin.readline


def mark_spaces(tbl, pos, id):
    row_cnt, col_cnt = len(tbl), len(tbl[0])

    que = deque([pos])
    visited = [pos]
    tbl[pos[0]][pos[1]] = id
    while len(que) > 0:
        [r, c] = que.popleft()
        for n_r, n_c in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
            if 0 > n_r or n_r >= row_cnt or 0 > n_c or n_c >= col_cnt:
                continue
            if tbl[n_r][n_c] == 0:
                tbl[n_r][n_c] = id
                visited.append([n_r, n_c])
                que.append([n_r, n_c])
    return len(visited)


def get_spaces(pos, tbl, space_sizes):
    row_cnt, col_cnt = len(tbl), len(tbl[0])
    r, c = pos
    result = 1
    neighbor_spaces = []
    for n_r, n_c in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
        if 0 > n_r or n_r >= row_cnt or 0 > n_c or n_c >= col_cnt:
            continue
        neighbor_spaces.append(tbl[n_r][n_c])
    
    neighbor_spaces = list(set(neighbor_spaces))
    for s in neighbor_spaces:
        result += space_sizes[s]
    return result


if __name__ == '__main__':
    row_cnt, col_cnt = map(int, input().split())
    base_tbl, walls_pos = [], []
    for r in range(row_cnt):
        row = [ c for c in input().rstrip() ]
        for c in range(col_cnt):
            row[c] = int(row[c])
            if row[c] == 1:
                walls_pos.append([r, c])
        base_tbl.append(row)

    space_sizes = [0, 0]
    space_id = 2
    for r in range(row_cnt):
        for c in range(col_cnt):
            if base_tbl[r][c] == 0:
                space_size = mark_spaces(base_tbl, [r, c], space_id)
                space_sizes.append(space_size)
                space_id += 1

    result_tbl = [ [ 0 for _ in range(col_cnt) ] for _ in range(row_cnt) ]
    for r, c in walls_pos:
        result_tbl[r][c] = get_spaces([r, c], base_tbl, space_sizes)
        result_tbl[r][c] %= 10

    for row in result_tbl:
        print("".join([str(c) for c in row]))

