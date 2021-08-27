#!/usr/bin/env python3

from collections import deque

if __name__ == '__main__':
    cnt_queue, cnt_reqs = map(int, input().split())
    requires = list(map(int, input().split()))
    q = deque([ i+1 for i in range(cnt_queue) ])
    answer = 0
    for r in requires:
        if q.index(r) <= len(q) // 2:
            while q[0] != r:
                q.rotate(-1)
                answer += 1
            q.popleft()
        else:
            while q[0] != r:
                q.rotate(1)
                answer += 1
            q.popleft()
    print(answer)
