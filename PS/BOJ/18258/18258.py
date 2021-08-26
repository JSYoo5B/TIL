#!/usr/bin/env python3

import sys
from collections import deque

if __name__ == '__main__':
    op_cnt = int(sys.stdin.readline().strip())
    q = deque()
    for _ in range(op_cnt):
        operation = sys.stdin.readline().strip()
        arg = 0
        if operation.startswith('push'):
            arg = operation.split()[1]
            operation = operation.split()[0]

        if operation == 'push':
            q.append(arg)
        elif operation == 'pop':
            result = q.popleft() if len(q) > 0 else -1
            print(result)
        elif operation == 'size':
            result = len(q)
            print(result)
        elif operation == 'empty':
            result = 1 if len(q) == 0 else 0
            print(result)
        elif operation == 'front':
            result = q[0] if len(q) > 0 else -1
            print(result)
        elif operation == 'back':
            result = q[-1] if len(q) > 0 else -1
            print(result)
