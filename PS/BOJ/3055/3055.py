#!/usr/bin/env python3

from collections import deque

def escape(graph, hedgehog, hole, waters):
    row_cnt = len(graph)
    col_cnt = len(graph[0])
    que = deque([ [w, '*', 0] for w in waters ])
    que.append([hedgehog, 'S', 0])
    time = 0
    while len(que) > 0:
        [[r, c], type, time] = que.popleft()
        neighbors = [ [r-1, c], [r+1, c], [r, c-1], [r, c+1] ]
        for [n_r, n_c] in neighbors:
            if 0 > n_r or n_r >= row_cnt \
                    or 0 > n_c or n_c >= col_cnt:
                continue
            if graph[n_r][n_c] == 'X' \
                    or graph[n_r][n_c] == '*' \
                    or graph[n_r][n_c] == 'S':
                continue
            elif graph[n_r][n_c] == 'D':
                if type == 'S': 
                    return time + 1
                elif type == '*':
                    continue
            graph[n_r][n_c] = type
            que.append([[n_r, n_c], type, time + 1])
    return -1

if __name__ == '__main__':
    row_cnt, col_cnt = map(int, input().split())
    hedgehog, hole = [], []
    waters = []
    graph = []
    for r in range(row_cnt):
        row = [ i for i in input() ]
        for c in range(col_cnt):
            if row[c] == 'D':
                hole = [r, c]
            elif row[c] == 'S':
                hedgehog = [r, c]
            elif row[c] == '*':
                waters.append([r, c])
        graph.append(row)

    answer = escape(graph, hedgehog, hole, waters)
    if answer == -1:
        answer = "KAKTUS"
    print(answer)
