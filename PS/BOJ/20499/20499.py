#!/usr/bin/env python3

if __name__ == '__main__':
    K, D, A = map(int, input().split('/'))
    if K + A < D or D == 0:
        print("hasu")
    else:
        print("gosu")
