#!/usr/bin/env python3

class Stack:
    def __init__(self):
        self.container = []
    def push(self, x):
        self.container.append(x)
    def pop(self):
        if len(self.container) == 0:
            return -1
        top = self.container[-1]
        self.container.pop()
        return top
    def size(self):
        return len(self.container)
    def empty(self):
        if len(self.container) == 0:
            return 1
        return 0
    def top(self):
        if len(self.container) == 0:
            return -1
        return self.container[-1]

if __name__ == '__main__':
    op_cnt = int(input())
    s = Stack()
    for _ in range(op_cnt):
        operation = input()
        arg = 0
        if operation.startswith('push'):
            arg = int(operation.split()[1])
            operation = operation.split()[0]

        if operation == 'push':
            s.push(arg)
        elif operation == 'pop':
            print(s.pop())
        elif operation == 'size':
            print(s.size())
        elif operation == 'empty':
            print(s.empty())
        elif operation == 'top':
            print(s.top())
