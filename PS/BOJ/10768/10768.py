#!/usr/bin/env python3

if __name__ == '__main__':
    month = int(input())
    day = int(input())
    conv_date = month * 30 + day
    base = 2 * 30 + 18
    if conv_date < base:
        print("Before")
    elif conv_date == base:
        print("Special")
    else:
        print("After")
