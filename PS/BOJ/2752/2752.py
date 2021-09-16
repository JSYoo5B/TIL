#!/usr/bin/env python3

if __name__ == '__main__':
    numbers = list(map(int, input().split()))
    numbers.sort()
    print(" ".join([str(n) for n in numbers]))
