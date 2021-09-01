#!/usr/bin/env python3

if __name__ == '__main__':
    test_cnt = int(input())
    for _ in range(test_cnt):
        n = int(input())
        upper_row = list(map(int, input().split()))
        below_row = list(map(int, input().split()))
        prices = [upper_row, below_row]

        memo = [ [prices[0][0], prices[1][0], 0] ]
        for i in range(1, n):
            upper_select = max(memo[-1][1], memo[-1][2]) + prices[0][i]
            below_select = max(memo[-1][0], memo[-1][2]) + prices[1][i]
            none_select = max(memo[-1][0], memo[-1][1])
            memo.append([upper_select, below_select, none_select])
        answer = max(memo[-1])
        print(answer)
