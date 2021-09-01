#!/usr/bin/env python3

from collections import deque

def traverse(start, end):
    q = deque([start])
    visited = [ -1 for _ in range(100001) ]
    visited[start] = 0
    while len(q) > 0:
        pos = q.popleft()
        step = visited[pos]
        if pos == end:
            return step
        if pos * 2 <= 100000 and visited[pos * 2] == -1:
            q.appendleft(pos * 2)
            visited[pos * 2] = step
        if pos - 1 >= 0 and visited[pos - 1] == -1:
            q.append(pos - 1)
            visited[pos - 1] = step + 1
        if pos + 1 <= 100000 and visited[pos + 1] == -1:
            q.append(pos + 1)
            visited[pos + 1] = step + 1

if __name__ == '__main__':
    start, end = map(int, input().split())
    answer = traverse(start, end)
    print(answer)
