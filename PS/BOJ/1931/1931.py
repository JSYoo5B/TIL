#!/usr/bin/env python3

if __name__ == '__main__':
    cnt_plans = int(input())
    plans = []
    for i in range(cnt_plans):
        plan = list(map(int, input().split()))
        plans.append(plan)

    plans.sort(key = lambda x: (x[1], x[0]))
    held_cnt = 0
    current = 0
    for p in plans:
        if current <= p[0]:
            # When the meeting start time is later or equal to current
            held_cnt += 1
            # Current time is the end time of meeting plan
            current = p[1]
    print(held_cnt)
