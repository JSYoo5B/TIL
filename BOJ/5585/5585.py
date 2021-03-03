#!/usr/bin/env python3

if __name__ == '__main__':
    coins = [500, 100, 50, 10, 5, 1]
    price = int(input())
    remaining = 1000 - price

    coin_req = 0
    for c in coins:
        if c > remaining:
            continue
        coin_req += remaining // c
        remaining %= c

    print(coin_req)
