#!/usr/bin/env python3

from sys import stdin
input = lambda :stdin.readline().rstrip()

def run_go_stack(init_val, ops):
    stack = [init_val]
    for op in ops:
        if op in ['POP', 'INV', 'DUP'] and len(stack) == 0:
            return "ERROR"
        elif op in ['SWP', 'ADD', 'SUB', 'MUL', 'DIV', 'MOD'] and len(stack) < 2:
            return "ERROR"
        elif op in ['DIV', 'MOD'] and stack[-1] == 0:
            return "ERROR"
        elif op.startswith("NUM"):
            operand = int(op.split()[1])
            stack.append(operand)
        elif op == 'POP':
            stack.pop()
        elif op == 'INV':
            stack[-1] *= -1
        elif op == 'DUP':
            stack.append(stack[-1])
        elif op == 'SWP':
            stack[-1], stack[-2] = stack[-2], stack[-1]
        elif op == 'ADD':
            operand = stack.pop()
            stack[-1] += operand
        elif op == 'SUB':
            operand = stack.pop()
            stack[-1] -= operand
        elif op == 'MUL':
            operand = stack.pop()
            stack[-1] *= operand
        elif op == 'DIV':
            a, b = stack.pop(), stack.pop()
            temp = abs(b) // abs(a)
            if (a > 0 and b < 0) or (a < 0 and b > 0):
                temp = -temp
            stack.append(temp)
        elif op == 'MOD':
            a, b = stack.pop(), stack.pop()
            temp = abs(b) % abs(a)
            if b < 0:
                temp = -temp
            stack.append(temp)
        elif op == 'END' and len(stack) != 1:
            return "ERROR"
        if len(stack) > 0 and abs(stack[-1]) > 10 ** 9:
            return "ERROR"
    return stack[0]


if __name__ == '__main__':
    while True:
        op = input()
        if op == 'QUIT':
            break

        ops = [ op ]
        while op != 'END':
            op = input()
            ops.append(op)

        nums_cnt = int(input())
        for _ in range(nums_cnt):
            num = int(input())
            answer = run_go_stack(num, ops)
            print(answer)

        # Handle blanks
        input()
        print()
