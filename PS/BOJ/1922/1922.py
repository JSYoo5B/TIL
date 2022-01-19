#!/usr/bin/env python3

from heapq import heappush, heappop
from sys import stdin
input = lambda : stdin.readline().rstrip()


def get_minimum_spanning_tree(nodes_cnt, edges):
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
        if len(edges) == 0:
            min_span_tree = []
            break

        [cost, src, dst] = heappop(edges)

        if root(src) != root(dst):
            min_span_tree.append(cost)
            union(src, dst)

    return min_span_tree


if __name__ == '__main__':
    nodes_cnt = int(input())
    edges_cnt = int(input())
    edges = []
    for _ in range(edges_cnt):
        src, dst, cost = map(int, input().split())
        if src == dst:
            continue
        heappush(edges, [cost, src-1, dst-1])

    mst = get_minimum_spanning_tree(nodes_cnt, edges)
    answer = sum(mst)
    print(answer)
