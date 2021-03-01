#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

def expand_cabbages(id, coord, table):
    table[coord[0]][coord[1]] = id
    # Create movable paths
    movables = [ coord[:] for i in range(4) ]
    movables[0][0] -= 1 # left
    movables[1][0] += 1 # right
    movables[2][1] -= 1 # up
    movables[3][1] += 1 # down
    for p in movables:
        x, y = p[0], p[1]
        if x < 0 or y < 0:
            continue
        if table[x][y] == 1:
            expand_cabbages(id, p, table)

def solve_problem():
    # Get input
    M, N, K = map(int, input().split())
    table = [ [ 0 for n in range(N+2) ] for m in range(M+2) ]
    cabbages = []
    for c in range(K):
        x, y = map(int, input().split())
        cabbages.append([x, y])
        table[x][y] = 1
    
    worm_cnt = 0
    for c in cabbages:
        x, y = c[0], c[1]
        if table[x][y] == 1:
            expand_cabbages(worm_cnt + 2, c, table)
            worm_cnt += 1
    print(worm_cnt)

if __name__ == '__main__':
    test_cases = int(input())
    for t in range(test_cases):
        solve_problem()
