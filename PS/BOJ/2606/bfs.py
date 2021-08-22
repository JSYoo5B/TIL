#!/usr/bin/env python3

from collections import deque

def bfs(node, edges, visited):
    q = deque()
    q.append(node)
    visited.append(node)
    while len(q) > 0:
        n = q.popleft()
        for i in range(len(edges)):
            if edges[n][i] == 1 and i not in visited:
                q.append(i)
                visited.append(i)

if __name__ == '__main__':
    node_cnt = int(input())
    edges_cnt = int(input())
    edges = [ [ 0 for i in range(node_cnt + 1) ] for j in range(node_cnt + 1) ]
    for e in range(edges_cnt):
        src, dst = map(int, input().split())
        edges[src][dst] = 1
        edges[dst][src] = 1

    visited = []
    bfs(1, edges, visited)
    answer = len(visited) - 1
    print(answer)
