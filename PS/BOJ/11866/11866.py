#!/usr/bin/env python3

from collections import deque

def josephus_loop(orig, skip):
    q = deque(orig)
    result = []
    while len(q) > 0:
        for i in range(skip - 1):
            q.append(q.popleft())
        result.append(q.popleft())
    return result

if __name__ == '__main__':
    N, K = map(int, input().split())
    orig = [ i for i in range(1, N+1) ]
    josephus = josephus_loop(orig, K)
    answer = '<' + ', '.join([ str(i) for i in josephus ]) + '>'
    print(answer)
