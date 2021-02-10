#!/usr/bin/env python3

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    powers = [x ** 2 for x in nums]
    crc = sum(powers) % 10
    print(crc)
