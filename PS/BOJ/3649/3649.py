#!/usr/bin/env python3

from sys import stdin
input = stdin.readline

def main():
    hole_len = int(input())
    blks_cnt = int(input())
    blks = []
    for _ in range(blks_cnt):
        blk = int(input())
        blks.append(blk)
    blks.sort()

    hole_len *= 10000000
    left, right = 0, blks_cnt - 1
    while left < right:
        combine = blks[left] + blks[right]
        if combine == hole_len:
            break
        elif combine < hole_len:
            left += 1
        else:
            right -= 1

    if left >= right:
        print("danger")
    else:
        print("yes", blks[left], blks[right])


if __name__ == '__main__':
    while True:
        try:
            main()
        except:
            break
