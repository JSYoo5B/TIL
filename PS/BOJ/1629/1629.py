#!/usr/bin/env python3

def divconq_pow_mod(base, pow, mod, cache = []):
    if len(cache) < pow:
        cache = [1, base % mod]
    answer = cache[pow % 2]
    if pow >= 2:
        answer = divconq_pow_mod(base, pow // 2, mod, cache) ** 2 * cache[pow % 2]
        answer %= mod
    return answer


if __name__ == '__main__':
    base, pow, mod = map(int, input().split())
    answer = divconq_pow_mod(base, pow, mod)
    print(answer)
