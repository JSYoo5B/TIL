#!/usr/bin/env python3

import sys
from collections import deque
import copy

input = sys.stdin.readline

def firestorm(ice_board, board_size, level):
    # split grids
    for r in range(1, board_size, 2 ** level):
        for c in range(1, board_size, 2 ** level):
            spin_grids(ice_board, [r, c], level)
    
    # melt ices
    melted_board = copy.deepcopy(ice_board)
    for r in range(1, board_size + 1):
        for c in range(1, board_size + 1):
            neighbors = [ ice_board[r-1][c], ice_board[r+1][c], \
                    ice_board[r][c-1], ice_board[r][c+1] ]
            if neighbors.count(0) > 1 and ice_board[r][c] > 0:
                melted_board[r][c] -= 1
    return melted_board

def spin_grids(ice_board, start_pos, level):
    if level < 1:
        return
    for r in range(2 ** (level - 1)):
        for c in range(2 ** (level - 1)):
            tl = [start_pos[0] + r, start_pos[1] + c]
            tr = [start_pos[0] + c, start_pos[1] + 2 ** level - 1 - r] 
            bl = [start_pos[0] + 2 ** level - 1 - c, start_pos[1] + r]
            br = [start_pos[0] + 2 ** level - 1 - r, start_pos[1] + 2 ** level - 1 - c]
            ices = [ ice_board[p[0]][p[1]] for p in [tl, tr, br, bl] ]
            ice_board[tl[0]][tl[1]] = ices[3]
            ice_board[tr[0]][tr[1]] = ices[0]
            ice_board[br[0]][br[1]] = ices[1]
            ice_board[bl[0]][bl[1]] = ices[2]


def get_max_ice_bundle_size(ice_board, board_size):
    max_size = 0
    for r in range(board_size):
        for c in range(board_size):
            if ice_board[r][c] == 0:
                continue
            bundle_size = get_ice_bundle_size(ice_board, [r, c])
            if bundle_size > max_size:
                max_size = bundle_size
    return max_size


def get_ice_bundle_size(ice_board, pos):
    bundle_size = 1
    ice_board[pos[0]][pos[1]] = 0
    que = deque([pos])
    while len(que) > 0:
        pos = que.popleft()
        r, c = pos[0], pos[1]
        neighbors = [ [r-1, c], [r+1, c], [r, c-1], [r, c+1] ]
        for p in neighbors:
            if ice_board[p[0]][p[1]] > 0:
                ice_board[p[0]][p[1]] = 0
                bundle_size += 1
                que.append(p)
    return bundle_size


if __name__ == '__main__':
    N, Q = map(int, input().split())
    board_size = 2 ** N
    ice_board = []
    ice_board.append([ 0 for _ in range(board_size + 2) ])
    for _ in range(board_size):
        row = list(map(int, input().split()))
        ice_board.append([0] + row + [0])
    ice_board.append([ 0 for _ in range(board_size + 2) ])
    fs_orders = list(map(int, input().split()))

    for lvl in fs_orders:
        ice_board = firestorm(ice_board, board_size, lvl)
    
    ice_sum = 0
    for row in ice_board:
        ice_sum += sum(row)
    max_bundle_size = get_max_ice_bundle_size(ice_board, board_size)

    print(ice_sum)
    print(max_bundle_size)
