#!/usr/bin/env python3

from math import sqrt

if __name__ == '__main__':
    hex_len = int(input())
    triangle_area = hex_len * hex_len * sqrt(3) / 2 / 2 
    print(triangle_area)
