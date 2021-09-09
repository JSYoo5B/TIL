#!/usr/bin/env python3

if __name__ == '__main__':
    A, B = map(int, input().split())
    answer = (A + B) * (A - B)
    print(answer)
