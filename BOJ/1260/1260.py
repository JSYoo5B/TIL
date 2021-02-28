#!/usr/bin/env python3

from collections import deque

def DFS(start, edges, visited):
    visited.append(start)
    for i in range(len(edges)):
        if edges[start][i] == 1 and i not in visited:
            DFS(i, edges, visited)

def BFS(start, edges, visited):
    visited.append(start)
    q = deque()
    q.append(start)
    while len(visited) < len(edges):
        if len(q) == 0:
            break
        node = q.popleft()
        for i in range(len(edges)):
            if edges[node][i] == 1 and i not in visited:
                visited.append(i)
                q.append(i)

if __name__ == '__main__':
    node, edge, start = map(int, input().split())
    # Create edge table
    edges = [ [ 0 for i in range(node + 1) ] for i in range(node + 1) ]
    # Update edge list
    for e in range(edge):
        src, dst = map(int, input().split())
        edges[src][dst] = 1
        edges[dst][src] = 1
    
    dfs_order, bfs_order = [], []
    DFS(start, edges, dfs_order)
    BFS(start, edges, bfs_order)

    print(' '.join(str(n) for n in dfs_order))
    print(' '.join(str(n) for n in bfs_order))
