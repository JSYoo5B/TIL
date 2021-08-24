#!/usr/bin/env python3

if __name__ == '__main__':
    cnt = int(input())
    numbers = list(map(int, input().split()))

    stack = [1000001]
    nges = [ -1 for _ in range(cnt) ]
    last_max = 0
    for i in range(cnt-1, -1, -1):
        while numbers[i] >= stack[-1]:
            stack.pop()
        if numbers[i] < stack[-1]:
            if len(stack) == 1:
                nges[i] = -1
            else:
                nges[i] = stack[-1]
            stack.append(numbers[i])
    print(*nges)
