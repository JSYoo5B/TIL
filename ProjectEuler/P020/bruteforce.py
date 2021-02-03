#!/usr/bin/env python3
""" Brute-force solution
Evident
(This is evident for python and other environment which supports big integer)
"""

def factorial(num, memo):
    if num == 0:
        return memo[0]
    elif num > len(memo)-1:
        memo.append(num * factorial(num-1, memo))
    return memo[num]

if __name__ == '__main__':
    facto_memo = [1]
    factorial(100, facto_memo)
    
    digits = [int(d) for d in str(facto_memo[100])]
    answer = sum(digits)
    print(answer)
