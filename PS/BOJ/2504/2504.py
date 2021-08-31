#!/usr/bin/env python3

if __name__ == '__main__':
    string = input()
    stack = []
    invalid = False
    for c in string:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            temp = 0
            while len(stack) > 0:
                top = stack[-1]
                if isinstance(top, int):
                    temp += top
                    stack.pop()
                elif top == '(':
                    temp = 2 if temp == 0 else temp * 2
                    stack.pop()
                    stack.append(temp)
                    break
                else:
                    invalid = True
                    break
        elif c == ']':
            temp = 0
            while len(stack) > 0:
                top = stack[-1]
                if isinstance(top, int):
                    temp += top
                    stack.pop()
                elif top == '[':
                    temp = 3 if temp == 0 else temp * 3
                    stack.pop()
                    stack.append(temp)
                    break
                else:
                    invalid = True
                    break
        if invalid:
            break
    if len([ i for i in stack if isinstance(i, str) ]) > 0 or invalid:
        print(0)
    else:
        print(sum(stack))
