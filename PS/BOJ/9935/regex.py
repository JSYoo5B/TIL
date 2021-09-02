#!/usr/bin/env python3

""" Time Limit Exceed solution
Worst time complexity: O(n^2)
1. When the pattern is 'AB' and the given string is in nested pattern
   (ex. AAAABBBB)
2. In single loop, string.replace removes only single pattern
3. It must loop until it ends nested pattern
"""

import sys

if __name__ == '__main__':
    origin = sys.stdin.readline().strip()
    pattern = sys.stdin.readline().strip()
    
    modified = origin
    while True:
        origin = modified
        modified = origin.replace(pattern, '')
        if modified == origin:
            break
    if modified == '':
        print('FRULA')
    else:
        print(modified)
