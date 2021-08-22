#!/usr/bin/env python3

from collections import deque

def mature_tomatos(matured, box):
    elapsed = 0
    q = deque()
    for pos in matured:
        q.append([pos, 0])
        box[pos[1]][pos[0]] = 1
    while len(q) > 0:
        tomato_status = q.popleft()
        pos, elapsed = tomato_status[0], tomato_status[1]
        directions = [ [pos[0], pos[1]] for i in range(4) ]
        directions[0][0] -= 1 # left
        directions[1][0] += 1 # right
        directions[2][1] -= 1 # up
        directions[3][1] += 1 # down
        for d in directions:
            if d[0] < 0 or d[1] < 0 or d[0] >= len(box[0]) or d[1] >= len(box):
                continue
            if box[d[1]][d[0]] == 0:
                q.append([d, elapsed+1])
                box[d[1]][d[0]] = 1
    return elapsed

if __name__ == '__main__':
    width, height = map(int, input().split())
    box = []
    for i in range(height):
        line = list(map(int, input().split()))
        box.append(line)
    
    matures = []
    for y in range(height):
        for x in range(width):
            if box[y][x] == 1:
                matures.append([x, y])

    elapsed = mature_tomatos(matures, box)
    for l in box:
        if l.count(0) > 0:
            elapsed = -1
    print(elapsed)
