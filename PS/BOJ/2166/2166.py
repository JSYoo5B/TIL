#!/usr/bin/env python3

from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    verts_cnt = int(input())
    verts = []
    for _ in range(verts_cnt):
        x, y = map(int, input().split())
        verts.append([x, y])

    area = 0.0
    for i in range(verts_cnt):
        det = verts[i-1][0]*verts[i][1]
        det -= verts[i-1][1]*verts[i][0]
        area += det
    area /= 2
    area = abs(area)
    print("{:.1f}".format(area))
