#!/usr/bin/env python3

UP_UNAVAIL, UP_AVAIL, RIGHT_UNAVAIL, RIGHT_AVAIL = 0, 1, 2, 3


if __name__ == '__main__':
    row_sz, col_sz = map(int, input().split())

    ways = [ [ [0, 0, 0, 0] for _ in range(col_sz) ] for _ in range(row_sz) ]
    for r in range(1, row_sz):
        ways[r][0][UP_AVAIL] = 1
    for c in range(1, col_sz):
        ways[0][c][RIGHT_AVAIL] = 1

    for r in range(1, row_sz):
        for c in range(1, col_sz):
            ways[r][c][UP_UNAVAIL] = ways[r-1][c][RIGHT_AVAIL]
            ways[r][c][RIGHT_UNAVAIL] = ways[r][c-1][UP_AVAIL]
            ways[r][c][UP_AVAIL] = ways[r-1][c][UP_UNAVAIL] + ways[r-1][c][UP_AVAIL]
            ways[r][c][RIGHT_AVAIL] = ways[r][c-1][RIGHT_UNAVAIL] + ways[r][c-1][RIGHT_AVAIL]

    answer = sum(ways[-1][-1])
    answer %= 100000
    print(answer)
