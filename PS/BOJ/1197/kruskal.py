#!/usr/bin/env python3

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def kruskal(node_cnt, edges):
    parents = [ i for i in range(node_cnt) ]

    def root(n):
        while n != parents[n]:
            n = parents[n]
        return parents[n]
    def union(n1, n2):
        parents[root(n2)] = root(n1)

    mst = []
    while len(mst) < node_cnt - 1:
        if len(edges) == 0:
            mst = []
            break
        [dist, src, dst] = heappop(edges)
        if root(src) != root(dst):
            mst.append([dist, src, dst])
            union(src, dst)
    return mst

if __name__ == '__main__':
    node_cnt, edge_cnt = map(int, input().split())
    edges = []
    for _ in range(edge_cnt):
        src, dst, dist = map(int, input().split())
        heappush(edges, [dist, src-1, dst-1])

    mst = kruskal(node_cnt, edges)
    answer = 0
    for dist, _, _ in mst:
        answer += dist
    print(answer)
