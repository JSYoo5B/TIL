#!/usr/bin/env python3

if __name__ == '__main__':
    weights_cnt = int(input())
    weights = list(map(int, input().split()))
    weights.sort()

    tgt_num = 1
    for w in weights:
        if tgt_num < w:
            break
        tgt_num += w
    print(tgt_num)
