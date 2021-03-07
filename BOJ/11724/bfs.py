#!/usr/bin/env python3

from collections import deque

def bfs(start, edges, visited):
    q = deque([start])
    visited.append(start)
    while len(q) > 0:
        n = q.popleft()
        for i in range(len(edges)):
            if edges[n][i] == 1 and i not in visited:
                q.append(i)
                visited.append(i)

if __name__ == '__main__':
    node_cnt, edge_cnt = map(int, input().split())
    edges = [ [ 0 for i in range(node_cnt+1) ] for j in range(node_cnt+1) ]
    for e in range(edge_cnt):
        src, dst = map(int, input().split())
        edges[src][dst] = 1
        edges[dst][src] = 1

    remainings = [ i for i in range(1, node_cnt+1) ]
    conn_comps_cnt = 0
    while len(remainings) > 0:
        visited = []
        bfs(remainings[0], edges, visited)
        conn_comps_cnt += 1
        remainings = [ i for i in remainings if i not in visited ]
    print(conn_comps_cnt)
