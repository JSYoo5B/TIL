#!/usr/bin/env python3

unit_sz, fill_sz, margin_sz = 3, 1, 1

def is_fill_space(r, c):
    global unit_sz, fill_sz, margin_sz
    left, right = margin_sz, fill_sz + margin_sz
    return left <= r < right and left <= c < right


def draw_plane(r, c, lvl):
    global unit_sz, fill_sz, margin_sz
    cur_unit = unit_sz ** lvl
    
    if lvl <= 0 and is_fill_space(r, c):
        return 1
    elif lvl <= 0:
        return 0

    cur_r, cur_c = r // cur_unit, c // cur_unit
    if is_fill_space(cur_r, cur_c):
        return 1
    else:
        return draw_plane(r % cur_unit, c % cur_unit, lvl-1)


if __name__ == '__main__':
    elapsed, unit_sz, fill_sz, \
            r1, r2, c1, c2 = map(int, input().split())
    margin_sz = (unit_sz - fill_sz) // 2
    width, height = c2 - c1, r2 - r1

    tbl = []
    for r in range(height+1):
        line = ''
        for c in range(width+1):
            val = draw_plane(r+r1, c+c1, elapsed - 1)
            line += str(val)
        tbl.append(line)

    for l in tbl:
        print(l)
