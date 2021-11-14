#!/usr/bin/env python3

def get_permutes(numbers, remains, partial=[]):
    if remains == 0:
        yield partial
        return

    for i in range(len(numbers)):
        # Skip same numbers
        if i > 0 and numbers[i] == numbers[i-1]:
            continue

        partial.append(numbers[i])
        yield from get_permutes(numbers[i:], remains-1, partial)
        partial.pop()


if __name__ == '__main__':
    numbers_cnt, perm_len = map(int, input().split())
    numbers = list(map(int, input().split()))
    
    numbers.sort()

    perms = get_permutes(numbers, perm_len)

    for p in perms:
        print(*p)
