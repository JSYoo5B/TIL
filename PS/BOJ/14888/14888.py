#!/usr/bin/env python3

def div(dividend, divisor):
    sign = 1 if dividend > 0 else -1
    quotient = abs(dividend) // divisor
    quotient *= sign
    return quotient

def get_formula_results(numbers, op_cnts, idx = 0, tmp_val = 0):
    if len(numbers) == idx:
        yield tmp_val
        return

    elif idx == 0:
        tmp_val = numbers[0]
        yield from get_formula_results(numbers, op_cnts, idx+1, tmp_val)
        return
    
    for op in range(4):
        if op_cnts[op] == 0:
            continue
        op_cnts[op] -= 1
        prev = tmp_val
        if op == 0:
            tmp_val += numbers[idx]
        elif op == 1:
            tmp_val -= numbers[idx]
        elif op == 2:
            tmp_val *= numbers[idx]
        else:
            tmp_val = div(tmp_val, numbers[idx])
        yield from get_formula_results(numbers, op_cnts, idx+1, tmp_val)
        tmp_val = prev
        op_cnts[op] += 1


if __name__ == '__main__':
    nums_cnt = int(input())
    numbers = list(map(int, input().split()))
    op_cnts = list(map(int, input().split()))

    avail_results = []
    formula_results = get_formula_results(numbers, op_cnts)
    for r in formula_results:
        avail_results.append(r)

    print(max(avail_results))
    print(min(avail_results))
