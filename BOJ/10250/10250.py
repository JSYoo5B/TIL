#!/usr/bin/env python3

if __name__ == '__main__':
    test_cases = int(input())

    for t in range(test_cases):
        H, W, N = map(int, input().split())
        floor = N % H
        room = N // H
        if floor == 0:
            floor = H
        else:
            room += 1
        room_number = floor * 100 + room
        print(room_number)
