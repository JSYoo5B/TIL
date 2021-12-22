#!/usr/bin/env python3

from heapq import heappush, heappop
from sys import stdin
input = stdin.readline


def minimum_spanning_tree(nodes_cnt, graph):
    parents = [ i for i in range(nodes_cnt) ]

    def root(n):
        updates = []
        while n != parents[n]:
            updates.append(n)
            n = parents[n]
        for u in updates:
            parents[u] = n
        return parents[n]
    def union(n1, n2):
        parents[root(n2)] = root(n1)

    min_span_tree = []
    while len(min_span_tree) < nodes_cnt - 1:
        if len(graph) == 0:
            min_span_tree = []

        [cost, src, dst] = heappop(graph)

        if root(src) != root(dst):
            min_span_tree.append([cost, src, dst])
            union(src, dst)

    return min_span_tree


if __name__ == '__main__':
    planets_cnt = int(input())
    planets = []
    for r in range(planets_cnt):
        row = list(map(int, input().split()))
        for c in range(r+1, planets_cnt):
            heappush(planets, [row[c], r, c])

    mst = minimum_spanning_tree(planets_cnt, planets)
    answer = 0
    for c, _, _ in mst:
        answer += c
    print(answer)
