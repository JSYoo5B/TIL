#!/usr/bin/env python3

def get_ways_to_price(coins, price):
    ways = [ 0 for _ in range(price + 1) ]
    for c in coins:
        if c > price:
            break
        ways[c] += 1
        for cur in range(c+1, price+1):
            ways[cur] += ways[cur-c]
    return ways[price]

if __name__ == '__main__':
    tests_cnt = int(input())
    for _ in range(tests_cnt):
        coins_cnt = int(input())
        coins = list(map(int, input().split()))
        price = int(input())
        ways = get_ways_to_price(coins, price)
        print(ways)
