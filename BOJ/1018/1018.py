#!/usr/bin/env python3

if __name__ == '__main__':
    # Get user input
    N, M = map(int, input().split())
    board = []
    for i in range(0, N):
        line = input()
        board.append(line)
    
    answer = 8*8
    for n in range(0, N-7):
        for m in range(0, M-7):
            count = 0
            for y in range(n, n+8):
                for x in range(m, m+8):
                    if board[y][x] == 'B' and (y+x)%2 == 0:
                        count += 1
                    elif board[y][x] == 'W' and (y+x)%2 == 1:
                        count += 1
            answer = min(answer, count, 64-count)
    
    print(answer)
