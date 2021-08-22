#!/usr/bin/env python3

if __name__ == '__main__':
    numbers = []
    for i in range(10):
        num = int(input())
        numbers.append(num)

    remainders = [ i % 42 for i in numbers ]
    uniques = set(remainders)
    print(len(uniques))
