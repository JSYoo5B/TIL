#!/usr/bin/env python3
""" Build from scratch solution
Calculate the order of permutation using factorial
"""

facto_memo = [1]

def factorial(num, memo):
    if num == 0:
        return memo[0]
    elif num > len(memo)-1:
        memo.append(num * factorial(num-1, memo))
    return memo[num]

def get_permutation(elems, nth):
    if nth == 0:
        return elems
    divisor = factorial(len(elems) - 1, facto_memo)
    idx, remainder = divmod(nth, divisor)
    return [elems[idx]] \
            + get_permutation([x for x in elems if x != elems[idx]], remainder)

REQUEST = 1000000

if __name__ == '__main__':
    elements = [x for x in range(0,9+1)]
    answer = get_permutation(elements, REQUEST-1)
    print(answer)

