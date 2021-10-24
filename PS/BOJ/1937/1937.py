#!/usr/bin/env python3

import sys
sys.setrecursionlimit(10**6)

def find_max_path(graph, max_info, pos):
    graph_cnt = len(graph)
    [r, c] = pos
    if max_info[r][c] > 0:
        return max_info[r][c]
    max_info[r][c] = 1

    neighbors = [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]
    for [n_r, n_c] in neighbors:
        if 0 > n_r or n_r >= graph_cnt \
                or 0 > n_c or n_c >= graph_cnt:
            continue
        if graph[r][c] < graph[n_r][n_c]:
            max_info[r][c] = max(max_info[r][c], \
                    find_max_path(graph, max_info, [n_r, n_c]) + 1)
    return max_info[r][c]

if __name__ == '__main__':
    graph_cnt = int(input())
    graph = []
    for _ in range(graph_cnt):
        row = list(map(int, input().split()))
        graph.append(row)

    max_info = [ [ 0 for _ in range(graph_cnt) ] \
            for _ in range(graph_cnt) ]
    
    answer = 0
    for r in range(graph_cnt):
        for c in range(graph_cnt):
            answer = max(answer, find_max_path(graph, max_info, [r, c]))
    print(answer)
