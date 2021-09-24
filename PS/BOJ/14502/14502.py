#!/usr/bin/env python3
import copy
from collections import deque

def set_walls(graph, remaining, pos_index):
    max_row = len(graph)
    max_col = len(graph[0])

    for pos in range(pos_index, max_row * max_col - remaining + 1):
        conv_row = pos // len(graph[0])
        conv_col = pos % len(graph[0])
        if graph[conv_row][conv_col] != 0:
            continue
        walled_graph = copy.deepcopy(graph)
        walled_graph[conv_row][conv_col] = 1
        if remaining == 1:
            yield walled_graph
        else:
            yield from set_walls(walled_graph, remaining - 1, pos + 1)
    return

def spread_virus(graph):
    max_row = len(graph)
    max_col = len(graph[0])
    for pos in range(max_row * max_col):
        conv_row = pos // len(graph[0])
        conv_col = pos % len(graph[0])
        if graph[conv_row][conv_col] != 2:
            continue
        que = deque([[conv_row, conv_col]])
        graph[conv_row][conv_col] = 3
        while len(que) > 0:
            current = que.popleft()
            avails = []
            avails.append([current[0]-1, current[1]])
            avails.append([current[0], current[1]-1])
            avails.append([current[0]+1, current[1]])
            avails.append([current[0], current[1]+1])
            for a in avails:
                if 0 <= a[0] < max_row and 0 <= a[1] < max_col:
                    if graph[a[0]][a[1]] == 0 or graph[a[0]][a[1]] == 2:
                        graph[a[0]][a[1]] = 3
                        que.append(a)
    return graph

if __name__ == '__main__':
    row_cnt, col_cnt = map(int, input().split())
    graph = []
    for _ in range(row_cnt):
        row = list(map(int, input().split()))
        graph.append(row)
    
    graph_gen = set_walls(graph, 3, 0)
    remain_spaces = []
    for walled_graph in graph_gen:
        spread_result = spread_virus(walled_graph)
        space = 0
        for row in spread_result:
            space += row.count(0)
        remain_spaces.append(space)
    answer = max(remain_spaces)
    print(answer)
