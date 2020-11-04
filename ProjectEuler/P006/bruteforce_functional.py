#!/usr/env/python3
""" Bruteforce
Obvious solution
"""
from functools import reduce

def square_of_sum(num):
    numbers = [x for x in range(1, num + 1)]
    sum = reduce(lambda x, y: x + y, numbers)

    return sum * sum

def sum_of_square(num):
    numbers = [x * x for x in range(1, num + 1)]
    sum = reduce(lambda x, y: x + y, numbers)
    return sum

if __name__ == '__main__':
    LIMIT = 100

    print(square_of_sum(LIMIT) - sum_of_square(LIMIT))
