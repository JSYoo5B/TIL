#!/usr/bin/env python3 

from collections import deque
from sys import stdin
input = stdin.readline

IMG_CODE = dict()
IMG_CODE['R'] = -2
IMG_CODE['G'] = -1
IMG_CODE['B'] = 1

def is_same_color(img, r1, c1, r2, c2):
    return img[r1][c1] == img[r2][c2]


def is_rg_same_color(img, r1, c1, r2, c2):
    tmp = img[r1][c1] + img[r2][c2]
    return tmp <= -2 or tmp == 2


def segment_img(img, segs, pos, id, check_same):
    img_size = len(img)
    segs[pos[0]][pos[1]] = id
    que = deque([pos])
    while len(que) > 0:
        [r, c] = que.popleft()
        for n_r, n_c in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
            if 0 > n_r or n_r >= img_size or 0 > n_c or n_c >= img_size:
                continue
            if segs[n_r][n_c] == 0 and check_same(img, r, c, n_r, n_c):
                segs[n_r][n_c] = id
                que.append([n_r, n_c])


if __name__ == '__main__':
    img_size = int(input())
    img = []
    for _ in range(img_size):
        line = input().rstrip()
        img_row = [ IMG_CODE[c] for c in line ]
        img.append(img_row)

    orig_segs = [ [ 0 for _ in range(img_size) ] for _ in range(img_size) ]
    rg_segs = [ [ 0 for _ in range(img_size) ] for _ in range(img_size) ]
    orig_id, rg_id = 0, 0
    for r in range(img_size):
        for c in range(img_size):
            if orig_segs[r][c] == 0:
                orig_id += 1
                segment_img(img, orig_segs, [r, c], orig_id, is_same_color)
            if rg_segs[r][c] == 0:
                rg_id += 1
                segment_img(img, rg_segs, [r, c], rg_id, is_rg_same_color)
    print(orig_id, rg_id)
