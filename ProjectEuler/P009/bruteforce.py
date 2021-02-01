#!/usr/bin/env python3
""" Brute-force solution
1. There are following conditions/facts
  1) a < b < c
  2) a^2 + b^2 = c^2
  3) a + b + c = 1000
  4) a + b > c (because it's triangle)
2. We can derive following facts
  1) c < 500
     a + b = 1000 - c, 1000 - c > c
  2) c > 333
     a < b < c, a + b + c = 1000, 3c > 1000
"""

def is_pythagorean_triplet(a, b, c):
    return a*a + b*b == c*c

if __name__ == '__main__':
    for c in range(333, 500):
        for a in range(2, int((1000 - c) / 2)):
            b = 1000 - c - a
            if is_pythagorean_triplet(a, b, c):
                print(a * b * c)

