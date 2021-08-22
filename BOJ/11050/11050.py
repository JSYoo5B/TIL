#!/usr/bin/env python3

def binomial_coeff(n, r):
    # Reduce r to smaller value
    r = min(r, n-r)
    answer = 1
    for i in range(n, n-r, -1):
        answer *= i
    for j in range(1, r+1):
        answer //= j
    return answer

if __name__ == '__main__':
    N, K = map(int, input().split())
    answer = binomial_coeff(N, K)

    print(answer)

