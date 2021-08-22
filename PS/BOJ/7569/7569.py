#!/usr/bin/env python3

from collections import deque

def mature_tomatos(matured, box):
    elapsed = 0
    q = deque()
    for pos in matured:
        q.append([pos, 0])
        box[pos[2]][pos[1]][pos[0]] = 1
    while len(q) > 0:
        tomato_status = q.popleft()
        pos, elapsed = tomato_status[0], tomato_status[1]
        directions = [ [pos[0], pos[1], pos[2]] for i in range(6) ]
        directions[0][0] -= 1 # left
        directions[1][0] += 1 # right
        directions[2][1] -= 1 # up
        directions[3][1] += 1 # down
        directions[4][2] -= 1 # below
        directions[5][2] += 1 # above
        for d in directions:
            if d[0] < 0 or d[1] < 0 or d[2] < 0 \
                    or d[0] >= len(box[0][0]) \
                    or d[1] >= len(box[0]) or d[2] >= len(box):
                continue
            if box[d[2]][d[1]][d[0]] == 0:
                q.append([d, elapsed+1])
                box[d[2]][d[1]][d[0]] = 1
    return elapsed

if __name__ == '__main__':
    width, height, depth = map(int, input().split())
    box = []
    for d in range(depth):
        floor = []
        for i in range(height):
            line = list(map(int, input().split()))
            floor.append(line)
        box.append(floor)
    
    matures = []
    for z in range(depth):
        for y in range(height):
            for x in range(width):
                if box[z][y][x] == 1:
                    matures.append([x, y, z])

    elapsed = mature_tomatos(matures, box)
    for floor in box:
        for l in floor:
            if l.count(0) > 0:
                elapsed = -1
                break;
    print(elapsed)
