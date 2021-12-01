#!/usr/bin/env python3

from collections import deque
import sys
input = sys.stdin.readline

def topological_sort(graph, in_degrees):
    nodes_cnt = len(in_degrees)
    topo_sort = []

    que = deque([ i for i in range(1, nodes_cnt) if in_degrees[i] == 0 ])
    while len(que) > 0:
        current = que.popleft()
        topo_sort.append(current)
        for n in graph[current]:
            in_degrees[n] -= 1
            if in_degrees[n] == 0:
                que.append(n)
    if len(topo_sort) < nodes_cnt - 1:
        topo_sort = []
    return topo_sort


if __name__ == '__main__':
    nodes_cnt, graph_cnt = map(int, input().split())
    in_degrees = [ 0 for _ in range(nodes_cnt + 1) ]
    graph = [ [] for _ in range(nodes_cnt + 1) ]
    for _ in range(graph_cnt):
        src, dst = map(int, input().split())
        graph[src].append(dst)
        in_degrees[dst] += 1

    linear_order = topological_sort(graph, in_degrees)
    print(*linear_order)
