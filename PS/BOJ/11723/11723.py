#!/usr/bin/env python3

from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    op_cnt = int(input())
    sets = set()
    for _ in range(op_cnt):
        oper = list(input().split())
        operation, operand = oper[0], 0
        if len(oper) == 2:
            operand = int(oper[1])
        
        if operation == 'add':
            sets.add(operand)
        elif operation == 'remove':
            sets.discard(operand)
        elif operation == 'check':
            answer = 1 if operand in sets else 0
            print(answer)
        elif operation == 'toggle':
            if operand in sets:
                sets.discard(operand)
            else:
                sets.add(operand)
        elif operation == 'all':
            sets |= { i for i in range(1, 21) }
        elif operation == 'empty':
            sets.clear()

