#!/usr/bin/env python3

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

if __name__ == '__main__':
    N = int(input())

    answer = factorial(N)

    print(answer)
