#!/usr/bin/env python3

UP, DOWN, RIGHT, LEFT = 1, 2, 3, 4
diffs = [ [-1, 0], [1, 0], [0, 1], [0, -1] ]


class shark:
    def __init__(self, pos, speed, dir, size):
        self.pos = pos
        self.speed = speed
        self.dir = dir
        self.size = size

    def move(self, map_size):
        row_max, col_max = map_size[0], map_size[1]
        diff = diffs[self.dir - 1]
        diff = [diff[0] * self.speed, diff[1] * self.speed]
        next_pos = [self.pos[0] + diff[0], self.pos[1] + diff[1]]
        while not (0 < next_pos[0] <= row_max and 0 < next_pos[1] <= col_max):
            if self.dir == UP and next_pos[0] < 1:
                next_pos[0] *= -1
                next_pos[0] += 2    # negate skipped r == 0, -1
                self.dir = DOWN
            elif self.dir == DOWN and next_pos[0] > row_max:
                next_pos[0] = row_max * 2 - next_pos[0]
                self.dir = UP
            elif self.dir == LEFT and next_pos[1] < 1:
                next_pos[1] *= -1
                next_pos[1] += 2    # negate skippedn c == 0, -1
                self.dir = RIGHT
            elif self.dir == RIGHT and next_pos[1] > col_max:
                next_pos[1] = col_max * 2 - next_pos[1]
                self.dir = LEFT
        self.pos = next_pos


if __name__ == '__main__':
    row_cnt, col_cnt, shark_cnt = map(int, input().split())
    sharks = []
    for _ in range(shark_cnt):
        r, c, speed, dir, size = map(int, input().split())
        shk = shark([r, c], speed, dir, size)
        sharks.append(shk)

    total_caught_size = 0
    for fisher_pos in range(1, col_cnt + 1):
        # Fisher catches sharks
        c = -1
        for s in range(len(sharks)):
            if sharks[s].pos[1] == fisher_pos:
                if c == -1:
                    c = s
                elif sharks[c].pos[0] > sharks[s].pos[0]:
                    c = s
        
        if c != -1:
            s = sharks[c]
            total_caught_size += s.size
            del sharks[c]

        # Sharks moves
        status = [ [ -1 for _ in range(col_cnt + 1) ] \
                for _ in range(row_cnt + 1) ]
        for i in range(len(sharks)):
            sharks[i].move([row_cnt, col_cnt])
            r, c = sharks[i].pos[0], sharks[i].pos[1]
            if status[r][c] == -1:
                status[r][c] = i
            else:
                other = status[r][c]
                if sharks[i].size > sharks[other].size:
                    status[r][c] = i
            
        remains = []
        for r in status:
            remaining = [ i for i in r if i >= 0 ]
            remains += remaining
        sharks = [ sharks[i] for i in remains ]
        
    print(total_caught_size)
