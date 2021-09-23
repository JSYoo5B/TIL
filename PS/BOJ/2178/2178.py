#!/usr/bin/env python3

from collections import deque

def find_path(graph):
    que = deque([ [0, 0, 1] ])
    visited = [ [0, 0] ]
    row_cnt, col_cnt = len(graph), len(graph[0])
    while len(que) > 0:
        next = que.popleft()
        r, c, dist = next[0], next[1], next[2]
        if r + 1 == row_cnt and c + 1 == col_cnt:
            return dist
        avails = []
        avails.append([r-1, c, dist+1])
        avails.append([r, c-1, dist+1])
        avails.append([r+1, c, dist+1])
        avails.append([r, c+1, dist+1])
        for a in avails:
            if 0 <= a[0] < row_cnt and 0 <= a[1] < col_cnt \
                    and graph[a[0]][a[1]] == 1 \
                    and a[0:2] not in visited:
                que.append(a)
                visited.append(a[0:2])


if __name__ == '__main__':
    row_cnt, col_cnt = map(int, input().split())
    graph = []
    for _ in range(row_cnt):
        row = input()
        graph.append([ int(i) for i in row ])

    answer = find_path(graph)
    print(answer)
