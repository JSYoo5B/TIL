#!/usr/bin/env python3

from collections import deque

def get_min_trial(graph, start):
    que = deque([[start, 0]])
    visited = [ 0 for _ in range(len(graph)) ]
    visited[start] = 1
    trial = 1
    while len(que) > 0:
        [cur, trial] = que.popleft()
        if cur == 100:
            break
        for p in [ cur + i for i in range(6, 0, -1) if cur + i <= 100 ]:
            if graph[p] > -1:
                p = graph[p]
            if visited[p] == 1:
                continue
            visited[p] = 1
            que.append([p, trial+1])
    return trial


if __name__ == '__main__':
    graph = [ -1 for _ in range(101) ]
    cnt_ladder, cnt_bridge = map(int, input().split())
    for _ in range(cnt_ladder + cnt_bridge):
        start, end = map(int, input().split())
        graph[start] = end

    answer = get_min_trial(graph, 1)
    print(answer)
