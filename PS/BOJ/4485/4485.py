#!/usr/bin/env python3

from heapq import heappush, heappop
from sys import stdin
input = stdin.readline
INF = 10 ** 9

def get_min_cost(tbl):
    tbl_size = len(tbl)
    dists = [ [ INF for _ in range(tbl_size) ] for _ in range(tbl_size) ]
    heap = [ [tbl[0][0], [0, 0]] ]
    while len(heap) > 0:
        [dist, [r, c]] = heappop(heap)
        dists[r][c] = min(dists[r][c], dist)
        for n_r, n_c in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
            if 0 > n_r or n_r >= tbl_size or 0 > n_c or n_c >= tbl_size:
                continue
            d = tbl[n_r][n_c]
            if dist + d < dists[n_r][n_c]:
                dists[n_r][n_c] = dist + d
                heappush(heap, [dists[n_r][n_c], [n_r, n_c]])
    return dists[-1][-1]


if __name__ == '__main__':
    prob_id = 1
    while True:
        tbl_size = int(input())
        if tbl_size == 0:
            break
        tbl = []
        for _ in range(tbl_size):
            row = list(map(int, input().split()))
            tbl.append(row)

        answer = get_min_cost(tbl)
        print("Problem {}: {}".format(prob_id, answer))
        prob_id += 1
