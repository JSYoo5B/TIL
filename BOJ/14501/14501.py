#!/usr/bin/env python3

if __name__ == '__main__':
    days = int(input())
    profit_tbl = []
    for i in range(days):
        profit_row = list(map(int, input().split()))
        profit_tbl.append(profit_row)
    
    profit_calc = [ 0 for i in range(days+1)]
    for d in range(days-1, -1, -1):
        duration, profit = profit_tbl[d][0], profit_tbl[d][1]
        # skip if duration exceeds final day
        if d + duration > days:
            profit_calc[d] = profit_calc[d+1]
            continue;
        profit_calc[d] = max(profit_calc[d+1], \
                profit_calc[d+duration] + profit)
    print(profit_calc[0])

