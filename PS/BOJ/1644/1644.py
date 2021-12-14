#!/usr/bin/env python3


def sieve_of_eratosthenes(num):
    checks = [ True for _ in range(num+1) ]

    checks[0], checks[1] = False, False
    for i in range(2, int((num+1)**0.5) + 1):
        if checks[i] == 1:
            for comp in range(i**2, num+1, i):
                checks[comp] = False

    return [ i for i in range(num+1) if checks[i] ]


if __name__ == '__main__':
    tgt_num = int(input())
    primes = sieve_of_eratosthenes(tgt_num)
    local_sum, prime_sums = 0, [ 0 ]
    for p in primes:
        local_sum += p
        prime_sums.append(local_sum)
    
    kinds_cnt = 0
    l, r = 0, 1
    while l <= r and r < len(prime_sums):
        cont_sum = prime_sums[r] - prime_sums[l]
        if cont_sum == tgt_num:
            kinds_cnt += 1

        if cont_sum > tgt_num:
            l += 1
        else:
            if r < len(prime_sums)-1:
                r += 1
            else:
                l += 1
    print(kinds_cnt)
