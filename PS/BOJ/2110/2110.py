#!/usr/bin/env python3

from sys import stdin

input = stdin.readline

if __name__ == '__main__':
    houses_cnt, stations_cnt = map(int, input().split())
    houses = []
    for _ in range(houses_cnt):
        house = int(input())
        houses.append(house)
    houses.sort()

    s_gap = 1
    e_gap = houses[-1] - houses[0]
    answer = 0
    while s_gap <= e_gap:
        gap = (s_gap + e_gap) // 2

        stations = [houses[0]]
        for i in range(1, houses_cnt):
            dist = houses[i] - stations[-1]
            if dist < gap:
                continue
            stations.append(houses[i])
        
        if len(stations) >= stations_cnt:
            s_gap = gap + 1
            answer = gap
        else:
            e_gap = gap - 1
    print(answer)
