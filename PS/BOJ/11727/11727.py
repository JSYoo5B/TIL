#!/usr/bin/env python3

if __name__ == '__main__':
    width = int(input())

    vars = []
    vars.append(0)
    vars.append(1)
    vars.append(3)
    for i in range(3, width+1):
        next = vars[-1] + vars[-2]*2
        next %= 10007
        vars.append(next)

    answer = vars[width]
    print(answer)
