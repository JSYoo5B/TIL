#!/usr/bin/env python3

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        elems_cnt = m + n - 2
        subset_cnt = min(m, n) - 1
        subset_cnt = min(subset_cnt, elems_cnt - subset_cnt)
        binom_coeff = 1
        for i in range(subset_cnt):
            binom_coeff *= (elems_cnt - i)
            binom_coeff //= (i + 1)
        return binom_coeff
