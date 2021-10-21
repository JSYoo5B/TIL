#!/usr/bin/env python3

from collections import deque

import sys
input = sys.stdin.readline

UP, DOWN, LEFT, RIGHT = 1, 2, 3, 4
DIFFS = [ [-1, 0], [1, 0], [0, -1], [0, 1] ]


def blizzard(table, dir, length):
    table_size = len(table)
    mid = table_size // 2
    [d_r, d_c] = DIFFS[dir - 1]
    ice_poses = [ [mid + d_r * (i+1), mid + d_c * (i+1)] for i in range(length) ]
    for [i_r, i_c] in ice_poses:
        table[i_r][i_c] = 0

def shrink_marbles(table, stats):
    table_size = len(table)
    marbles = []
    [r, c] = [table_size // 2, table_size // 2]
    while r >= 0 and c >= 0:
        # Skip for zeros
        if table[r][c] == 0:
            pass
        # Add marbles when it's empty
        elif len(marbles) == 0:
            marbles.append([table[r][c], 1])
        elif marbles[-1][0] == table[r][c]:
            marbles[-1][1] += 1
        else:
            marbles.append([table[r][c], 1])
        [r, c] = get_next_pos(table_size, r, c)
    
    while True:
        explodes = [ m for m in marbles if m[1] >= 4 ]
        if len(explodes) == 0:
            break
        for color, cnt in explodes:
            stats[color - 1] += cnt
        rest = [ m for m in marbles if m[1] < 4 ]
        marbles = []
        for r in rest:
            if len(marbles) == 0 or marbles[-1][0] != r[0]:
                marbles.append(r)
            else:
                marbles[-1][1] += r[1]

    return marbles


def place_marbles(table_size, marbles):
    table = [ [ 0 for _ in range(table_size) ] for _ in range(table_size) ]
    [r, c] = [table_size // 2, table_size // 2 - 1]
    marbles.reverse()
    while r >= 0 and c >= 0:
        if len(marbles) > 0:
            last = marbles.pop()
            table[r][c] = last[1]
            [r, c] = get_next_pos(table_size, r, c)
            table[r][c] = last[0]
            [r, c] = get_next_pos(table_size, r, c)
            continue
        else:
            break
    return table


def get_next_pos(table_size, r, c):
    mid = table_size // 2
    if r <= mid and c >= r and r + c < table_size:
        # LEFT
        c -= 1
    elif c < mid and r - c >= 1  and r + c < table_size - 1:
        # DOWN
        r += 1
    elif r > mid and r + c >= table_size - 1 and r - c > 0:
        # RIGHT
        c += 1
    else:
        # UP
        r -= 1
    return [r, c]


if __name__ == '__main__':
    table_size, op_cnt = map(int, input().split())
    table = []
    for _ in range(table_size):
        row = list(map(int, input().split()))
        table.append(row)
    operations = []
    for _ in range(op_cnt):
        operation = list(map(int, input().split()))
        operations.append(operation)

    stats = [0, 0, 0]
    for [dir, length] in operations:
        # Start blizzard
        blizzard(table, dir, length)

        # Shift bubbles, explode neighbors, and convert into new marbles
        marbles = shrink_marbles(table, stats)
        # Place converted marbles into table
        table = place_marbles(table_size, marbles)
    answer = stats[0] + stats[1] * 2 + stats[2] * 3
    print(answer)
