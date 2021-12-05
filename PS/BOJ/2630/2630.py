#!/usr/bin/env python3

from sys import stdin
input = stdin.readline

def get_colors(tbl, r, c, size):
    if size == 1:
        if tbl[r][c] == 0:
            return 1, 0
        else:
            return 0, 1

    white_cnt, blue_cnt = 0, 0
    size //= 2
    for row in range(2):
        for col in range(2):
            w, b = get_colors(tbl, r + row * size, c + col * size, size)
            white_cnt += w
            blue_cnt += b

    if blue_cnt == 0:
        white_cnt //= 4
    elif white_cnt == 0:
        blue_cnt //= 4

    return white_cnt, blue_cnt


if __name__ == '__main__':
    size = int(input())
    tbl = []
    for _ in range(size):
        row = list(map(int, input().split()))
        tbl.append(row)

    w, b = get_colors(tbl, 0, 0, size)
    print(w)
    print(b)
