#!/usr/bin/env python3

if __name__ == '__main__':
    total_price = int(input())
    for _ in range(9):
        price = int(input())
        total_price -= price
    answer = total_price
    print(answer)
