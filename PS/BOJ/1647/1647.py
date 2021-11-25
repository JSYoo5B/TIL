#!/usr/bin/env python3

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

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
    while len(min_span_tree) < nodes_cnt - 2:
        if len(edges) == 0:
            min_span_tree = []
            break

        [cost, src, dst] = heappop(edges)
        # Skip when current edge generates cycle
        if root(src) != root(dst):
            min_span_tree.append([cost, src, dst])
            union(src, dst)    

    return min_span_tree

if __name__ == '__main__':
    nodes_cnt, edges_cnt = map(int, input().split())
    edges = []
    for _ in range(edges_cnt):
        src, dst, cost = map(int, input().split())
        src, dst = min(src, dst), max(src, dst)
        heappush(edges, [cost, src-1, dst-1])

    min_span_tree = get_minimum_spanning_tree(nodes_cnt, edges)
    total_cost = 0
    for cost, _, _ in min_span_tree:
        total_cost += cost
    print(total_cost)
