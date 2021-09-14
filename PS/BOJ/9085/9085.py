#!/usr/bin/env python3

if __name__ == '__main__':
    test_cnt = int(input())
    for _ in range(test_cnt):
        n = int(input())
        numbers = list(map(int, input().split()))
        answer = sum(numbers)
        print(answer)
