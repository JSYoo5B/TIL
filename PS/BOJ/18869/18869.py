#!/usr/bin/env python3

from sys import stdin
input = lambda : stdin.readline().rstrip()

if __name__ == '__main__':
    univ_cnt, planet_cnt = map(int, input().split())
    univs = []
    for _ in range(univ_cnt):
        planets = list(map(int, input().split()))
        univ = [0]
        min_val, max_val = planets[0], planets[0]
        min_idx, max_idx = 0, 0
        for i in range(1, planet_cnt):
            cur = univ[-1]
            if planets[i] < min_val:
                cur = min_idx - 1
                min_val, min_idx = planets[i], cur
            elif planets[i] > max_val:
                cur = max_idx + 1
                max_val, max_idx = planets[i], cur
            elif planets[i] > planets[i-1]:
                cur += 1
            elif planets[i] < planets[i-1]:
                cur -= 1
            univ.append(cur)
        univ_str = ''.join([str(i) for i in univ])
        univs.append(univ_str)
        
    answer = 0
    for left in range(univ_cnt-1):
        for right in range(left+1, univ_cnt):
            if univs[left] == univs[right]:
                answer += 1
    print(answer)
