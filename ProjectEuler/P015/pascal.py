#!/usr/bin/env python3
""" Pascal's triangle
Lattice paths are in form of Pascal's triangle
C(n, k) means binomial coefficient
1x1 grid: 2 = C(2, 1)
2x2 grid: 6 = C(4, 2)
3x3 grid: 20 = C(6, 3)
by these pattern, NxN grid = C(2N, N)
"""

REQUEST = 20

def binomial_coeff(n, k):
    result = 1
    # calculate n!/k!
    for i in range(k+1, n+1):
        result *= i
    # divide into (n-k!):
    for i in range(1, n-k+1):
        result /= i
    return int(result)

if __name__ == '__main__':
    answer = binomial_coeff(2 * REQUEST, REQUEST)

    print(answer)
