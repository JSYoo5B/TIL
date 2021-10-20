#!/usr/bin/env python3

from copy import deepcopy
from collections import deque

RAINBOW, BLACK = 0, -1
BLANK = ' '

def get_blk_group(table, start_pos):
    color = table[start_pos[0]][start_pos[1]]
    tbl_size = len(table)

    blk_group = [start_pos]
    que = deque([start_pos])
    while len(que) > 0:
        [r, c] = que.popleft()
        neighbors = [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]
        for [n_r, n_c] in neighbors:
            if 0 > n_r or n_r >= tbl_size \
                    or 0 > n_c or n_c >= tbl_size:
                continue
            if table[n_r][n_c] in (RAINBOW, color) \
                    and [n_r, n_c] not in blk_group:
                blk_group.append([n_r, n_c])
                que.append([n_r, n_c])
    return blk_group


def count_rainbows(table, blk_group):
    cells = [ table[r][c] for [r, c] in blk_group ]
    return cells.count(RAINBOW)


def remove_blk_group(table, blk_group):
    for [r, c] in blk_group:
        table[r][c] = BLANK


def apply_gravity(table):
    tbl_size = len(table)
    for c in range(tbl_size):
        base = tbl_size
        while base > 0:
            base -= 1
            if table[base][c] != BLANK:
                continue
            skip_r = base
            for top in range(base-1, -1, -1):
                if table[top][c] == BLACK:
                    skip_r = top
                    break
                elif table[top][c] != BLANK:
                    table[base][c] = table[top][c]
                    table[top][c] = BLANK
                    break
            base = skip_r


def rotate_table(table):
    transpose = [ list(e) for e in zip(*table) ]
    transpose.reverse()
    return transpose


if __name__ == '__main__':
    tbl_size, color_cnt = map(int, input().split())
    table = []
    for _ in range(tbl_size):
        row = list(map(int, input().split()))
        table.append(row)

    score = 0
    while True:
        # Search group to delete
        max_blk_len = 0
        max_rainbow_cnt = 0
        target_grp = []
        visited = [ [ 0 for _ in range(tbl_size) ] for _ in range(tbl_size) ]
        for r in range(tbl_size):
            for c in range(tbl_size):
                # Skip non colored cell, visited cells
                if table[r][c] in (RAINBOW, BLACK, BLANK) \
                        or visited[r][c] == 1:
                    continue

                # Get group
                blk_group = get_blk_group(table, [r, c])
                # Anyway, set group cells as visited
                for [c_r, c_c] in blk_group:
                    visited[c_r][c_c] = 1
                # Skip when group were not found (has 1 cell for group)
                if len(blk_group) == 1:
                    continue

                if len(blk_group) > max_blk_len:
                    target_grp = blk_group
                    max_blk_len = len(target_grp)
                    max_rainbow_cnt = count_rainbows(table, target_grp)
                elif len(blk_group) == max_blk_len \
                        and count_rainbows(table, blk_group) >= max_rainbow_cnt:
                    target_grp = blk_group
                    max_blk_len = len(target_grp)
                    max_rainbow_cnt = count_rainbows(table, target_grp)
        # When no any group were found, 
        if max_blk_len == 0:
            break

        # Remove blocks and apply score
        score += max_blk_len ** 2
        remove_blk_group(table, target_grp)
        # Apply gravity, rotate, and apply again
        apply_gravity(table)
        table = rotate_table(table)
        apply_gravity(table)

    print(score)
