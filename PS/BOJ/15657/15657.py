#!/usr/bin/env python3

def get_permutes(numbers, remains, partial=[]):
    if remains == 0:
        yield partial
        return

    for i in range(len(numbers)):
        partial.append(numbers[i])
        yield from get_permutes(numbers[i:], remains-1, partial)
        partial.pop()

if __name__ == '__main__':
    nums_cnt, perm_len = map(int, input().split())
    numbers = list(map(int, input().split()))

    numbers.sort()

    permutes = get_permutes(numbers, perm_len)
    for p in permutes:
        print(*p)

