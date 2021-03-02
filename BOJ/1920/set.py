#!/usr/bin/env python3

if __name__ == '__main__':
    num_count = int(input())
    numbers = set(map(int, input().split()))
    find_count = int(input())
    finds = list(map(int, input().split()))
    for n in finds:
        if n in numbers:
            print(1)
        else:
            print(0)
