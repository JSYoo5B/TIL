#!/usr/bin/env python3

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

INF = 10 * 3000000

def get_dists(edges, start_node):
    nodes_cnt = len(edges)
    dists = [ INF for _ in range(nodes_cnt) ]

    heap = [ [0, start_node] ]
    while len(heap) > 0:
        [dist, node] = heappop(heap)
        dists[node] = min(dists[node], dist)
        for d, n in edges[node]:
            if dist + d < dists[n]:
                dists[n] = dist + d
                heappush(heap, [dists[n], n])
    return dists


if __name__ == '__main__':
    nodes_cnt, edges_cnt = map(int, input().split())
    start_node = int(input()) - 1
    edges = [ [] for _ in range(nodes_cnt) ]
    for _ in range(edges_cnt):
        src, dst, dist = map(int, input().split())
        src -= 1
        dst -= 1
        edges[src].append([dist, dst])

    dists = get_dists(edges, start_node)
    for i in dists:
        if i == INF:
            print("INF")
        else:
            print(i)
