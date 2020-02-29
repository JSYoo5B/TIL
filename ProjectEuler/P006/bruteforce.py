#!/usr/env/python3
""" Bruteforce
Obvious solution
"""

def square_of_sum(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i

    return sum * sum

def sum_of_square(num):
    sum = 0
    for i in range(1, num + 1):
        sum += (i * i)

    return sum

if __name__ == '__main__':
    LIMIT = 100

    print(square_of_sum(LIMIT) - sum_of_square(LIMIT))
