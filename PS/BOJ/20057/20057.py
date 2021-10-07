#!/usr/bin/env python3

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
next_diffs = [ [-1, 0], [1, 0], [0, -1], [0, 1] ]
scatter_rates = [ 10, 10, 5, 7, 7, 2, 2, 1, 1, 0 ]
scatter_diffs = [ 
        # Up direction
        [ [-1, -1], [-1, 1], [-2, 0], [0, -1], [0, 1], 
            [0, -2], [0, 2], [1, -1], [1, 1], [-1, 0] ],
        # Down direction
        [ [1, -1], [1, 1], [2, 0], [0, -1], [0, 1],
            [0, -2], [0, 2], [-1, -1], [-1, 1], [1, 0] ],
        # Left direction
        [ [-1, -1], [1, -1], [0, -2], [-1, 0], [1, 0],
            [-2, 0], [2, 0], [-1, 1], [1, 1], [0, -1] ],
        # Right direction
        [ [-1, 1], [1, 1], [0, 2], [-1, 0], [1, 0],
            [-2, 0], [2, 0], [-1, -1], [1, -1], [0, 1] ]
        ]


def is_in_sands(pos, sands_size):
    return 0 <= pos[0] < sands_size and 0 <= pos[1] < sands_size


def move(sands, pos, dir):
    sands_size = len(sands)
    move_wasted = 0
    o_r, o_c = pos[0], pos[1]
    origin = sands[o_r][o_c]
    for idx in range(len(scatter_rates)):
        scatter = (origin * scatter_rates[idx]) // 100 if scatter_rates[idx] > 0 else sands[o_r][o_c]
        diff = scatter_diffs[dir][idx]
        scatter_pos = [o_r + diff[0], o_c + diff[1]]
        if is_in_sands(scatter_pos, sands_size):
            s_r, s_c = scatter_pos[0], scatter_pos[1]
            sands[s_r][s_c] += scatter
        else:
            move_wasted += scatter
        sands[o_r][o_c] -= scatter
    return move_wasted            


def tornado(sands):
    sands_size = len(sands)
    wasted = 0

    pos = [sands_size // 2, sands_size // 2]
    dir = UP
    while pos != [0, 0]:
        # Get direction to move and next move position
        r, c = pos[0], pos[1]
        if r <= (sands_size // 2) and r + c == sands_size - 1:
            # From up to left
            dir = LEFT
        elif r <= (sands_size // 2) and r - c == 1:
            # From left to down
            dir = DOWN
        elif r > (sands_size // 2) and r + c == sands_size - 1:
            # From down to right
            dir = RIGHT
        elif r > (sands_size // 2) and r == c:
            # From right to up
            dir = UP
        next_pos = [r + next_diffs[dir][0], c + next_diffs[dir][1]]
        # Move into next position (scatter sands and return wasted sands)
        wasted += move(sands, next_pos, dir)
        pos = next_pos
    return wasted


if __name__ == '__main__':
    sands_size = int(input())
    sands = []
    for _ in range(sands_size):
        row = list(map(int, input().split()))
        sands.append(row)
    
    answer = tornado(sands)
    print(answer)
