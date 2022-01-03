#!/usr/bin/env python3

def calc(op1, op, op2):
    answer = 0
    if op == '+':
        answer = op1 + op2
    elif op == '*':
        answer = op1 * op2
    elif op == '-':
        answer = op1 - op2
    return answer


def get_formula_results(nums, ops, precalcs, acc = 0, idx = 0):
    if len(ops) == 0:
        yield nums[0]
        return
    elif idx >= len(ops):
        yield acc
        return
    elif idx == 0:
        acc = nums[0]

    if idx + 2 <= len(ops):
        tmp = calc(acc, ops[idx], precalcs[idx+1])
        yield from get_formula_results(nums, ops, precalcs, tmp, idx + 2)
    tmp = calc(acc, ops[idx], nums[idx+1])
    yield from get_formula_results(nums, ops, precalcs, tmp, idx + 1)


if __name__ == '__main__':
    formula_len = int(input())
    formula = input()
    
    nums = [ int(formula[i]) for i in range(0, formula_len, 2) ]
    ops = [ formula[i] for i in range(1, formula_len, 2) ]
    precalcs = [ calc(nums[i], ops[i], nums[i+1]) for i in range(0, formula_len // 2) ]

    answers = list(get_formula_results(nums, ops, precalcs))
    print(max(answers))
