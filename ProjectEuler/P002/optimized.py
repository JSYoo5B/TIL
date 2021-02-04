#!/usr/bin/env python3
""" Optimized solution
1. Odd-even for fibonacci number has pattern
   Odd -> Odd -> Even -> Odd -> Odd -> Even ...
2. By these pattern, check 3 patterns
   F(n) = F(n-1) + F(n-2)
        = F(n-2) + F(n-3) + F(n-3) + F(n-4)
        = F(n-3) + F(n-4) + 2*F(n-3) + F(n-4)
        = 3*F(n-3) + 2*F(n-4)
        = 3*F(n-3) + F(n-4) + F(n-5) + F(n-6)
        = 3*F(n-3) + F(n-3) + F(n-6)
        = 4*F(n-3) + F(n-6)
3. For odd fibonacci numbers, recurrence relation is
   Odd(n) = 4*Odd(n-1) + Odd(n-2)
   Odd(0) = 0, Odd(1) = 2, Odd(2) = 8, Odd(3) = 34
"""

REQUEST = 4000000

if __name__ == '__main__':
    answer = 0
    fibo = [0, 2]
    while (fibo[-1] < REQUEST):
        answer += fibo[-1]
        fibo.append(4 * fibo[-1] + fibo[-2])
    print(answer)
