#!/usr/bin/env python3

if __name__ == '__main__':
    cnt = int(input())
    numbers = list(map(int, input().split()))

    coords = [ n for n in numbers ]
    coords = list(set(coords))
    coords.sort()
    coord_dict = {}
    for i in range(len(coords)):
        coord_dict[coords[i]] = i

    translates = [ coord_dict[n] for n in numbers ]
    print(' '.join([ str(n) for n in translates ]))
