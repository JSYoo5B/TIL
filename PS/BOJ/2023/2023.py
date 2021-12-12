#!/usr/bin/env python3

STARTS_WITH = [2, 3, 5, 7]
ENDS_WITH = [1, 3, 7, 9]

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_primes(num, length):
    if len(str(num)) == length:
        yield num
        return

    for e in ENDS_WITH:
        next = num * 10 + e
        if is_prime(next):
            yield from get_primes(num * 10 + e, length)

if __name__ == '__main__':
    length = int(input())

    for s in STARTS_WITH:
        primes = get_primes(s, length)
        for p in primes:
            print(p)
