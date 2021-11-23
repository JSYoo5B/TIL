#!/usr/bin/env python3

N_QUEEN = [ 0, 1, 0, 0, 2, 10, 4, 40, 92, 352, \
        724, 2680, 14200, 73712, 365596, 2279184 ]

if __name__ == '__main__':
    tbl_size = int(input())
    answer = N_QUEEN[tbl_size]
    print(answer)
