#!/usr/bin/env python3

if __name__ == '__main__':
    coin_cnt, remaining = map(int, input().split())
    coins = []
    for i in range(coin_cnt):
        coin = int(input())
        coins.append(coin)
    coins.reverse()
    coin_req = 0
    for c in coins:
        if remaining < c:
            continue
        coin_req += remaining // c
        remaining %= c

    print(coin_req)
        
