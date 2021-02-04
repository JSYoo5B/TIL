#!/usr/bin/env python3
""" Brute-force solution
1. do loop from 1 to 1000
2. check if current number is multiples of 3 or 5
3. accumulate sum
expected time complexity = O(n)
"""

REQUEST = 1000

def is_mul_of(num, divisors):
    for d in divisors:
        if num % d == 0:
            return True
    return False

if __name__ == '__main__':
    answer = 0
    for i in range(1, REQUEST):
        if is_mul_of(i, [3, 5]):
            answer += i
    print(answer)
