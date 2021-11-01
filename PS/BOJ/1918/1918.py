#!/usr/bin/env python3

PRIORITY = { '+': 1, '-': 1,
        '*': 2, '/': 2,
        '(': 0, ')': 0 }

if __name__ == '__main__':
    infix_formula = input()
    postfix_formula = ''
    op_stack = []

    for c in infix_formula:
        if c in PRIORITY.keys():
            # pass
            if len(op_stack) == 0 or c == '(' \
                    or PRIORITY[op_stack[-1]] < PRIORITY[c]:
                op_stack.append(c)
                continue
            if c == ')':
                while len(op_stack) > 0:
                    top = op_stack.pop()
                    if top == '(':
                        break
                    postfix_formula += top
                continue
                
            while len(op_stack) > 0 \
                    and PRIORITY[c] <= PRIORITY[op_stack[-1]]:
                top = op_stack.pop()
                postfix_formula += top
            op_stack.append(c)
        else:
            postfix_formula += c

    while len(op_stack) > 0:
        top = op_stack.pop()
        if top not in ('(', ')'):
            postfix_formula += top
    print(postfix_formula)
