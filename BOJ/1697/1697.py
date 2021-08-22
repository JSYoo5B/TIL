#!/usr/bin/env python3

from collections import deque

def traverse(start, end):
    q = deque([[start, 0]])
    visited = {start}
    while len(q) > 0:
        status = q.popleft()
        pos, step = status[0], status[1]
        if pos == end:
            return step
        if pos >= 0 and pos-1 not in visited:
            q.append([pos-1, step+1])
            visited.add(pos-1)
        if pos <= 100000 and pos+1 not in visited:
            q.append([pos+1, step+1])
            visited.add(pos+1)
        if pos <= 50000 and pos*2 not in visited:
            q.append([pos*2, step+1])
            visited.add(pos*2)

if __name__ == '__main__':
    start, end = map(int, input().split())
    answer = traverse(start, end)
    print(answer)
