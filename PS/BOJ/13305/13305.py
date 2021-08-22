#!/usr/bin/env python3

if __name__ == '__main__':
    cnt_cities = int(input())
    dists = list(map(int, input().split()))
    prices = list(map(int, input().split()))

    budget = 0
    remain_dist = sum(dists)
    current_price = prices[0]
    city = 0
    while remain_dist > 0:
        if current_price > prices[city]:
            current_price = prices[city]
        budget += current_price * dists[city]
        remain_dist -= dists[city]
        city += 1

    print(budget)
