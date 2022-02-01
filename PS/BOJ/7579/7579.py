#!/usr/bin/env python3

from sys import stdin
input = lambda : stdin.readline().rstrip()

if __name__ == '__main__':
    apps_cnt, req_mem = map(int, input().split())
    mems = [0] + list(map(int, input().split()))
    costs = [0] + list(map(int, input().split()))

    answer = sum(costs)
    if req_mem == 0:
        answer = 0
    cands = [ [ 0 for _ in range(sum(costs)+1) ] for _ in range(apps_cnt+1) ]
    for cur in range(1, apps_cnt+1):
        mem = mems[cur]
        cost = costs[cur]

        for remain in range(1, sum(costs) + 1):
            if remain < cost:
                cands[cur][remain] = cands[cur-1][remain]
            else:
                cands[cur][remain] = max(mem + cands[cur-1][remain-cost], cands[cur-1][remain])

            if cands[cur][remain] >= req_mem:
                answer = min(answer, remain)
    print(answer)
