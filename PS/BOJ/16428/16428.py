#!/usr/bin/env python3

if __name__ == '__main__':
    A, B = map(int, input().split())
    quotient = A // B if B > 0 else A // (B * -1) * -1
    remainder = A % B if B > 0 else A % (B * -1)
    print(quotient)
    print(remainder)
