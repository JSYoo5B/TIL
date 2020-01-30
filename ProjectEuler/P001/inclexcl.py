#!/usr/bin/env python3
""" Inclusion-exclusion principle
1. Get sum of arithmetic sequence about multiples of 3
2. Get sum of arithmetic sequence about multiples of 5
3. Get sum of arithmetic sequence about multiples of 15 (LCM)
answer = (1) + (2) + (3)
expected time complexity = O(1)
"""

REQUEST = 1000

def arith_sum_till(num, limit):
    # Find greatest, not exceeding limit, multiple of num
    while limit % num != 0:
        limit -= 1

    arith_sum = (limit / num) * (num + limit) / 2
    return int(arith_sum)

if __name__ == '__main__':
    sum_3 = arith_sum_till(3, REQUEST)
    sum_5 = arith_sum_till(5, REQUEST)
    sum_15 = arith_sum_till(15, REQUEST)

    answer = sum_3 + sum_5 - sum_15

    print(answer)
