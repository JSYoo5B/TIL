#!/usr/bin/env python3
""" Factorization
1.  Set divisor(prime factor) to 2
2.  Check if current divisor is complete divisor for given number
    When it is complete divisor, update given number to the quotient.
    Otherwise, increase divisor. (For complete divisor, don't increase yet)
3.  Repeat this step until the given number becomes 1. (fully divided)
4.  Recent divisor is the largest prime factor
Reason:
    By setting the divisor with 2, the smallest prime number, all multipled
    factors will be divided into prime factors. (When the current factor
    is not completely divisible, then it increases)
    All number's prime factors are consisted by the less or equal number of
    itself. The looping direction "Increase factor" means other less prime
    factorization were done already.
"""

REQUEST = 600851475143

if __name__ == '__main__':
    required = REQUEST

    curr_factor = 2
    max_factor = 0
    while required != 1:
        if required % curr_factor == 0:
            max_factor = curr_factor
            required /= curr_factor
        else:
            curr_factor += 1

    print(max_factor)
