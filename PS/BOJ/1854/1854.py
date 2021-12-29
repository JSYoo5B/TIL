#!/usr/bin/env python3

from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

INF = 10 ** 9

def dijkstra_nth(graph, src, nth):
    nodes_cnt = len(graph)
    dists = [ [ INF for _ in range(nth) ] for _ in range(nodes_cnt) ]
    dists[src][0] = 0
    heap = [[0, src]]
    while len(heap) > 0:
        dist, node = heappop(heap)
        for n, d in graph[node]:
            if dists[n][-1] > dist + d:
                dists[n][-1] = dist + d
                dists[n].sort()
                heappush(heap, [dist + d, n])
    return [ dists[i][-1] for i in range(nodes_cnt) ]
    

if __name__ == '__main__':
    nodes_cnt, edges_cnt, rank = map(int, input().split())
    graph = [ [] for _ in range(nodes_cnt) ]
    for _ in range(edges_cnt):
        src, dst, dist = map(int, input().split())
        src -= 1
        dst -= 1
        graph[src].append([dst, dist])

    answer = dijkstra_nth(graph, 0, rank)
    for a in answer:
        if a == INF:
            print(-1)
        else:
            print(a)
