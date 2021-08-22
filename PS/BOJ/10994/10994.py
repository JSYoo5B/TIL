#!/usr/bin/env python3

def draw_stars(level, start_x, start_y, table):
    if level == 0:
        return

    length = (level - 1) * 4 + 1
    end_x, end_y = start_x + length, start_y + length

    # Draw lines (for readability, separated row and column drawing)
    for x in range(start_x, end_x):
        # Draw top line
        table[x][start_y] = '*'
        # Draw bottom line
        table[x][end_y-1] = '*'
    
    for y in range(start_y, end_y):
        # Draw left line
        table[start_x][y] = '*'
        # Draw right line
        table[end_x-1][y] = '*'

    # Recurse inner level
    draw_stars(level-1, start_x + 2, start_y + 2, table)


if __name__ == '__main__':
    N = int(input())
    tbl_size = (N - 1) * 4 + 1
    tbl = [ [ ' ' for i in range(tbl_size) ] for i in range(tbl_size) ]

    draw_stars(N, 0, 0, tbl)
    lines = [ ''.join(l) for l in tbl ]
    drawing = '\n'.join(lines)
    print(drawing)
