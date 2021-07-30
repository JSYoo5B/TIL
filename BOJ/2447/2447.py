#!/usr/bin/env python3

def get_character(x, y, N, memo):
    # Use memo first
    if memo[x][y] != None:
        return memo[x][y]

    N //= 3
    if N == 1:
        # On lowest level, follow default pattern
        if x % 3 == 1 and y % 3 == 1:
            memo[x][y] = ' '
            return ' '
        else:
            memo[x][y] = '*'
            return '*'
    elif x//N == 1 and y//N == 1:
        # Center of current levels are blank
        memo[x][y] = ' '
        return ' '
    else:
        # When current grid isn't center, reduce
        memo[x][y] = get_character(x%N, y%N, N, memo)
        return memo[x][y]


if __name__ == '__main__':
    N = int(input())
    memo = [ [None for i in range(N) ] for j in range(N) ]

    for x in range(0, N):
        for y in range(0, N):
            ch = get_character(x, y, N, memo)
            print(ch, end='')
        print()

