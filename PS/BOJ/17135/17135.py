#!/usr/bin/env python3

import sys
from copy import deepcopy
from itertools import combinations


def get_attack_diffs(atk_range):
    diffs = []
    for d in range(1, atk_range+1):
        for x in range(-1 * d+1, d, 1):
            y = d - abs(x)
            diffs.append([-y, x])
    return diffs


def play_game(game_tbl, archer_poses, atk_diffs):
    row_cnt, col_cnt = len(game_tbl), len(game_tbl[0])
    
    cur_tbl = deepcopy(game_tbl)
    enemy_killed = 0
    for turn in range(row_cnt, 0, -1):
        tgt_enemies = []
        for archer in archer_poses:
            for [r, c] in atk_diffs:
                p_r, p_c = [turn + r, archer + c]
                if 0 > p_c or p_c >= col_cnt \
                        or 0 > p_r or p_r >= row_cnt:
                    continue
                if cur_tbl[p_r][p_c] == 1:
                    tgt_enemies.append([p_r, p_c])
                    break
        for [r, c] in tgt_enemies:
            if cur_tbl[r][c] == 1:
                enemy_killed += 1
                cur_tbl[r][c] = 0
    return enemy_killed
        

if __name__ == '__main__':
    row_cnt, col_cnt, atk_range = map(int, input().split())
    game_tbl = []
    for _ in range(row_cnt):
        row = list(map(int, input().split()))
        game_tbl.append(row)

    atk_diffs = get_attack_diffs(atk_range)
    max_score = 0
    for archer_poses in combinations([ i for i in range(col_cnt) ], 3):
        score = play_game(game_tbl, archer_poses, atk_diffs)
        max_score = max(max_score, score)
    print(max_score)
