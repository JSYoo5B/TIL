#!/usr/bin/env python3
""" Brute-force solution
Evident
(This is evident for python and other environment which supports big integer)
"""

def self_power(num):
    return num ** num

REQUEST = 10
if __name__ == '__main__':
    self_powers = []
    for i in range(1, 1000+1):
        self_powers.append(self_power(i))
    answer = sum(self_powers) % (10 ** REQUEST)
    print(answer)
