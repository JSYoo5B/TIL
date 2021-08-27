#!/usr/bin/env python3

if __name__ == '__main__':
    s = input()
    suffix_arrays = [ s[i:] for i in range(len(s)) ]
    suffix_arrays.sort()
    for i in suffix_arrays:
        print(i)
