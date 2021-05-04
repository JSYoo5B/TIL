#!/usr/bin/env python3

if __name__ == '__main__':
    day = int(input())
    cars = list(map(int, input().split()))
    answer = cars.count(day)
    print(answer)
