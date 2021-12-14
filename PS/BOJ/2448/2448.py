#!/usr/bin/env python3

from math import log

def draw_star(r, c, n, memo = []):
    if len(memo) == 0:
        memo = [ [ ' ' for _ in range(n*2) ] for _ in range(n) ]
        return draw_star(r, c, n, memo)

    if n == 3:
        memo[r][c] = '*'
        memo[r+1][c-1] = memo[r+1][c+1] = '*'
        memo[r+2][c-2] = memo[r+2][c-1] = '*'
        memo[r+2][c] = memo[r+2][c+1] = memo[r+2][c+2] = '*'
        return memo

    n_2 = n // 2
    draw_star(r, c, n_2, memo)
    draw_star(r+n_2, c-n_2, n_2, memo)
    draw_star(r+n_2, c+n_2, n_2, memo)
    return memo


if __name__ == '__main__':
    N = int(input())
    lines = draw_star(0, N-1, N)
    
    triangle = ''
    for l in lines:
        line = ''.join(l)
        triangle += line + '\n'

    print(triangle)
