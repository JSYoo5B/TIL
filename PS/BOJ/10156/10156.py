#!/usr/bin/env python3

if __name__ == '__main__':
    price, cnt, balance = map(int, input().split())
    answer = price * cnt - balance
    if answer < 0:
        answer = 0
    print(answer)
