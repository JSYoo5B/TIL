#!/usr/bin/env python3

from collections import deque
import sys

input = sys.stdin.readline

[UP, LEFT, DOWN, RIGHT] = [ i for i in range(4) ]
diffs = [ [-1, 0], [0, -1], [1, 0], [0, 1] ]


if __name__ == '__main__':
    tbl_size = int(input())
    apple_cnt = int(input())
    tbl = [ [ 0 for _ in range(tbl_size) ] for _ in range(tbl_size) ]
    for _ in range(apple_cnt):
        r, c = map(int, input().split())
        tbl[r-1][c-1] = 1
    direction_cnt = int(input())
    directions = []
    for _ in range(direction_cnt):
        t, change = input().split()
        directions.append([int(t), change])
    directions.sort()
    directions.reverse()

    snake = deque([[0, 0]])
    snake_dir = RIGHT
    elapsed = 1
    while True:
        [n_r, n_c] = [snake[-1][0] + diffs[snake_dir][0], \
                snake[-1][1] + diffs[snake_dir][1] ]
        if 0 > n_r or n_r >= tbl_size or 0 > n_c or n_c >= tbl_size:
            break
        elif [n_r, n_c] in snake:
            break
        
        snake.append([n_r, n_c])
        if tbl[n_r][n_c] == 1:
            tbl[n_r][n_c] = 0
        else:
            snake.popleft()

        if len(directions) > 0 and directions[-1][0] == elapsed:
            if directions[-1][1] == 'L':
                snake_dir += 1
                snake_dir %= 4
            else:
                snake_dir += 3
                snake_dir %= 4
            directions.pop()
        elapsed += 1
    print(elapsed)

