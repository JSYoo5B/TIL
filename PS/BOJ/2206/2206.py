#!/usr/bin/env python3

import sys

input = sys.stdin.readline

from collections import deque

def find_shortest_path(graph):
    row_cnt, col_cnt = len(graph), len(graph[0])
    max_trial = row_cnt * col_cnt + 1
    trials = [ [ [max_trial, max_trial] for _ in range(col_cnt) ] \
            for _ in range(row_cnt) ]
    trials[0][0][1] = 1
    que = deque([ [0, 0, 1] ])
    while len(que) > 0:
        [r, c, avail] = que.popleft()
        if [r, c] == [row_cnt-1, col_cnt-1]:
            break
        cur_trial = trials[r][c][avail] + 1
        neighbors = [ [r-1, c], [r+1, c], [r, c-1], [r, c+1] ]
        for [n_r, n_c] in neighbors:
            if 0 > n_r or n_r >= row_cnt \
                    or 0 > n_c or n_c >= col_cnt:
                continue
            if graph[n_r][n_c] == 0 \
                    and trials[n_r][n_c][avail] == max_trial:
                trials[n_r][n_c][avail] = cur_trial
                que.append([n_r, n_c, avail])
            if avail == 1 and graph[n_r][n_c] == 1 \
                    and trials[n_r][n_c][0] == max_trial:
                trials[n_r][n_c][0] = cur_trial
                que.append([n_r, n_c, 0])
    answer = min(trials[row_cnt-1][col_cnt-1])
    if answer == max_trial:
        answer = -1
    return answer


if __name__ == '__main__':
    row_cnt, col_cnt = map(int, input().split())
    graph = []
    for _ in range(row_cnt):
        row = input().rstrip()
        row = [ int(i) for i in row ]
        graph.append(row)

    answer = find_shortest_path(graph)
    print(answer)
