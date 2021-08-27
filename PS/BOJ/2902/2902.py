#!/usr/bin/env python3

if __name__ == '__main__':
    title = input()
    names = title.split('-')
    abbreviate = ''
    for n in names:
        abbreviate += n[0]
    print(abbreviate)
