#!/usr/bin/env python3

from sys import stdin
input = lambda : stdin.readline().rstrip()

def get_avail_num(digits, length, prev = 0):
    if length == 0:
        yield prev
        return

    prev *= 10
    for d in digits:
        yield from get_avail_num(digits, length-1, prev+d)


if __name__ == '__main__':
    nums_cnt = int(input())
    num_lens = list(map(int, input().split()))
    digits_cnt = int(input())
    digits = list(map(int, input().split()))

    avail_nums = [ None for _ in range(max(num_lens[:-1]) + 1) ]
    for n in num_lens[:-1]:
        if avail_nums[n] is not None:
            continue

        avail_nums[n] = set(get_avail_num(digits, n))

    o1_len, o2_len, res_len = num_lens[0], num_lens[1], num_lens[-1]
    cand_combs = []
    for op1 in avail_nums[o1_len]:
        for op2 in avail_nums[o2_len]:
            res_digits = str(op1 * op2)
            if len(res_digits) != res_len:
                continue
            valid = True
            for r in res_digits:
                if int(r) not in digits:
                    valid = False
                    break
            if valid:
                cand_combs.append([op1, op2])

    answer = 0
    part_lens = num_lens[2:-1]
    for op1, op2 in cand_combs:
        valid = True
        digits = [ int(d) for d in str(op2) ]
        for i in range(o2_len):
            if op1 * digits[i] not in avail_nums[part_lens[i]]:
                valid = False
                break
        if valid:
            answer += 1

    print(answer)
