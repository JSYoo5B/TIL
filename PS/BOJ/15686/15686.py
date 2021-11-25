#!/usr/bin/env python3

from itertools import combinations

if __name__ == '__main__':
    tbl_size, remain_cnt = map(int, input().split())
    tbl = []
    for _ in range(tbl_size):
        row = list(map(int, input().split()))
        tbl.append(row)

    homes = []
    stores = []
    for r in range(tbl_size):
        for c in range(tbl_size):
            if tbl[r][c] == 1:
                homes.append([r, c])
            if tbl[r][c] == 2:
                stores.append([r, c])


    comb = combinations(stores, remain_cnt)
    min_costs = []
    for sel_stores in comb:
        cur_cost = 0
        for [h_r, h_c] in homes:
            costs = []
            for [s_r, s_c] in sel_stores:
                costs.append(abs(s_r-h_r) + abs(s_c-h_c))
            cur_cost += min(costs)
        min_costs.append(cur_cost)
    answer = min(min_costs)
    print(answer)

