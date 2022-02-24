#!/usr/bin/env python3

from itertools import permutations
from copy import deepcopy
from collections import deque
from sys import stdin
input = lambda : stdin.readline().rstrip()

def rotate_matrix(mat, row, col, radius):
    row_sz, col_sz = len(mat), len(mat[0])
    for sz in range(1, radius + 1):
        que = deque()
        # top
        r = row - sz
        for c in range(col - sz, col + sz + 1):
            que.append(mat[r][c])
        # right
        c = col + sz
        for r in range(row - sz + 1, row + sz + 1):
            que.append(mat[r][c])
        # bottom
        r = row + sz
        for c in range(col + sz - 1, col - sz - 1, -1):
            que.append(mat[r][c])
        # left
        c = col - sz
        for r in range(row + sz - 1, row - sz, -1):
            que.append(mat[r][c])

        que.rotate(1)
        # top
        r = row - sz
        for c in range(col - sz, col + sz + 1):
            mat[r][c] = que.popleft()
        # right
        c = col + sz
        for r in range(row - sz + 1, row + sz + 1):
            mat[r][c] = que.popleft()
        # bottom
        r = row + sz
        for c in range(col + sz - 1, col - sz - 1, -1):
            mat[r][c] = que.popleft()
        # left
        c = col - sz
        for r in range(row + sz - 1, row - sz, -1):
            mat[r][c] = que.popleft()
    return


if __name__ == '__main__':
    row_sz, col_sz, op_cnt = map(int, input().split())
    matrix, ops = [], []
    for _ in range(row_sz):
        row = list(map(int, input().split()))
        matrix.append(row)
    for _ in range(op_cnt):
        r, c, radius = map(int, input().split())
        ops.append([r-1, c-1, radius])

    answer = row_sz * col_sz * 1000
    for op_orders in permutations(ops, op_cnt):
        mat = deepcopy(matrix)
        for [r, c, radius] in op_orders:
            rotate_matrix(mat, r, c, radius)
        for row in mat:
            answer = min(answer, sum(row))

    print(answer)

