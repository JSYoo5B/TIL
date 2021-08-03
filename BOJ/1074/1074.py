#!/usr/bin/env python3

def get_cell_number(level, prefix, row, col):
    # On final level, return by z figure
    if level == 1:
        return prefix + row * 2 + col

    # Divide current square into 2x2 and find quadrant
    divisor = 2 ** (level-1)
    div_row, div_col = row // divisor, col // divisor
    # Get z figure order, add prefix with square size
    z_order = div_row * 2 + div_col
    prefix += (divisor ** 2) * z_order
    # Call smaller problem
    return get_cell_number(level-1, prefix, row % divisor, col % divisor)


if __name__ == '__main__':
    N, r, c = map(int, input().split())

    answer = get_cell_number(N, 0, r, c)
    print(answer)
