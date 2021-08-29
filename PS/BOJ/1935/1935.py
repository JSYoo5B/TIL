#!/usr/bin/env python3

if __name__ == '__main__':
    cnt_vars = int(input())
    postfix = input()
    variables = []
    for _ in range(cnt_vars):
        var = int(input())
        variables.append(var)

    stack = []
    for c in postfix:
        if c == '+':
            op2 = stack.pop()
            op1 = stack.pop()
            result = op1 + op2
            stack.append(result)
        elif c == '-':
            op2 = stack.pop()
            op1 = stack.pop()
            result = op1 - op2
            stack.append(result)
        elif c == '*':
            op2 = stack.pop()
            op1 = stack.pop()
            result = op1 * op2
            stack.append(result)
        elif c == '/':
            op2 = stack.pop()
            op1 = stack.pop()
            result = op1 / op2
            stack.append(result)
        else:
            var_idx = ord(c) - ord('A')
            stack.append(variables[var_idx])
    answer = stack[0]
    print("{:.2f}".format(answer))
