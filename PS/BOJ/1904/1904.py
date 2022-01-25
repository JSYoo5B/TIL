#!/usr/bin/env python3

from collections import deque

if __name__ == '__main__':
    length = int(input())
    length -= 1

    avails = deque([ [0, 0] for _ in range(2) ])
    avails[0][1] = 1
    avails[1][0] = 1
    avails[1][1] = 1

    for _ in range(length - 1):
        next = [0, 0]
        next[0] = (avails[-2][0] + avails[-2][1]) % 15746
        next[1] = (avails[-1][0] + avails[-1][1]) % 15746
        avails.popleft()
        avails.append(next)

    if length >= 2:
        print(sum(avails[-1]) % 15746)
    else:
        print(sum(avails[length]))
