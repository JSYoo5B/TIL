#!/usr/bin/env python3

if __name__ == '__main__':
    num_cnt = int(input())
    numbers = []
    for i in range(num_cnt):
        num = int(input())
        if num == 0:
            numbers.pop()
        else:
            numbers.append(num)
    answer = sum(numbers)
    print(answer)
