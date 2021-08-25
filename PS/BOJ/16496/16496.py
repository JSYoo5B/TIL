#!/usr/bin/env python3

from functools import cmp_to_key

if __name__ == '__main__':
    cnt_nums = int(input())
    numbers = list(input().split())
    
    numbers.sort(key=cmp_to_key(lambda a, b: 1 if int(a+b) < int(b+a) else -1))
    greatest = ''.join(numbers)
    answer = int(greatest)
    print(answer)
