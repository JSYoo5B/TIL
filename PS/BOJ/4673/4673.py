#!/usr/bin/env python3

def d_func(num):
    for d in str(num):
        num += int(d)
    return num

if __name__ == '__main__':
    gen_numbers = set()
    for i in range(10000 + 1):
        gen_numbers.add(d_func(i))
    self_numbers = [ i for i in range(10000 + 1) if i not in gen_numbers ]
    for n in self_numbers:
        print(n)
