#!/usr/bin/env python3

if __name__ == '__main__':
    dividend, divisor = map(int, input().split(' '))
    quot, remain = divmod(dividend, divisor)
    print(quot)
    print(remain)

