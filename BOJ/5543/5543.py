#!/usr/bin/env python3

if __name__ == '__main__':
    burgers = []
    beverages = []
    for i in range(3):
        burger = int(input())
        burgers.append(burger)
    for i in range(2):
        beverage = int(input())
        beverages.append(beverage)

    answer = min(burgers) + min(beverages) - 50
    print(answer)
