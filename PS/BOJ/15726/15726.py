#!/usr/bin/env python3

if __name__ == '__main__':
    A, B, C = map(int, input().split())
    answer = max(int(A * B / C), int(A / B * C))
    print(answer)
