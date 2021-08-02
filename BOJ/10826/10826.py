#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

def fibonacci(num, memo = [0, 1]):
    if len(memo) > num:
        return memo[num]
    elif len(memo) == num:
        next = memo[num-1] + memo[num-2]
        memo.append(next)
        return next
    else:
        return fibonacci(num-1) + fibonacci(num-2)

if __name__ == '__main__':
    n = int(input())

    answer = fibonacci(n)

    print(answer)
