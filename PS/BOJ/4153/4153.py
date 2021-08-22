#!/usr/bin/env python3

if __name__ == '__main__':
    while True:
        lines = list(map(int, input().split()))
        if sum(lines) == 0:
            break

        lines.sort()
        if (lines[0] ** 2 + lines[1] ** 2) == (lines[2] ** 2):
            if lines[0] + lines[1] > lines[2]:
                print('right')
            else:
                print('wrong')
        else:
            print('wrong')
