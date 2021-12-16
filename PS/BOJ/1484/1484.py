#!/usr/bin/env python3

if __name__ == '__main__':
    tgt_diff = int(input())

    weights = [ (i+1)**2 for i in range(100000) ]
    origin, gain = 0, 1
    avails = []
    while origin < 100000 and gain < 100000:
        if origin >= gain:
            gain += 1
            continue

        diff = weights[gain] - weights[origin]
        if tgt_diff == diff:
            avails.append(gain+1)
            origin += 1
        elif diff < tgt_diff:
            gain += 1
        else:
            origin += 1

        if weights[gain] - weights[gain-1] > tgt_diff * 2:
            break
    if len(avails) == 0:
        print(-1)
    else:
        for a in avails:
            print(a)
