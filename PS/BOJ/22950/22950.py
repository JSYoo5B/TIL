#!/usr/bin/env python3

if __name__ == '__main__':
    bin_len = int(input())
    binary = input()
    bin_radix = min(bin_len, int(input()))

    remain = binary[-bin_radix+1:]
    if bin_radix == 0 or '1' not in remain:
        print("YES")
    else:
        print("NO")
