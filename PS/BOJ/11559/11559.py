#!/usr/bin/env python3

from collections import deque

def find_neighbors(table, pos):
    row_cnt, col_cnt = len(table), len(table[0])
    [r, c] = pos
    color = table[r][c]
    visited = [ [r, c] ]
    que = deque([ [r, c] ])
    while len(que) > 0:
        [r, c] = que.popleft()
        for [n_r, n_c] in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
            if 0 > n_r or n_r >= row_cnt \
                    or 0 > n_c or n_c >= col_cnt:
                continue
            if table[n_r][n_c] == color \
                    and [n_r, n_c] not in visited:
                visited.append([n_r, n_c])
                que.append([n_r, n_c])
    return visited

if __name__ == '__main__':
    row_cnt, col_cnt = 12, 6
    game_tbl = []
    for _ in range(row_cnt):
        row = input()
        game_tbl.append(row)

    # Modify game table for easier calc
    game_tbl.reverse()
    game_tbl = list(map(list, zip(*game_tbl)))
    
    explode_cnt = -1
    exploded = True
    while exploded == True:
        explode_cnt += 1
        exploded = False

        # Find neighbors and explode puyos
        visited = [ [ 0 for _ in range(12) ] for _ in range(6) ]
        for r in range(6):
            for c in range(12):
                if visited[r][c] == 1 \
                        or game_tbl[r][c] == '.':
                    continue
                neighs = find_neighbors(game_tbl, [r, c])
                if len(neighs) >= 4:
                    exploded = True
                    for [n_r, n_c] in neighs:
                        game_tbl[n_r][n_c] = '.'
                        visited[n_r][n_c] = 1
        
        # Apply gravity
        next_tbl = []
        for r in range(6):
            new_row = [ game_tbl[r][c] for c in range(12) \
                    if game_tbl[r][c] != '.' ]
            new_row += [ '.' for _ in range(12 - len(new_row)) ]
            next_tbl.append(new_row)
        game_tbl = next_tbl

    print(explode_cnt)
