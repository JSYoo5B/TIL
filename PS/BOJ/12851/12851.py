#!/usr/bin/env python3

from collections import deque

def traverse(start, end):
    q = deque([[start, 0]])
    visited = {start:3}
    cnt_solutions = 0
    fastest_step = 100001
    while len(q) > 0:
        status = q.popleft()
        pos, step = status[0], status[1]
        if pos == end and fastest_step >= step:
            cnt_solutions += 1
            fastest_step = step
        if fastest_step < 100001:
            continue
        if pos >= 0 and visited.get(pos-1, 0) < 10:
            q.append([pos-1, step+1])
            visited[pos-1] = visited.get(pos-1, 0) + 1
        if pos <= 100000 and visited.get(pos+1, 0) < 10:
            q.append([pos+1, step+1])
            visited[pos+1] = visited.get(pos+1, 0) + 1
        if pos <= 50000 and visited.get(pos*2, 0) < 10:
            q.append([pos*2, step+1])
            visited[pos*2] = visited.get(pos*2, 0) + 1
    return fastest_step, cnt_solutions

if __name__ == '__main__':
    start, end = map(int, input().split())
    step, cnt_sols = traverse(start, end)
    print(step)
    print(cnt_sols)
