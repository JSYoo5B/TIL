#!/usr/bin/env python3

from sys import stdin
input = lambda : stdin.readline().rstrip()

if __name__ == '__main__':
    univ_cnt, planet_cnt = map(int, input().split())
    univs = []
    for _ in range(univ_cnt):
        planets = list(map(int, input().split()))
        orders = sorted(planets)
        univ = [orders.index(x) for x in planets]
        univs.append(univ)
        
    answer = 0
    for left in range(univ_cnt-1):
        for right in range(left+1, univ_cnt):
            identical = True
            for p in range(planet_cnt):
                if univs[left][p] != univs[right][p]:
                    identical = False
                    break
            if identical:
                answer += 1
    print(answer)
