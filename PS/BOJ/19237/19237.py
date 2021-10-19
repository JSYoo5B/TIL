#!/usr/bin/env python3

import sys

input = sys.stdin.readline

UP, DOWN, LEFT, RIGHT = 1, 2, 3, 4

def move(pos, dir):
    new_pos = [pos[0], pos[1]]
    if dir == UP:
        new_pos[0] -= 1
    elif dir == DOWN:
        new_pos[0] += 1
    elif dir == LEFT:
        new_pos[1] -= 1
    elif dir == RIGHT:
        new_pos[1] += 1
    return new_pos


class shark:
    def __init__(self):
        self.id = -1
        self.pos = [-1, -1]
        self.dir = -1
        self.prefers = []
    
    def move(self, smell_table):
        world_size = len(smell_table)
        [r, c] = self.pos
        current_prefer = self.prefers[self.dir - 1]
        # Try to move non-smelling cell
        next_pos = self.pos
        for dir in current_prefer:
            [n_r, n_c] = move([r, c], dir)
            if 0 > n_r or n_r >= world_size \
                    or 0 > n_c or n_c >= world_size:
                continue
            smell_cell = smell_table[n_r][n_c]
            if smell_cell[1] == 0:
                next_pos = [n_r, n_c]
                self.dir = dir
                break
        if next_pos == self.pos:
            for dir in current_prefer:
                [n_r, n_c] = move([r, c], dir)
                if 0 > n_r or n_r >= world_size \
                        or 0 > n_c or n_c >= world_size:
                    continue
                smell_cell = smell_table[n_r][n_c]
                if smell_cell[0] == self.id:
                    next_pos = [n_r, n_c]
                    self.dir = dir
                    break
        self.pos = next_pos
        return next_pos
 

if __name__ == '__main__':
    world_size, shark_cnt, smell_duration = map(int, input().split())
    world = []
    smell_table = []
    sharks = [ shark() for _ in range(shark_cnt) ]
    for r in range(world_size):
        row = list(map(int, input().split()))
        smell_row = []
        for c in range(world_size):
            smell_cell = [0, 0]
            if row[c] > 0:
                id = row[c]
                sharks[id-1].id = id
                sharks[id-1].pos = [r, c]
                smell_cell = [id, smell_duration]
            smell_row.append(smell_cell)
        world.append(row)
        smell_table.append(smell_row)

    shark_dirs = list(map(int, input().split()))
    for i in range(shark_cnt):
        sharks[i].dir = shark_dirs[i]
        for _ in range(4):
            pref = list(map(int, input().split()))
            sharks[i].prefers.append(pref)

    elapsed = 0
    sharks.reverse()
    while elapsed <= 1000:
        if len(sharks) == 1:
            break

        # Empty current pos
        for r in range(world_size):
            for c in range(world_size):
                world[r][c] = 0

        # Try to move sharks
        dead_sharks = []
        for s_idx in range(len(sharks)):
            [n_r, n_c] = sharks[s_idx].move(smell_table)
            # When the shark collides, remove greater id shark
            if world[n_r][n_c] != 0:
                dead_sharks.append(world[n_r][n_c])
            world[n_r][n_c] = sharks[s_idx].id
        
        # Remove shark by dead list
        dead_idxs = [ i for i in range(len(sharks)) \
                if sharks[i].id in dead_sharks ]
        dead_idxs.reverse()
        for d in dead_idxs:
            del sharks[d]

        # Put smell for new position
        for s in sharks:
            [r, c] = s.pos
            smell_table[r][c] = [s.id, smell_duration + 1]
        
        # process elapsed time
        elapsed += 1
        for r in range(world_size):
            for c in range(world_size):
                if smell_table[r][c][1] > 0:
                    smell_table[r][c][1] -= 1

    if elapsed > 1000:
        elapsed = -1
    print(elapsed)
