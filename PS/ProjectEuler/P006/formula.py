#!/usr/bin/env python
""" Using the formulas
square of sum = (n * (n+1) / 2)^2
sum of square = n * (n+1) * (2n+1) / 6
answer = (n/4 + 1/6) * (n^2 - 1)
"""
def square_of_sum(n):
    return (n * (n + 1) / 2) * (n * (n + 1) / 2)

def sum_of_square(n):
    return n * (n + 1) * (2 * n + 1) / 6

if __name__ == '__main__':
    LIMIT = 100
    
    print(square_of_sum(LIMIT) - sum_of_square(LIMIT))

