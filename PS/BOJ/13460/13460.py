#!/usr/bin/env python3

from collections import deque

def find_step_cnt(table, red, blue, hole):
    visited = [ [red, blue] ]
    que = deque([[red, blue, 0]])
    while len(que) > 0:
        next = que.popleft()
        red_pos, blue_pos, trial = next[0], next[1], next[2]
        if trial >= 10:
            return -1
        for dir in [ [-1, 0], [1, 0], [0, -1], [0, 1] ]:
            next_red, next_blue = tilt_table(table, red_pos, blue_pos, hole, dir)
            if next_blue == hole:
                continue
            if next_red == hole:
                return trial + 1
            if [next_red, next_blue] not in visited:
                visited.append([next_red, next_blue])
                que.append([next_red, next_blue, trial + 1])
    return -1

def tilt_table(table, red_pos, blue_pos, hole, dir):
    row_max = len(table)
    col_max = len(table[0])
    first_ball, second_ball = red_pos, blue_pos
    swap_order = False
    red_order = red_pos[0] * dir[0] + red_pos[1] * dir[1]
    blue_order = blue_pos[0] * dir[0] + blue_pos[1] * dir[1]
    if red_order < blue_order:
        first_ball, second_ball = blue_pos, red_pos
        swap_order = True
    while True:
        next_r, next_c = first_ball[0] + dir[0], first_ball[1] + dir[1]
        if 0 > next_r or next_r >= row_max or 0 > next_c or next_c >= col_max:
            break
        elif next_r == hole[0] and next_c == hole[1]:
            first_ball = hole
            break
        elif next_r == second_ball[0] and next_c == second_ball[1]:
            break
        elif table[next_r][next_c] == '#':
            break
        first_ball = [next_r, next_c]
    while True:
        next_r, next_c = second_ball[0] + dir[0], second_ball[1] + dir[1]
        if 0 > next_r or next_r >= row_max or 0 > next_c or next_c >= col_max:
            break
        elif next_r == hole[0] and next_c == hole[1]:
            second_ball = hole
            break
        elif next_r == first_ball[0] and next_c == first_ball[1]:
            break
        elif table[next_r][next_c] == '#':
            break
        second_ball = [next_r, next_c]
    if swap_order == False:
        return first_ball, second_ball
    else:
        return second_ball, first_ball


if __name__ == '__main__':
    row_cnt, col_cnt = map(int, input().split())
    table = []
    red_pos, blue_pos, hole_pos = [-1, -1], [-1, -1], [-1, -1]
    for r in range(row_cnt):
        row_str = input()
        row = [ c for c in row_str ]
        for c in range(col_cnt):
            if row[c] == 'R':
                red_pos = [r, c]
                row[c] = '.'
            elif row[c] == 'B':
                blue_pos = [r, c]
                row[c] = '.'
            elif row[c] == 'O':
                hole_pos = [r, c]
                row[c] = '.'
        table.append(row)
    answer = find_step_cnt(table, red_pos, blue_pos, hole_pos)    
    print(answer)
