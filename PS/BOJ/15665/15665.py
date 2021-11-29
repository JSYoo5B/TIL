#!/usr/bin/env python3


def gen_picked_numbers(numbers, pick_cnt, cache = []):
    if pick_cnt == 0:
        yield cache
        return

    for n in numbers:
        cache.append(n)
        yield from gen_picked_numbers(numbers, pick_cnt-1, cache)
        cache.pop()

if __name__ == '__main__':
    numbers_cnt, pick_cnt = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers = list(set(numbers))
    numbers.sort()

    picked_numbers = gen_picked_numbers(numbers, pick_cnt)
    for p in picked_numbers:
        print(*p)
