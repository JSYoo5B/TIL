#!/usr/bin/env python3

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

if __name__ == '__main__':
    n = int(input())

    answer = fibonacci(n)

    print(answer)
