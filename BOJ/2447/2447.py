#!/usr/bin/env python3

def get_character(x, y, N):
    N //= 3
    if N == 1:
        # On lowest level, follow default pattern
        if x % 3 == 1 and y % 3 == 1:
            return ' '
        else:
            return '*'
    elif x//N == 1 and y//N == 1:
        # Center of current levels are blank
        return ' '
    else:
        # When current grid isn't center, reduce
        return get_character(x%N, y%N, N)


if __name__ == '__main__':
    N = int(input())

    for x in range(0, N):
        for y in range(0, N):
            ch = get_character(x, y, N)
            print(ch, end='')
        print()
