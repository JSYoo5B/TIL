#!/usr/bin/env python3
from collections import deque

def dfs(edges, node_cnt, start):
    visited = [start]
    stack = [start]
    while len(stack) > 0:
        top = stack[-1]
        deeper = False
        for i in range(node_cnt + 1):
            if edges[top][i] == 1 and i not in visited:
                visited.append(i)
                stack.append(i)
                deeper = True
                break
        if deeper:
            continue
        stack.pop()
    return visited

def bfs(edges, node_cnt, start):
    visited = [start]
    que = deque([start])
    while len(que) > 0:
        current = que.popleft()
        for i in range(node_cnt + 1):
            if edges[current][i] == 1 and i not in visited:
                visited.append(i)
                que.append(i)
    return visited

if __name__ == '__main__':
    node_cnt, edge_cnt, start = map(int, input().split())
    edges = [ [ 0 for _ in range(node_cnt + 1) ] for _ in range(node_cnt + 1) ]
    for _ in range(edge_cnt):
        node1, node2 = map(int, input().split())
        edges[node1][node2] = 1
        edges[node2][node1] = 1
    
    dfs_order = dfs(edges, node_cnt, start)
    bfs_order = bfs(edges, node_cnt, start)
    print(*dfs_order)
    print(*bfs_order)
