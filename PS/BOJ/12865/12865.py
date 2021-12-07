#!/usr/bin/env python3

from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    items_cnt, capacity = map(int, input().split())
    items = [ [0, 0] ] # dummy item
    for _ in range(items_cnt):
        weight, price = map(int, input().split())
        if weight > capacity or price == 0:
            continue
        items.append([weight, price])
    items_cnt = len(items)

    bags = [ [ 0 for _ in range(capacity+1) ] for _ in range(items_cnt) ]
    for i in range(1, items_cnt):
        for remain in range(1, capacity+1):
            [weight, price] = items[i]

            if remain < weight:
                bags[i][remain] = bags[i-1][remain]
            else:
                bags[i][remain] = max(price + bags[i-1][remain-weight], \
                        bags[i-1][remain])
    answer = bags[-1][-1]
    print(answer)
