#!/usr/bin/env python3

def get_permutations(pool, remain, current = []):
    if remain == 0:
        yield current
        return

    for n in pool:
        current.append(n)
        yield from get_permutations(pool, remain-1, current)
        current.pop()


if __name__ == '__main__':
    nums_cnt, perm_len = map(int, input().split())
    nums = [ i+1 for i in range(nums_cnt) ]

    perms = get_permutations(nums, perm_len)
    for p in perms:
        print(*p)
