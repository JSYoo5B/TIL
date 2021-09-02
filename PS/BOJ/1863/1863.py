#!/usr/bin/env python3

if __name__ == '__main__':
    cnt_inputs = int(input())
    stack = []
    answer = 0
    for _ in range(cnt_inputs):
        x, y = map(int, input().split())
        while len(stack) != 0 and stack[-1] > y:
            answer += 1
            stack.pop()
        if len(stack) != 0 and stack[-1] == y:
            continue
        stack.append(y)
    answer += len([ x for x in stack if x > 0 ])
    print(answer)
