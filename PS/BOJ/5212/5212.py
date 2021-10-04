#!/usr/bin/env python3

from copy import deepcopy

if __name__ == '__main__':
    row_cnt, col_cnt = map(int, input().split())
    earth_map = []
    earth_map.append([ '.' for _ in range(col_cnt + 2) ])
    for _ in range(row_cnt):
        row_str = input()
        row = ['.']
        row += [ c for c in row_str ]
        row.append('.')
        earth_map.append(row)
    earth_map.append([ '.' for _ in range(col_cnt + 2) ])
    
    new_earth_map = deepcopy(earth_map)
    lt_pos, rb_pos = [row_cnt, col_cnt], [0, 0]
    for r in range(1, row_cnt + 1):
        for c in range(1, col_cnt + 1):
            if earth_map[r][c] == '.':
                continue

            neighbors = [ earth_map[r-1][c], earth_map[r+1][c], \
                    earth_map[r][c-1], earth_map[r][c+1] ]
            if neighbors.count('.') >= 3:
                new_earth_map[r][c] = '.'
            else:
                lt_pos[0] = min(r, lt_pos[0])
                lt_pos[1] = min(c, lt_pos[1])
                rb_pos[0] = max(r, rb_pos[0])
                rb_pos[1] = max(c, rb_pos[1])

    partial_map = ''
    for r in range(lt_pos[0], rb_pos[0] + 1):
        for c in range(lt_pos[1], rb_pos[1] + 1):
            partial_map += new_earth_map[r][c]
        partial_map += '\n'
    print(partial_map)

