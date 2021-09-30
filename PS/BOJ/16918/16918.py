#!/usr/bin/env python3

import copy

if __name__ == '__main__':
    row_cnt, col_cnt, n = map(int, input().split())
    game_table = []
    for _ in range(row_cnt):
        row_str = input()
        row = [ c for c in row_str ]
        game_table.append(row)

    if n == 1:
        for row in game_table:
            print(''.join(row))
    elif n % 2 == 0:
        full_row = [ 'O' for _ in range(col_cnt) ]
        for _ in range(row_cnt):
            print(''.join(full_row))
    else:
        while True:
            bomb_pos = []
            for r in range(row_cnt):
                for c in range(col_cnt):
                    if game_table[r][c] == 'O':
                        bomb_pos.append([r, c])
                    game_table[r][c] = '.' if game_table[r][c] == 'O' else 'O'
            explode_pos = []
            for pos in bomb_pos:
                r, c = pos[0], pos[1]
                explode_pos += [ [r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1] ]
            for pos in explode_pos:
                p_r, p_c = pos[0], pos[1]
                if 0 <= p_r < row_cnt and 0 <= p_c < col_cnt:
                    game_table[p_r][p_c] = '.'
            if n % 4 == 3:
                break
            else:
                n = 3
 
        for row in game_table:
            print(''.join(row))
 
