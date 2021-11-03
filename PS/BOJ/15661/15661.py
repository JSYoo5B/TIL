#!/usr/bin/env python3

input = __import__('sys').stdin.readline

from itertools import combinations

if __name__ == '__main__':
    players_cnt = int(input())
    stat_tbl = []
    for _ in range(players_cnt):
        row = list(map(int, input().split()))
        stat_tbl.append(row)

    player_pool = [ i for i in range(players_cnt) ]
    min_diff = 100**20
    for left_cnt in range(2, players_cnt//2 + 1):
        left_teams = combinations(player_pool, left_cnt)
        for left in left_teams:
            right = [ p for p in player_pool if p not in left ]
            left_stat, right_stat = 0, 0
            for p1 in left:
                for p2 in left:
                    left_stat += stat_tbl[p1][p2]
            for p1 in right:
                for p2 in right:
                    right_stat += stat_tbl[p1][p2]
            diff = max(left_stat, right_stat) - min(left_stat, right_stat)
            min_diff = min(min_diff, diff)
            if min_diff == 0:
                break
        if min_diff == 0:
            break
    print(min_diff)
