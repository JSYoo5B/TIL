#!/usr/bin/env python3

from collections import deque

import sys
input = sys.stdin.readline


def move_like_horse(graph, jump_avail):
    row_cnt, col_cnt = len(graph), len(graph[0])
    max_trial = row_cnt * col_cnt + 1
    trials = [ [ [max_trial for _ in range(jump_avail + 1)] \
            for _ in range(col_cnt) ] \
            for _ in range(row_cnt) ]
    trials[0][0] = [0 for _ in range(jump_avail + 1)]
    que = deque([[0, 0, jump_avail]])
    while len(que) > 0:
        [r, c, jump_left] = que.popleft()
        if [r, c] == [row_cnt-1, col_cnt-1]:
            break
        trial = trials[r][c][jump_left] + 1
        monkey_moves = [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]
        for [m_r, m_c] in monkey_moves:
            if 0 > m_r or m_r >= row_cnt \
                    or 0 > m_c or m_c >= col_cnt:
                continue
            if graph[m_r][m_c] == 1:
                continue
            if trials[m_r][m_c][jump_left] > trial:
                trials[m_r][m_c][jump_left] = trial
                que.append([m_r, m_c, jump_left])

        if jump_left == 0:
            continue
        jump_left -= 1
        jump_moves = [ [r-2, c-1], [r-2, c+1], [r-1, c-2], [r-1, c+2], \
                [r+2, c-1], [r+2, c+1], [r+1, c-2], [r+1, c+2] ]
        for [j_r, j_c] in jump_moves:
            if 0 > j_r or j_r >= row_cnt \
                    or 0 > j_c or j_c >= col_cnt:
                continue
            if graph[j_r][j_c] == 1:
                continue
            if trials[j_r][j_c][jump_left] > trial:
                trials[j_r][j_c][jump_left] = trial
                que.append([j_r, j_c, jump_left])

    answer = min(trials[row_cnt-1][col_cnt-1])
    if answer == max_trial:
        answer = -1
    return answer


if __name__ == '__main__':
    jump_avail = int(input())
    col_cnt, row_cnt = map(int, input().split())
    graph = []
    for _ in range(row_cnt):
        row = list(map(int, input().split()))
        graph.append(row)

    answer = move_like_horse(graph, jump_avail)
    print(answer)
