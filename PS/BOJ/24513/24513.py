#!/usr/bin/env python3

from sys import stdin
input = lambda : stdin.readline().rstrip()


def spread_virus(tbl, viruses):
    row_sz, col_sz = len(tbl), len(tbl[0])
    next_spreads = set()
    for r, c in viruses:
        for n_r, n_c in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
            if 0 > n_r or n_r >= row_sz or 0 > n_c or n_c >= col_sz:
                continue
            if (n_r, n_c) not in next_spreads and tbl[n_r][n_c] == 0:
                next_spreads.add((n_r, n_c))
    return next_spreads


if __name__ == '__main__':
    row_sz, col_sz = map(int, input().split())
    tbl = []
    unos, duos = set(), set()
    for r in range(row_sz):
        line = list(map(int, input().split()))
        for c in range(col_sz):
            if line[c] == 1:
                unos.add((r, c))
            elif line[c] == 2:
                duos.add((r, c))
        tbl.append(line)

    uno_cnt, duo_cnt, trio_cnt = len(unos), len(duos), 0
    while len(unos) > 0 or len(duos) > 0:
        unos = spread_virus(tbl, unos)
        duos = spread_virus(tbl, duos)

        trios = unos & duos
        unos = unos - trios
        duos = duos - trios
        for (r, c) in unos:
            tbl[r][c] = 1
        uno_cnt += len(unos)
        for (r, c) in duos:
            tbl[r][c] = 2
        duo_cnt += len(duos)
        for (r, c) in trios:
            tbl[r][c] = 3
        trio_cnt += len(trios)
    print(uno_cnt, duo_cnt, trio_cnt)
