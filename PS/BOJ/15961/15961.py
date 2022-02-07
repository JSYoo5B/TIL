#!/usr/bin/env python3

from collections import defaultdict
from sys import stdin
input = lambda : stdin.readline().rstrip()

if __name__ == '__main__':
    dish_cnt, sushi_type_cnt, cont_cnt, coup_num = map(int, input().split())
    sushies = []
    for _ in range(dish_cnt):
        sushi_type = int(input())
        sushies.append(sushi_type)

    # Create dishes with loop
    dishes = []
    dishes += sushies
    dishes += sushies
    dishes.pop()

    # Configure first selects
    selects = defaultdict(int)
    for i in range(cont_cnt):
        selects[dishes[i]] += 1
    
    answer = len(selects)
    if coup_num not in selects.keys():
        answer += 1
    for i in range(1, dish_cnt):
        # Skip for same results
        if dishes[i+cont_cnt-1] == dishes[i-1]:
            continue

        # decrease previous, increase next
        selects[dishes[i-1]] -= 1
        selects[dishes[i+cont_cnt-1]] += 1
        if selects[dishes[i-1]] == 0:
            del selects[dishes[i-1]]
 
        cur_result = len(selects)
        if coup_num not in selects.keys():
            cur_result += 1
        answer = max(answer, cur_result)
        if answer == sushi_type_cnt or answer == cont_cnt + 1:
            break

    print(answer)
