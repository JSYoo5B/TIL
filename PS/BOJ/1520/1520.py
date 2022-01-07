#!/usr/bin/env python3

from sys import setrecursionlimit
from sys import stdin
input = lambda : stdin.readline().rstrip()
setrecursionlimit(10**9)

def find_ways(tbl, r, c, memo = None):
    row_sz, col_sz = len(tbl), len(tbl[0])
    if memo == None:
        memo = [ [ -1 for _ in range(col_sz) ] for _ in range(row_sz) ]

    if r == row_sz - 1 and c == col_sz - 1:
        memo[r][c] = 1
    if memo[r][c] > -1:
        return memo[r][c]

    memo[r][c] = 0
    for n_r, n_c in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
        if n_r in [-1, row_sz] or n_c in [-1, col_sz]:
            continue
        if tbl[r][c] > tbl[n_r][n_c]:
            memo[r][c] += find_ways(tbl, n_r, n_c, memo)
    
    return memo[r][c]


if __name__ == '__main__':
    row_sz, col_sz = map(int, input().split())
    tbl = []
    for _ in range(row_sz):
        row = list(map(int, input().split()))
        tbl.append(row)

    answer = find_ways(tbl, 0, 0)
    print(answer)
