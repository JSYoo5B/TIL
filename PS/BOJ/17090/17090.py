#!/usr/bin/env python3

from sys import stdin
from sys import setrecursionlimit
input = lambda : stdin.readline().rstrip()
setrecursionlimit(10**9)

def escapable_tiles(table, results, r, c):
    if results[r][c] >= 0:
        return results[r][c]

    row_sz, col_sz = len(table), len(table[0])
    n_r, n_c = -1, -1
    if table[r][c] == 'U':
        n_r, n_c = r-1, c
    elif table[r][c] == 'D':
        n_r, n_c = r+1, c
    elif table[r][c] == 'L':
        n_r, n_c = r, c-1
    else:
        n_r, n_c = r, c+1

    if 0 > n_r or n_r >= row_sz or 0 > n_c or n_c >= col_sz:
        results[r][c] = 1
    elif results[n_r][n_c] == -2:
        results[r][c] = 0
    else:
        results[r][c] = -2
        results[r][c] = escapable_tiles(table, results, n_r, n_c)
    return results[r][c]


if __name__ == '__main__':
    row_sz, col_sz = map(int, input().split())
    tbl = []
    for _ in range(row_sz):
        line = [ c for c in input() ]
        tbl.append(line)

    results = [ [ -1 for _ in range(col_sz) ] for _ in range(row_sz) ]
    for r in range(row_sz):
        for c in range(col_sz):
            escapable_tiles(tbl, results, r, c)

    answer = 0
    for row in results:
        answer += sum(row)
    print(answer)
