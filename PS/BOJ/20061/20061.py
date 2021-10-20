#!/usr/bin/env python3

from collections import deque
import sys
input = sys.stdin.readline

def start_drops(board, blocks):
    score = 0
    for b in blocks:
        # Stack blocks
        [type, c] = b
        board.append([ 1 for _ in range(4) ])
        for below in range(2, 7):
            # Go down when below cells are blank
            if type == 2 and board[below][c] == 0 and board[below][c+1] == 0:
                continue
            elif type != 2 and board[below][c] == 0:
                continue

            # otherwise, stack it
            board[below-1][c] = 1
            if type == 2:
                board[below-1][c+1] = 1
            elif type == 3:
                board[below-2][c] = 1
            break
        board.pop()
        
        # Check the complete row, score it
        row = -1
        while row >= -4:
            if sum(board[row]) < 4:
                row -= 1
                continue
            score += 1
            del board[row]
            board.appendleft([ 0 for _ in range(4) ])
        # When the buffered row has value, push down
        while sum(board[1]) > 0:
            board.pop()
            board.appendleft([ 0 for _ in range(4) ])
    return score


if __name__ == '__main__':
    cnt_blocks = int(input())
    g_blocks, b_blocks = [], []
    for _ in range(cnt_blocks):
        blk_type, r, c = map(int, input().split())
        g_blocks.append([blk_type, c])
        if blk_type == 2:
            blk_type = 3
        elif blk_type == 3:
            blk_type = 2
        b_blocks.append([blk_type, r])

    g_board = deque([ [ 0 for _ in range(4) ] for _ in range(6) ])
    b_board = deque([ [ 0 for _ in range(4) ] for _ in range(6) ])
    score = 0
    score += start_drops(g_board, g_blocks)
    score += start_drops(b_board, b_blocks)
    
    blk_cnt = 0
    blk_cnt += sum([ sum(b_row) for b_row in b_board ])
    blk_cnt += sum([ sum(g_row) for g_row in g_board ])

    print(score)
    print(blk_cnt)
