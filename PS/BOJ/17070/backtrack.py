#!/usr/bin/env python3

import sys
input = sys.stdin.readline

HOR, DIAG, VER = 0, 1, 2
BLANK_REQS = [
        [ [0, 1] ], # HORIZONTAL
        [ [0, 1], [1, 0], [1, 1] ], #DIAGONAL
        [ [1, 0] ] # VERTICAL
    ]
AVAIL_DIRS = [
    [ HOR, DIAG ],
    [ HOR, VER, DIAG ],
    [ VER, DIAG ]
]
table = []
tbl_size = 0

def get_avail_ways(r, c, dir):
    if r == tbl_size - 1 and dir == VER:
        return 0
    elif c == tbl_size - 1 and dir == HOR:
        return 0
    avail_ways = 0
    for next_dir in AVAIL_DIRS[dir]:
        appliable = True
        c_r, c_c = 0, 0
        for diff in BLANK_REQS[next_dir]:
            c_r, c_c = r + diff[0], c + diff[1]
            if c_r >= tbl_size or c_c >= tbl_size \
                    or table[c_r][c_c] == 1:
                appliable = False
                break
        if appliable == False and dir != DIAG:
            break
        elif appliable == False:
            continue
        if c_r == tbl_size - 1 and c_c == tbl_size -1:
            return 1
        avail_ways += get_avail_ways(c_r, c_c, next_dir)
    return avail_ways

if __name__ == '__main__':
    tbl_size = int(input())
    for _ in range(tbl_size):
        row = list(map(int, input().split()))
        table.append(row)

    if table[-1][-1] == 1:
        answer = 0
    else:
        answer = get_avail_ways(0, 1, HOR)
    print(answer)
