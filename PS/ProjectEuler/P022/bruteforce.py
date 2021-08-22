#!/usr/bin/env python3
""" Brute-force solution
Evident
"""

def get_worth(name):
    worth = 0
    for a in name:
        worth += ord(a) - ord('A') + 1
    return worth

if __name__ == '__main__':
    names = []
    with open('p022_names.txt') as file:
        for i in file:
            tokens = i.split(',')
            for t in tokens:
                # Ignore double quotes for names
                names.append(t[1:-1])
    # need to sort in alphabetical order
    names.sort()

    namescores = []
    for idx, name in enumerate(names):
        namescores.append((idx + 1) * get_worth(name))
    answer = sum(namescores)

    print(answer)
