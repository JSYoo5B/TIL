#!/usr/bin/env python3

from collections import deque

def rotate_array(origin, rotate_cnt):
    row_cnt, col_cnt = len(origin), len(origin[0])
    result = [ [ 0 for _ in range(col_cnt) ] for _ in range(row_cnt) ]

    rotate_loops = min(row_cnt, col_cnt) // 2
    for order in range(rotate_loops):
        row_lb, row_ub = 0 + order, row_cnt - order
        col_lb, col_ub = 0 + order, col_cnt - order
        # top, right direction
        elems = [ origin[row_lb][c] for c in range(col_lb, col_ub) ]
        locs = [ [row_lb, c] for c in range(col_lb, col_ub) ]
        # right, down direction
        elems += [ origin[r][col_ub-1] for r in range(row_lb+1, row_ub-1) ]
        locs += [ [r, col_ub-1] for r in range(row_lb+1, row_ub-1) ]
        # bottom, left direction
        elems += [ origin[row_ub-1][c] for c in range(col_ub-1, col_lb-1, -1) ]
        locs += [ [row_ub-1, c] for c in range(col_ub-1, col_lb-1, -1) ]
        # left, up direction
        elems += [ origin[r][col_lb] for r in range(row_ub-2, row_lb, -1) ]
        locs += [ [r, col_lb] for r in range(row_ub-2, row_lb, -1) ]
        # rotate elements
        que = deque(elems)
        actual_rotate_cnt = rotate_cnt % len(que)
        que.rotate(-1 * actual_rotate_cnt)
        for [r, c] in locs:
            result[r][c] = que.popleft()

    return result


if __name__ == '__main__':
    row_cnt, col_cnt, rotate_cnt = map(int, input().split())
    origin_table = []
    for _  in range(row_cnt):
        row = list(map(int, input().split()))
        origin_table.append(row)

    rotate_table = rotate_array(origin_table, rotate_cnt)
    for r in rotate_table:
        print(*r)
