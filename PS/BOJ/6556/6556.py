#!/usr/bin/env python3

if __name__ == '__main__':
    while True:
        m, n = map(int, input().split())
        if m == 0 and n == 0:
            break
        elems_cnt = m + n
        subset_cnt = min(m, n)
        subset_cnt = min(subset_cnt, elems_cnt - subset_cnt)
        binom_coeff = 1
        for i in range(subset_cnt):
            binom_coeff *= (elems_cnt - i)
            binom_coeff //= (i + 1)
        print(binom_coeff)
