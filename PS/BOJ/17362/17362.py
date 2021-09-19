#!/usr/bin/env python3

if __name__ == '__main__':
    given = int(input())
    remainder = (given - 1) % 8
    if remainder <= 4:
        answer = remainder + 1
    else:
        answer = 9 - remainder
    print(answer)
