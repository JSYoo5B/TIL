#!/usr/bin/env python3
""" Memoization solution
Collatz sequence for given number may be the part of other Collatz sequence
ex. 4 → 2 → 1 is partial Collatz sequence of 8 → 4 → 2 → 1
by these characteristic, pre-calculated Collatz sequence can be reusable.
Using memoization method can be solved by 2 approach: top-down and bottom-up.
Current problem condition says starting number must be under one million, but
the terms are allowed to go above one million.
Bottom-up approach (backtrack possible condition from 1) may produce unwanted
results, so this solution uses top-down approach.
"""

REQUEST=1000000

def get_collatz_length(memo, number):
    if memo.get(number) == None:
        # get next collatz sequence
        if number % 2 == 0:
            next = int(number / 2)
        else:
            next = 3 * number + 1
        # try to get next collatz sequence's length
        # and set given number's sequence length as incremented length
        if memo.get(next) == None:
            length = get_collatz_length(memo, next)
        else:
            length = memo[next]
        memo[number] = length + 1

    return memo[number]

if __name__ == '__main__':
    collatz_memo = {1:1}

    for i in range(1, REQUEST + 1):
        get_collatz_length(collatz_memo, i)

    answer = max(collatz_memo, key=collatz_memo.get)
    print(answer)
