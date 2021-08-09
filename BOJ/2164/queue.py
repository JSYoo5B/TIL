#!/usr/bin/env python3

from collections import deque

if __name__ == '__main__':
    N = int(input())
    numbers = deque([ i for i in range(1, N+1) ])

    while len(numbers) > 1:
        numbers.popleft()
        numbers.append(numbers.popleft())

    print(numbers.pop())
