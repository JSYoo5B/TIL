#!/usr/bin/env python3

from sys import stdin
input = stdin.readline


def get_mat_calc_min(mat_szs, start, end, costs = []):
    mat_cnt = len(mat_szs)
    if len(costs) == 0:
        costs = [ [ 2**32 for _ in range(mat_cnt) ] for _ in range(mat_cnt) ]
        for i in range(mat_cnt - 1):
            costs[i][i] = 0
            costs[i][i+1] = mat_szs[i][0] * mat_szs[i][1] * mat_szs[i+1][1]
        costs[-1][-1] = 0
        return get_mat_calc_min(mat_szs, start, end, costs)

    if costs[start][end] != 2**32:
        return costs[start][end]

    for mid in range(start, end):
        cost_left = get_mat_calc_min(mat_szs, start, mid, costs)
        cost_right = get_mat_calc_min(mat_szs, mid+1, end, costs)
        cost_cur = mat_szs[start][0] * mat_szs[mid][1] * mat_szs[end][1]
        costs[start][end] = min(costs[start][end], cost_left + cost_cur + cost_right)

    return costs[start][end]


if __name__ == '__main__':
    matrix_cnt = int(input())
    mat_szs = []
    for _ in range(matrix_cnt):
        r, c = map(int, input().split())
        mat_szs.append([r, c])

    answer = get_mat_calc_min(mat_szs, 0, matrix_cnt - 1)
    print(answer)
