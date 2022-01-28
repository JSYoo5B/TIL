#!/usr/bin/env python3

from collections import deque

def get_path_to_dst(src, dst):
    limit = min(max(src+10, dst+10), 100001)
    prevs = [ -1 for _ in range(limit) ]
    prevs[src] = src
    que = deque([src])
    while len(que) > 0:
        cur = que.popleft()
        if cur == dst:
            break

        for next in [cur-1, cur+1, cur*2]:
            if next < 0 or next >= limit:
                continue
            if prevs[next] == -1:
                prevs[next] = cur
                que.append(next)

    cur = dst
    answers = []
    while prevs[cur] != cur:
        answers.append(cur)
        cur = prevs[cur]
    answers.append(src)
    answers.reverse()
    return answers


if __name__ == '__main__':
    src, dst = map(int, input().split())
    answers = get_path_to_dst(src, dst)
    print(len(answers)-1)
    print(*answers)
