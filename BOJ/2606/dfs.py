#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

def dfs(node, edges, visited):
    visited.append(node)
    for i in range(len(edges)):
        if edges[node][i] == 1 and i not in visited:
            dfs(i, edges, visited)

if __name__ == '__main__':
    node_cnt = int(input())
    edges_cnt = int(input())
    edges = [ [ 0 for i in range(node_cnt + 1) ] for j in range(node_cnt + 1) ]
    for e in range(edges_cnt):
        src, dst = map(int, input().split())
        edges[src][dst] = 1
        edges[dst][src] = 1

    visited = []
    dfs(1, edges, visited)
    answer = len(visited) - 1
    print(answer)
