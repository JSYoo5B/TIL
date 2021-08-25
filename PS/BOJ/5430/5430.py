#!/usr/bin/env python3

from collections import deque

def run_AC(operations, numbers):
    dq = deque(numbers)
    front = True
    for o in operations:
        if o == 'R':
            front = not front
        if o == 'D':
            if len(dq) == 0:
                return None
            if front:
                dq.popleft()
            else:
                dq.pop()
    if not front:
        dq.reverse()

    return list(dq)

if __name__ == '__main__':
    cnt_tests = int(input())
    for _ in range(cnt_tests):
        operations = input()
        cnt_nums = int(input())
        arr = input()
       
        numbers = []
        if cnt_nums > 0:
            numbers = list(map(int, arr[1:-1].split(',')))
        result = run_AC(operations, numbers)
        if result == None:
            print('error')
        else:
            print('[' + ','.join([ str(n) for n in result ]) + ']')
