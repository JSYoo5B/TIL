#!/usr/bin/env python3

from sys import stdin
input = lambda : stdin.readline().rstrip()

TETRIMINOS = [
        [[0, 0], [0, 1], [0, 2], [0, 3]], # I, horizontal
        [[0, 0], [1, 0], [2, 0], [3, 0]], # I, vertical
        [[0, 0], [0, 1], [1, 0], [1, 1]], # O (square)
        [[0, 0], [1, 0], [2, 0], [2, 1]], # L right, up
        [[0, 0], [0, 1], [0, 2], [1, 0]], # L right, right
        [[0, 0], [0, 1], [1, 1], [2, 1]], # L right, down
        [[1, 0], [1, 1], [1, 2], [0, 2]], # L right, left
        [[0, 1], [1, 1], [2, 1], [2, 0]], # L left, up
        [[0, 0], [1, 0], [1, 1], [1, 2]], # L left, right
        [[0, 1], [0, 0], [1, 0], [2, 0]], # L left, down
        [[0, 0], [0, 1], [0, 2], [1, 2]], # L left, left
        [[1, 0], [1, 1], [0, 1], [0, 2]], # S, horizontal
        [[0, 0], [1, 0], [1, 1], [2, 1]], # S, vertical
        [[0, 0], [0, 1], [1, 1], [1, 2]], # Z, horizontal
        [[0, 1], [1, 1], [1, 0], [2, 0]], # Z, vertical
        [[1, 0], [1, 1], [1, 2], [0, 1]], # T, up
        [[0, 0], [1, 0], [2, 0], [1, 1]], # T, right
        [[0, 0], [0, 1], [0, 2], [1, 1]], # T, down
        [[0, 1], [1, 1], [2, 1], [1, 0]], # T, left
    ]


def test_tetriminos():
    for T in TETRIMINOS:
        tbl = [ [ 0 for _ in range(4) ] for _ in range(4) ]
        for r, c in T:
            tbl[r][c] = 1
        for r in tbl:
            print(*r)
        print()


if __name__ == '__main__':
    row_sz, col_sz = map(int, input().split())
    tbl = []
    for _ in range(row_sz):
        row = list(map(int, input().split()))
        tbl.append(row)

    answer = 0
    for r in range(row_sz):
        for c in range(col_sz):
            for T in TETRIMINOS:
                local_sum = 0
                for diff_r, diff_c in T:
                    if r + diff_r >= row_sz or c + diff_c >= col_sz:
                        break
                    local_sum += tbl[r + diff_r][c + diff_c]
                answer = max(local_sum, answer)
    print(answer)
