#!/usr/bin/env python3
""" Brute-force solution
1. Generate fibonacci number till the number is less than 4M
2. When the fibonacci number is even, accumulate sum
expected time complexity = O(log n)
n refers to the number which must not exceed
"""

REQUEST = 4000000

if __name__ == '__main__':
    answer = 0
    fibo = [1, 2]
    while (fibo[-1] < REQUEST):
        if (fibo[-1] % 2 == 0):
            answer += fibo[-1]
        fibo.append(fibo[-1] + fibo[-2])
    print(answer)
