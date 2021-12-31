#!/usr/bin/env python3

from collections import deque
from sys import stdin
input = stdin.readline

MAX_DIST = 20 * 50

def get_dist(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])


def travel(home, stores, fest):
    que = deque([home])
    visited = [home]
    avail = False
    while len(que) > 0:
        cur = que.popleft()
        if get_dist(cur, fest) <= MAX_DIST:
            avail = True
            break
        for p in stores:
            if p in visited:
                continue
            if get_dist(cur, p) <= MAX_DIST:
                visited.append(p)
                que.append(p)
    return avail


if __name__ == '__main__':
    test_cnt = int(input())
    for _ in range(test_cnt):
        store_cnt = int(input())
        stores = []
        home = list(map(int, input().split()))
        for _ in range(store_cnt):
            x, y = map(int, input().split())
            stores.append([x, y])
        fest = list(map(int, input().split()))
        
        answer = travel(home, stores, fest)
        if answer == True:
            print("happy")
        else:
            print("sad")
