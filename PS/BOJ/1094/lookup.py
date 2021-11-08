#!/usr/bin/env python3

bits = [0]

while len(bits) <= 64:
    next = [ i + 1 for i in bits ]
    bits += next

if __name__ == '__main__':
    req_len = int(input())
    answer = bits[req_len]
    print(answer)
