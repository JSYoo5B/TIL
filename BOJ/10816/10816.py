#!/usr/bin/env python3

if __name__ == '__main__':
    cnt_numbers = int(input())
    numbers = list(map(int, input().split()))
    num_dict = dict()
    for i in numbers:
        cnt = num_dict.get(i, 0)
        num_dict[i] = cnt + 1

    cnt_finds = int(input())
    finds = list(map(int, input().split()))
    results = [ num_dict.get(i, 0) for i in finds ]
    print(' '.join([ str(i) for i in results ]))
