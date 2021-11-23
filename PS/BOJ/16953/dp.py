#!/usr/bin/env python3

if __name__ == '__main__':
    org, dst = map(int, input().split())

    count = 1
    while dst != org:
        if dst % 10 == 1:
            dst //= 10
            count += 1
        elif dst % 2 == 0:
            dst //= 2
            count += 1
        else:
            count = -1
            break
        if dst < org:
            count = -1
            break
    print(count)
