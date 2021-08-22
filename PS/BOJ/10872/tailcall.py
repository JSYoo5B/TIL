#!/usr/bin/env python3

def factorial(num, result = 1):
    if num == 0:
        return result
    return factorial(num - 1, num * result)

if __name__ == '__main__':
    N = int(input())

    answer = factorial(N)

    print(answer)
