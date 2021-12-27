#!/usr/bin/env python3

from heapq import heappush, heappop
from sys import stdin
input = stdin.readline
INF = 10 ** 9

def shortest_path(edges, src):
    nodes_cnt = len(edges)
    dists = [ INF for _ in range(nodes_cnt) ]
    heap = [ [0, src] ]
    while len(heap) > 0:
        [dist, node] = heappop(heap)
        dists[node] = min(dists[node], dist)
        for n in range(nodes_cnt):
            if edges[node][n] == INF:
                continue
            d = edges[node][n]
            if dist + d < dists[n]:
                dists[n] = dist + d
                heappush(heap, [dists[n], n])
    return dists


if __name__ == '__main__':
    cities_cnt = int(input())
    edges_cnt = int(input())
    edges = [ [ INF for _ in range(cities_cnt) ] for _ in range(cities_cnt) ]
    for _ in range(edges_cnt):
        src, dst, dist = map(int, input().split())
        edges[src-1][dst-1] = min(edges[src-1][dst-1], dist)
    src_city, dst_city = map(int, input().split())

    dists = shortest_path(edges, src_city-1)
    answer = dists[dst_city-1]
    print(answer)
