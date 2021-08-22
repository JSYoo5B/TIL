#!/usr/bin/env python3

if __name__ == '__main__':
    while True:
        number_str = input()
        if number_str == '0':
            break
        rev_str = number_str[::-1]
        if rev_str == number_str:
            print('yes')
        else:
            print('no')
