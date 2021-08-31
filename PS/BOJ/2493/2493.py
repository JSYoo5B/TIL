#!/usr/bin/env python3

if __name__ == '__main__':
    cnt_towers = int(input())
    heights = list(map(int, input().split()))
    towers = [ [i+1, heights[i]] for i in range(cnt_towers) ]
    stack = [[0, 100_000_001]]
    lefts = []
    for t in towers:
        watching = stack[-1]
        if watching[1] > t[1]:
            lefts.append(watching[0])
            stack.append(t)
        else:
            while watching[1] <= t[1]:
                stack.pop()
                watching = stack[-1]
            lefts.append(watching[0])
            stack.append(t)
    print(*lefts)
